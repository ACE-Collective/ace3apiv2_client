from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_response_file_collection_history_entry import (
    ListResponseFileCollectionHistoryEntry,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: int,
    *,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/file-collections/{collection_id}/history".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ListResponseFileCollectionHistoryEntry | None:
    if response.status_code == 200:
        response_200 = ListResponseFileCollectionHistoryEntry.from_dict(response.json())

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
) -> Response[HTTPValidationError | ListResponseFileCollectionHistoryEntry]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
) -> Response[HTTPValidationError | ListResponseFileCollectionHistoryEntry]:
    """Get File Collection History

     What the file collector recorded of each attempt at a request, newest first.

    Args:
        collection_id (int):
        limit (int | Unset): at most this many of the latest attempts Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListResponseFileCollectionHistoryEntry]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
) -> HTTPValidationError | ListResponseFileCollectionHistoryEntry | None:
    """Get File Collection History

     What the file collector recorded of each attempt at a request, newest first.

    Args:
        collection_id (int):
        limit (int | Unset): at most this many of the latest attempts Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListResponseFileCollectionHistoryEntry
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    collection_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
) -> Response[HTTPValidationError | ListResponseFileCollectionHistoryEntry]:
    """Get File Collection History

     What the file collector recorded of each attempt at a request, newest first.

    Args:
        collection_id (int):
        limit (int | Unset): at most this many of the latest attempts Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListResponseFileCollectionHistoryEntry]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
) -> HTTPValidationError | ListResponseFileCollectionHistoryEntry | None:
    """Get File Collection History

     What the file collector recorded of each attempt at a request, newest first.

    Args:
        collection_id (int):
        limit (int | Unset): at most this many of the latest attempts Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListResponseFileCollectionHistoryEntry
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            limit=limit,
        )
    ).parsed
