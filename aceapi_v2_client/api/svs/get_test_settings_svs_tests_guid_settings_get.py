from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.test_settings import TestSettings
from ...types import Response


def _get_kwargs(
    guid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/svs/tests/{guid}/settings".format(
            guid=quote(str(guid), safe=""),
        ),
    }

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
) -> Response[HTTPValidationError | TestSettings]:
    """Get Test Settings

     The test's settings; 404 when it has none (its runs get the computed window).

    Args:
        guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TestSettings]
    """

    kwargs = _get_kwargs(
        guid=guid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    guid: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | TestSettings | None:
    """Get Test Settings

     The test's settings; 404 when it has none (its runs get the computed window).

    Args:
        guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TestSettings
    """

    return sync_detailed(
        guid=guid,
        client=client,
    ).parsed


async def asyncio_detailed(
    guid: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | TestSettings]:
    """Get Test Settings

     The test's settings; 404 when it has none (its runs get the computed window).

    Args:
        guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TestSettings]
    """

    kwargs = _get_kwargs(
        guid=guid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    guid: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | TestSettings | None:
    """Get Test Settings

     The test's settings; 404 when it has none (its runs get the computed window).

    Args:
        guid (str):

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
        )
    ).parsed
