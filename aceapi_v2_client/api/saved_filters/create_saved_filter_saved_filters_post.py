from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.saved_filter_create import SavedFilterCreate
from ...models.saved_filter_read import SavedFilterRead
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SavedFilterCreate,
    screen: str | Unset = "alerts",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["screen"] = screen

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/saved-filters/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SavedFilterRead | None:
    if response.status_code == 201:
        response_201 = SavedFilterRead.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | SavedFilterRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SavedFilterCreate,
    screen: str | Unset = "alerts",
) -> Response[HTTPValidationError | SavedFilterRead]:
    """Create Saved Filter

    Args:
        screen (str | Unset): the screen the saved filters belong to Default: 'alerts'.
        body (SavedFilterCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SavedFilterRead]
    """

    kwargs = _get_kwargs(
        body=body,
        screen=screen,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SavedFilterCreate,
    screen: str | Unset = "alerts",
) -> HTTPValidationError | SavedFilterRead | None:
    """Create Saved Filter

    Args:
        screen (str | Unset): the screen the saved filters belong to Default: 'alerts'.
        body (SavedFilterCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SavedFilterRead
    """

    return sync_detailed(
        client=client,
        body=body,
        screen=screen,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SavedFilterCreate,
    screen: str | Unset = "alerts",
) -> Response[HTTPValidationError | SavedFilterRead]:
    """Create Saved Filter

    Args:
        screen (str | Unset): the screen the saved filters belong to Default: 'alerts'.
        body (SavedFilterCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SavedFilterRead]
    """

    kwargs = _get_kwargs(
        body=body,
        screen=screen,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SavedFilterCreate,
    screen: str | Unset = "alerts",
) -> HTTPValidationError | SavedFilterRead | None:
    """Create Saved Filter

    Args:
        screen (str | Unset): the screen the saved filters belong to Default: 'alerts'.
        body (SavedFilterCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SavedFilterRead
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            screen=screen,
        )
    ).parsed
