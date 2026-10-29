from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.encoded_filters import EncodedFilters
from ...models.filter_list import FilterList
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    screen: str,
    *,
    body: FilterList,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/filter-screens/{screen}/encode".format(
            screen=quote(str(screen), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EncodedFilters | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EncodedFilters.from_dict(response.json())

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
) -> Response[EncodedFilters | HTTPValidationError]:
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
    body: FilterList,
) -> Response[EncodedFilters | HTTPValidationError]:
    """Encode Filters

     The share-link form of a filter list. The filters are validated for the screen first, so
    a link is never made from a filter the screen would refuse.

    Args:
        screen (str):
        body (FilterList):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EncodedFilters | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        screen=screen,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    screen: str,
    *,
    client: AuthenticatedClient,
    body: FilterList,
) -> EncodedFilters | HTTPValidationError | None:
    """Encode Filters

     The share-link form of a filter list. The filters are validated for the screen first, so
    a link is never made from a filter the screen would refuse.

    Args:
        screen (str):
        body (FilterList):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EncodedFilters | HTTPValidationError
    """

    return sync_detailed(
        screen=screen,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    screen: str,
    *,
    client: AuthenticatedClient,
    body: FilterList,
) -> Response[EncodedFilters | HTTPValidationError]:
    """Encode Filters

     The share-link form of a filter list. The filters are validated for the screen first, so
    a link is never made from a filter the screen would refuse.

    Args:
        screen (str):
        body (FilterList):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EncodedFilters | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        screen=screen,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    screen: str,
    *,
    client: AuthenticatedClient,
    body: FilterList,
) -> EncodedFilters | HTTPValidationError | None:
    """Encode Filters

     The share-link form of a filter list. The filters are validated for the screen first, so
    a link is never made from a filter the screen would refuse.

    Args:
        screen (str):
        body (FilterList):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EncodedFilters | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            screen=screen,
            client=client,
            body=body,
        )
    ).parsed
