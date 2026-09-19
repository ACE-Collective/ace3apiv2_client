"""schema coverage test for aceapi-v2-client

the package under ``aceapi_v2_client/api`` is generated from the vendored
``openapi.json``. this test is the guard that the two never drift apart: every
operation the schema declares must have a generated endpoint module exposing the
four call styles, and no module may linger for an operation the api dropped.

it needs no running instance -- it reads the committed schema and imports the
committed package, so it runs offline and in ci.

when it fails, the fix is almost always to regenerate:

    scripts/regenerate.sh https://localhost:8443/api/v2/openapi.json
"""

import importlib
import json
import re
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent
SCHEMA_PATH = PROJECT_ROOT / "openapi.json"
API_ROOT = PROJECT_ROOT / "aceapi_v2_client" / "api"

HTTP_METHODS = ("get", "post", "put", "patch", "delete")

# the four functions openapi-python-client emits for every operation
ENDPOINT_FUNCTIONS = ("sync", "sync_detailed", "asyncio", "asyncio_detailed")


def _schema_operations():
    """every operation in the vendored schema, as (module_name, method, path)

    the generator derives a module name from the operationId by collapsing the
    runs of underscores that fastapi's path templating leaves behind
    (``get_alert_alerts__alert_uuid__get`` -> ``get_alert_alerts_alert_uuid_get``)
    and the package from the operation's first tag.
    """
    schema = json.loads(SCHEMA_PATH.read_text())
    operations = []
    for path, item in schema["paths"].items():
        for method, operation in item.items():
            if method not in HTTP_METHODS:
                continue
            tag = operation.get("tags", ["default"])[0]
            package = tag.replace("-", "_")
            module = re.sub(r"_+", "_", operation["operationId"])
            operations.append((f"{package}.{module}", method.upper(), path))
    return sorted(operations)


def _generated_modules():
    """every generated endpoint module, as dotted ``package.module`` names"""
    return {
        f"{path.parent.name}.{path.stem}"
        for path in API_ROOT.glob("*/*.py")
        if path.name != "__init__.py"
    }


SCHEMA_OPERATIONS = _schema_operations()


def test_schema_has_operations():
    # a truncated or unparseable schema would make every other assertion here
    # vacuously pass, so pin the floor
    assert len(SCHEMA_OPERATIONS) > 50


@pytest.mark.parametrize(
    "module_name,method,path",
    SCHEMA_OPERATIONS,
    ids=[f"{method} {path}" for _, method, path in SCHEMA_OPERATIONS],
)
def test_operation_has_endpoint_module(module_name, method, path):
    # every documented operation is callable from the client, in all four styles
    module = importlib.import_module(f"aceapi_v2_client.api.{module_name}")
    for function_name in ENDPOINT_FUNCTIONS:
        assert callable(getattr(module, function_name, None)), (
            f"{module_name} is missing {function_name}()"
        )


def test_no_stale_endpoint_modules():
    # the mirror of the test above: a module left behind for an operation the api
    # removed would keep compiling and fail only at call time against a 404
    expected = {module_name for module_name, _, _ in SCHEMA_OPERATIONS}
    assert _generated_modules() - expected == set()
