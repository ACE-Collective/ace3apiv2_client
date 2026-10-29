from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.decoded_filters import DecodedFilters
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    screen: str,
    *,
    f: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_f: list[str] | Unset = UNSET
    if not isinstance(f, Unset):
        json_f = f

    params["f"] = json_f

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/filter-screens/{screen}/decode".format(
            screen=quote(str(screen), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DecodedFilters | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DecodedFilters.from_dict(response.json())

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
) -> Response[DecodedFilters | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    screen: str,
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
) -> Response[DecodedFilters | HTTPValidationError]:
    """Decode Filters

     The filter list a share link names. A filter that no longer exists is skipped and
    reported in warnings, so an old link still opens; a malformed one is a 422.

    Args:
        screen (str):
        f (list[str] | Unset): the f= values of a share link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DecodedFilters | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        screen=screen,
        f=f,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    screen: str,
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
) -> DecodedFilters | HTTPValidationError | None:
    """Decode Filters

     The filter list a share link names. A filter that no longer exists is skipped and
    reported in warnings, so an old link still opens; a malformed one is a 422.

    Args:
        screen (str):
        f (list[str] | Unset): the f= values of a share link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DecodedFilters | HTTPValidationError
    """

    return sync_detailed(
        screen=screen,
        client=client,
        f=f,
    ).parsed


async def asyncio_detailed(
    screen: str,
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
) -> Response[DecodedFilters | HTTPValidationError]:
    """Decode Filters

     The filter list a share link names. A filter that no longer exists is skipped and
    reported in warnings, so an old link still opens; a malformed one is a 422.

    Args:
        screen (str):
        f (list[str] | Unset): the f= values of a share link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DecodedFilters | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        screen=screen,
        f=f,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    screen: str,
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
) -> DecodedFilters | HTTPValidationError | None:
    """Decode Filters

     The filter list a share link names. A filter that no longer exists is skipped and
    reported in warnings, so an old link still opens; a malformed one is a 422.

    Args:
        screen (str):
        f (list[str] | Unset): the f= values of a share link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DecodedFilters | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            screen=screen,
            client=client,
            f=f,
        )
    ).parsed
