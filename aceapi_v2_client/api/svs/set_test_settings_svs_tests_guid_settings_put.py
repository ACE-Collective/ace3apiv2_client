from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.test_settings import TestSettings
from ...models.test_settings_request import TestSettingsRequest
from ...types import Response


def _get_kwargs(
    guid: str,
    *,
    body: TestSettingsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/svs/tests/{guid}/settings".format(
            guid=quote(str(guid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TestSettings | None:
    if response.status_code == 200:
        response_200 = TestSettings.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | TestSettings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    guid: str,
    *,
    client: AuthenticatedClient,
    body: TestSettingsRequest,
) -> Response[HTTPValidationError | TestSettings]:
    """Set Test Settings

     Set the settings of the test's runs registered from now on, replacing what was set: the
    observation window (null for the computed one; 422 outside 1 minute to the configured ceiling)
    and holds_host.

    Args:
        guid (str):
        body (TestSettingsRequest): A test's settings, as svs:run_manage sets them.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TestSettings]
    """

    kwargs = _get_kwargs(
        guid=guid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    guid: str,
    *,
    client: AuthenticatedClient,
    body: TestSettingsRequest,
) -> HTTPValidationError | TestSettings | None:
    """Set Test Settings

     Set the settings of the test's runs registered from now on, replacing what was set: the
    observation window (null for the computed one; 422 outside 1 minute to the configured ceiling)
    and holds_host.

    Args:
        guid (str):
        body (TestSettingsRequest): A test's settings, as svs:run_manage sets them.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TestSettings
    """

    return sync_detailed(
        guid=guid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    guid: str,
    *,
    client: AuthenticatedClient,
    body: TestSettingsRequest,
) -> Response[HTTPValidationError | TestSettings]:
    """Set Test Settings

     Set the settings of the test's runs registered from now on, replacing what was set: the
    observation window (null for the computed one; 422 outside 1 minute to the configured ceiling)
    and holds_host.

    Args:
        guid (str):
        body (TestSettingsRequest): A test's settings, as svs:run_manage sets them.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TestSettings]
    """

    kwargs = _get_kwargs(
        guid=guid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    guid: str,
    *,
    client: AuthenticatedClient,
    body: TestSettingsRequest,
) -> HTTPValidationError | TestSettings | None:
    """Set Test Settings

     Set the settings of the test's runs registered from now on, replacing what was set: the
    observation window (null for the computed one; 422 outside 1 minute to the configured ceiling)
    and holds_host.

    Args:
        guid (str):
        body (TestSettingsRequest): A test's settings, as svs:run_manage sets them.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TestSettings
    """

    return (
        await asyncio_detailed(
            guid=guid,
            client=client,
            body=body,
        )
    ).parsed
