from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.filter_screen_read import FilterScreenRead
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    screen: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/filter-screens/{screen}".format(
            screen=quote(str(screen), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FilterScreenRead | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FilterScreenRead.from_dict(response.json())

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
) -> Response[FilterScreenRead | HTTPValidationError]:
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
) -> Response[FilterScreenRead | HTTPValidationError]:
    """Get Filter Screen Descriptor

    Args:
        screen (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilterScreenRead | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        screen=screen,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    screen: str,
    *,
    client: AuthenticatedClient,
) -> FilterScreenRead | HTTPValidationError | None:
    """Get Filter Screen Descriptor

    Args:
        screen (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilterScreenRead | HTTPValidationError
    """

    return sync_detailed(
        screen=screen,
        client=client,
    ).parsed


async def asyncio_detailed(
    screen: str,
    *,
    client: AuthenticatedClient,
) -> Response[FilterScreenRead | HTTPValidationError]:
    """Get Filter Screen Descriptor

    Args:
        screen (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilterScreenRead | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        screen=screen,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    screen: str,
    *,
    client: AuthenticatedClient,
) -> FilterScreenRead | HTTPValidationError | None:
    """Get Filter Screen Descriptor

    Args:
        screen (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilterScreenRead | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            screen=screen,
            client=client,
        )
    ).parsed
