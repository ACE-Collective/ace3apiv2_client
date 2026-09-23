# aceapi-v2-client

A Python client library for the **ACE (Analysis Correlation Engine) API v2**.

The client is generated from the API's OpenAPI schema with
[openapi-python-client](https://github.com/openapi-generators/openapi-python-client),
so every endpoint and model is fully typed. A small hand-written `auth` module
adds convenience helpers for ACE's API-key authentication.

## Installation

```bash
pip install aceapi-v2-client
```

Or install from a checkout of this directory:

```bash
pip install .
```

Requires Python 3.9+.

## Quickstart (API key)

ACE's primary machine-to-machine authentication is an API key sent in the
`x-ace-auth` header. Use the `authenticated_client` helper to build a client
with that header pre-populated:

```python
from aceapi_v2_client.auth import authenticated_client
from aceapi_v2_client.api.common import ping_common_ping_get
from aceapi_v2_client.api.observables import (
    list_observable_types_observable_types_get,
)

client = authenticated_client(
    base_url="https://localhost:8443/api/v2",
    api_key="YOUR-API-KEY",
    verify_ssl=False,  # development instances use a self-signed certificate
)

# a simple authenticated health check
pong = ping_common_ping_get.sync(client=client)
print(pong.result)  # "pong"

# call a data endpoint — responses are parsed into typed models
types = list_observable_types_observable_types_get.sync(client=client)
print(types)
```

Every endpoint module under `aceapi_v2_client.api.*` exposes four functions:

| function          | returns                          |
| ----------------- | -------------------------------- |
| `sync(...)`       | the parsed body (or `None`)      |
| `sync_detailed(...)` | a `Response` with status + parsed body |
| `asyncio(...)`    | the parsed body, async           |
| `asyncio_detailed(...)` | a `Response`, async         |

All take `client=` as a keyword argument plus any path/query/body parameters
the operation defines.

### Searching alerts

`POST /search/alerts` takes ACE's alert query language — free text plus any
number of `field:value` terms:

```python
from aceapi_v2_client.api.search import search_alerts_search_alerts_post
from aceapi_v2_client.models import AlertSearchRequest

results = search_alerts_search_alerts_post.sync(
    client=client,
    body=AlertSearchRequest(query="disposition:DELIVERY alert_date:-7d"),
)
print(results.total)
for result in results.results:
    # each result wraps the alert summary plus its ranking metadata
    print(result.rank, result.score, result.alert.uuid, result.alert.description)
```

Terms may be inverted with a leading `-`, ORed by separating values with commas,
and quoted when a value contains a space. `detection_point:<signature uuid>[:<version>]`
narrows to alerts with a detection point from that signature; the same filter is
available structurally as `SearchFiltersBody(detection_points=[...])`.
`POST /search/similar` takes an alert UUID instead and returns the alerts nearest
to it.

### Async usage

```python
import asyncio
from aceapi_v2_client.auth import authenticated_client
from aceapi_v2_client.api.common import ping_common_ping_get

client = authenticated_client("https://localhost:8443/api/v2", "YOUR-API-KEY",
                              verify_ssl=False)

async def main():
    async with client as c:
        print(await ping_common_ping_get.asyncio(client=c))

asyncio.run(main())
```

## API keys are scoped

An API key carries its own permission scope. A key's **effective permission is
the intersection of that scope with its owner's permissions** — a key can never
do more than its owner, and a restricted key does strictly less. A key created
with "inherit" scope simply gets whatever its owner has.

The practical consequence for client code: a call can fail with
`403 {"detail": "Permission denied"}` even though the key is valid and the owner
is privileged, because the *key* is scoped too narrowly. Most read/write
endpoints are permission-gated — including `/observable-types/`, the
`observable-*`, `threat*`, `search`, `alerts` and `crashes` endpoints, and
`/common/valid_*`. Only `/health/ping`, `/common/ping`,
`/common/supported_api_version`, and `/users/me/apikeys` are reachable with any
valid key.

**Self-service endpoints are the exception in the other direction.** `/users/me`,
`/users/me/preferences*` and the saved-filter endpoints act only on the caller's
own account and GUI state, so they check no permission at all — but they *do*
require a credential that carries no narrowing scope. An inherit-scoped key (or
the GUI's session cookie) passes; a key issued for one narrow machine task gets
`403 {"detail": "Permission denied"}` no matter how privileged its owner is.

Keys are **display-once**: the plaintext is returned only by the create call and
is never recoverable afterward. Mint one with `POST /users/{user_id}/apikeys`
(requires `user:write`) or from the CLI:

```bash
ace user add-api-key    # also: list-api-keys, revoke-api-key
```

To see your own keys — metadata only, never the secret:

```python
from aceapi_v2_client.api.users import list_my_api_keys_users_me_apikeys_get

for key in list_my_api_keys_users_me_apikeys_get.sync(client=client):
    print(key.id, key.name, key.inherit_user_scope, key.scope)
```

> JWT/OAuth2 login (`POST /auth/token`, `POST /auth/refresh`) and the
> `token_client` helper were removed. The API key above is the only mechanism
> available to a machine client.

## Endpoint coverage

The client covers **every endpoint the API publishes** — all 73 operations
across the groups below. `tests/test_coverage.py` enforces this: it reads the
vendored `openapi.json`, imports the matching module for each operation, and
fails if the API grew an endpoint the client has not been regenerated for (or
kept one the API dropped). It needs no running instance.

<details>
<summary><code>aceapi_v2_client.api.alerts</code> — 4 operations</summary>

| operation | module |
| --------- | ------ |
| `POST /alerts/bulk-add-observable` | `bulk_add_observable_alerts_bulk_add_observable_post` |
| `GET /alerts/{alert_uuid}` | `get_alert_alerts_alert_uuid_get` |
| `GET /alerts/{alert_uuid}/download` | `download_alert_alerts_alert_uuid_download_get` |
| `GET /alerts/{alert_uuid}/logs` | `view_alert_logs_alerts_alert_uuid_logs_get` |

</details>

<details>
<summary><code>aceapi_v2_client.api.common</code> — 5 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /common/ping` | `ping_common_ping_get` |
| `GET /common/supported_api_version` | `supported_api_version_common_supported_api_version_get` |
| `GET /common/valid_companies` | `valid_companies_common_valid_companies_get` |
| `GET /common/valid_directives` | `valid_directives_common_valid_directives_get` |
| `GET /common/valid_observables` | `valid_observables_common_valid_observables_get` |

</details>

<details>
<summary><code>aceapi_v2_client.api.crashes</code> — 3 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /crashes/` | `list_crash_reports_crashes_get` |
| `GET /crashes/{crash_id}` | `get_crash_report_crashes_crash_id_get` |
| `GET /crashes/{crash_id}/download` | `download_crash_report_crashes_crash_id_download_get` |

</details>

<details>
<summary><code>aceapi_v2_client.api.detection</code> — 5 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /detection/` | `list_detections_detection_get` |
| `POST /detection/` | `create_detection_detection_post` |
| `GET /detection/types` | `observable_types_detection_types_get` |
| `DELETE /detection/{detection_id}` | `delete_detection_detection_detection_id_delete` |
| `PATCH /detection/{detection_id}/expiration` | `set_expiration_detection_detection_id_expiration_patch` |

</details>

<details>
<summary><code>aceapi_v2_client.api.events</code> — 4 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /events/export` | `export_events_events_export_get` |
| `GET /events/open` | `open_events_events_open_get` |
| `PATCH /events/{event_id}` | `update_event_status_events_event_id_patch` |
| `GET /events/{event_ref}` | `get_event_events_event_ref_get` |

</details>

<details>
<summary><code>aceapi_v2_client.api.health</code> — 1 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /health/ping` | `ping_health_ping_get` |

</details>

<details>
<summary><code>aceapi_v2_client.api.nodes</code> — 4 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /nodes/` | `list_nodes_nodes_get` |
| `GET /nodes/{node_id}` | `get_node_nodes_node_id_get` |
| `POST /nodes/{node_id}/drain` | `drain_node_nodes_node_id_drain_post` |
| `POST /nodes/{node_id}/resume` | `resume_node_nodes_node_id_resume_post` |

</details>

<details>
<summary><code>aceapi_v2_client.api.observables</code> — 7 operations</summary>

| operation | module |
| --------- | ------ |
| `POST /observable-comments/` | `create_comment_observable_comments_post` |
| `DELETE /observable-comments/{comment_id}` | `delete_comment_observable_comments_comment_id_delete` |
| `PATCH /observable-comments/{comment_id}` | `update_comment_observable_comments_comment_id_patch` |
| `GET /observable-comments/{observable_id}` | `list_comments_observable_comments_observable_id_get` |
| `GET /observable-types/` | `list_observable_types_observable_types_get` |
| `PATCH /observables/interesting` | `set_interesting_observables_interesting_patch` |
| `POST /observables/lookup` | `lookup_observables_observables_lookup_post` |

</details>

<details>
<summary><code>aceapi_v2_client.api.saved_filters</code> — 7 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /saved-filters/` | `list_saved_filters_saved_filters_get` |
| `POST /saved-filters/` | `create_saved_filter_saved_filters_post` |
| `PUT /saved-filters/quick-filters` | `set_quick_filters_saved_filters_quick_filters_put` |
| `PUT /saved-filters/scratch/{kind}` | `upsert_scratch_filter_saved_filters_scratch_kind_put` |
| `DELETE /saved-filters/{filter_uuid}` | `delete_saved_filter_saved_filters_filter_uuid_delete` |
| `GET /saved-filters/{filter_uuid}` | `get_saved_filter_saved_filters_filter_uuid_get` |
| `PATCH /saved-filters/{filter_uuid}` | `update_saved_filter_saved_filters_filter_uuid_patch` |

</details>

<details>
<summary><code>aceapi_v2_client.api.search</code> — 2 operations</summary>

| operation | module |
| --------- | ------ |
| `POST /search/alerts` | `search_alerts_search_alerts_post` |
| `POST /search/similar` | `similar_alerts_search_similar_post` |

</details>

<details>
<summary><code>aceapi_v2_client.api.secrets</code> — 3 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /secrets/` | `list_secrets_secrets_get` |
| `DELETE /secrets/{key}` | `delete_secret_secrets_key_delete` |
| `PUT /secrets/{key}` | `set_secret_secrets_key_put` |

</details>

<details>
<summary><code>aceapi_v2_client.api.threats</code> — 8 operations</summary>

| operation | module |
| --------- | ------ |
| `GET /threat-types/` | `list_threat_types_threat_types_get` |
| `POST /threat-types/` | `create_threat_type_threat_types_post` |
| `DELETE /threat-types/{threat_type_id}` | `delete_threat_type_threat_types_threat_type_id_delete` |
| `GET /threat-types/{threat_type_id}` | `get_threat_type_threat_types_threat_type_id_get` |
| `PATCH /threat-types/{threat_type_id}` | `update_threat_type_threat_types_threat_type_id_patch` |
| `DELETE /threats/` | `delete_threat_threats_delete` |
| `GET /threats/` | `list_threats_threats_get` |
| `POST /threats/` | `create_threat_threats_post` |

</details>

<details>
<summary><code>aceapi_v2_client.api.users</code> — 20 operations</summary>

| operation | module |
| --------- | ------ |
| `PATCH /users/` | `update_users_users_patch` |
| `POST /users/` | `create_user_users_post` |
| `DELETE /users/apikeys/{key_id}` | `revoke_api_key_users_apikeys_key_id_delete` |
| `PUT /users/apikeys/{key_id}` | `update_api_key_users_apikeys_key_id_put` |
| `GET /users/catalog` | `permission_catalog_users_catalog_get` |
| `GET /users/details` | `user_details_users_details_get` |
| `POST /users/groups` | `create_group_users_groups_post` |
| `POST /users/groups/delete` | `delete_groups_users_groups_delete_post` |
| `GET /users/management-view` | `management_view_users_management_view_get` |
| `GET /users/me` | `get_me_users_me_get` |
| `PATCH /users/me` | `update_me_users_me_patch` |
| `GET /users/me/apikeys` | `list_my_api_keys_users_me_apikeys_get` |
| `GET /users/me/preferences` | `get_preferences_users_me_preferences_get` |
| `DELETE /users/me/preferences/{key}` | `reset_preference_users_me_preferences_key_delete` |
| `GET /users/me/preferences/{key}` | `get_preference_users_me_preferences_key_get` |
| `PUT /users/me/preferences/{key}` | `set_preference_users_me_preferences_key_put` |
| `POST /users/permissions` | `add_permission_users_permissions_post` |
| `POST /users/permissions/delete` | `delete_permission_users_permissions_delete_post` |
| `GET /users/{user_id}/apikeys` | `list_user_api_keys_users_user_id_apikeys_get` |
| `POST /users/{user_id}/apikeys` | `create_api_key_users_user_id_apikeys_post` |

</details>

### Endpoints that do not return JSON

Four operations serve something other than `application/json`. They still return
their payload through `.parsed`, but with a caveat on two of them:

| operation | `.parsed` holds | annotated as |
| --------- | --------------- | ------------ |
| `GET /alerts/{alert_uuid}/logs` | the log text | `str` |
| `GET /events/export` | the CSV/JSON export text | `str` |
| `GET /alerts/{alert_uuid}/download` | the zip, as **`bytes`** | `str` |
| `GET /crashes/{crash_id}/download` | the zip, as **`bytes`** | `str` |

The two zip downloads really do hand back `bytes` at runtime — the `str`
annotation is an artifact of the schema declaring the body as a string with a
`contentMediaType`, and the generator honouring that literally. Write the result
straight to a file in binary mode:

```python
from pathlib import Path

from aceapi_v2_client.api.alerts import download_alert_alerts_alert_uuid_download_get

response = download_alert_alerts_alert_uuid_download_get.sync_detailed(
    alert_uuid="...", client=client
)
# .parsed and .content hold the same bytes; .content is the honestly-typed one
Path("alert.zip").write_bytes(response.content)
```

Both archives are **zip-encrypted with the password `infected`** — they contain
the file observables the alert or crash was built from.

## Base URL and TLS notes

- **The base URL must include the `/api/v2` prefix.** The generated client
  appends operation paths (e.g. `/common/ping`) directly to `base_url`.
  - From inside the docker compose network: `https://ace-http/api/v2`
  - From the docker host: `https://localhost:8443/api/v2`
- Development instances serve a **self-signed certificate**. Pass
  `verify_ssl=False` (as above) or point `verify_ssl` at a CA bundle path for
  production.

## Keeping the client up to date

The generated code is committed to this repository. When the ACE API v2 changes,
regenerate it from the live schema:

```bash
# against the default instance (https://ace-http/api/v2/openapi.json)
scripts/regenerate.sh

# or against a specific instance
scripts/regenerate.sh https://localhost:8443/api/v2/openapi.json
```

The script:

1. fetches the latest `openapi.json` into this directory (the build-time source
   of truth),
2. installs `openapi-python-client` into a throwaway virtualenv (so it never
   touches your main environment),
3. regenerates the package, preserving the hand-maintained files
   (`aceapi_v2_client/auth.py` and `aceapi_v2_client/py.typed`).

After running it:

1. **Check coverage**: `pytest tests/test_coverage.py` — this fails loudly if any
   endpoint in the new schema has no generated module. It runs offline.
2. **Review the diff**: `git diff aceapi_v2_client/`
3. **Bump the version** if the API changed — update `version` in
   `pyproject.toml` and `package_version_override` in
   `openapi-python-client-config.yaml`. The client version mirrors the API's
   major version (`2.x.y`); bump the patch/minor for client-only changes.
4. **Rebuild and verify** (below).

> Only `auth.py` and `py.typed` are hand-maintained. Do not add other custom
> code inside `aceapi_v2_client/` — it would be overwritten on regeneration.

### Watch the generator's warnings

The generator understands `application/json`, `application/octet-stream` and
`text/*` response bodies. Anything else makes it print a
`Cannot parse response ... Unsupported content_type` warning and **silently drop
that success response from the generated code** — `sync()` then returns `None` on
a perfectly good 200, and a client built with `raise_on_unexpected_status=True`
raises on it.

`openapi-python-client-config.yaml` already maps the API's `application/zip`
downloads onto `application/octet-stream` to avoid exactly that. If a
regeneration prints a new warning of this kind, add the content type to
`content_type_overrides` rather than shipping an endpoint that returns nothing.

> The regeneration script needs `python3 -m venv` to work. On Debian/Ubuntu,
> where `ensurepip` lives in a separate `python3-venv` package, it falls back to
> bootstrapping pip with `get-pip.py` — that path needs outbound network access
> to `bootstrap.pypa.io`.

## Building and publishing to PyPI

```bash
pip install -r requirements-dev.txt
python -m build              # produces dist/*.whl and dist/*.tar.gz
twine check dist/*           # validate metadata for PyPI
twine upload dist/*          # publish (requires PyPI credentials)
```

## Running the tests

`tests/test_coverage.py` runs offline — it checks the committed package against
the committed schema and needs nothing but the package's own dependencies:

```bash
pytest tests/test_coverage.py -v
```

`tests/test_smoke.py` only runs when pointed at a live instance, and is skipped
otherwise. It exercises one endpoint from each major group, including a
create/read/update/delete round trip against `/saved-filters/` that cleans up
after itself:

```bash
ACE_API_BASE_URL=https://ace-http/api/v2 \
ACE_API_KEY=YOUR-API-KEY \
ACE_API_VERIFY_SSL=false \
pytest tests/test_smoke.py -v
```

Point it at a key with an **inherit** scope: the `/users/me` and saved-filter
tests are self-service routes, which a narrowly scoped key cannot reach (see
[API keys are scoped](#api-keys-are-scoped)).

## License

Apache-2.0. See [LICENSE](LICENSE).
