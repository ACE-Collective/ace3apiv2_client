from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_response_saved_filter_read import ListResponseSavedFilterRead
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    screen: str | Unset = "alerts",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["screen"] = screen

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/saved-filters/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ListResponseSavedFilterRead | None:
    if response.status_code == 200:
        response_200 = ListResponseSavedFilterRead.from_dict(response.json())

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
) -> Response[HTTPValidationError | ListResponseSavedFilterRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    screen: str | Unset = "alerts",
) -> Response[HTTPValidationError | ListResponseSavedFilterRead]:
    """List Saved Filters

    Args:
        screen (str | Unset): the screen the saved filters belong to Default: 'alerts'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListResponseSavedFilterRead]
    """

    kwargs = _get_kwargs(
        screen=screen,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    screen: str | Unset = "alerts",
) -> HTTPValidationError | ListResponseSavedFilterRead | None:
    """List Saved Filters

    Args:
        screen (str | Unset): the screen the saved filters belong to Default: 'alerts'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListResponseSavedFilterRead
    """

    return sync_detailed(
        client=client,
        screen=screen,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    screen: str | Unset = "alerts",
) -> Response[HTTPValidationError | ListResponseSavedFilterRead]:
    """List Saved Filters

    Args:
        screen (str | Unset): the screen the saved filters belong to Default: 'alerts'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListResponseSavedFilterRead]
    """

    kwargs = _get_kwargs(
        screen=screen,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    screen: str | Unset = "alerts",
) -> HTTPValidationError | ListResponseSavedFilterRead | None:
    """List Saved Filters

    Args:
        screen (str | Unset): the screen the saved filters belong to Default: 'alerts'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListResponseSavedFilterRead
    """

    return (
        await asyncio_detailed(
            client=client,
            screen=screen,
        )
    ).parsed
