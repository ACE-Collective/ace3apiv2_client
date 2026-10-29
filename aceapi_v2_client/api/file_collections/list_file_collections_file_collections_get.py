from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_collection_list_page import FileCollectionListPage
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    f: list[str] | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    tz: str | Unset = "UTC",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_f: list[str] | Unset = UNSET
    if not isinstance(f, Unset):
        json_f = f

    params["f"] = json_f

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    params["limit"] = limit

    params["tz"] = tz

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/file-collections/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FileCollectionListPage | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FileCollectionListPage.from_dict(response.json())

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
) -> Response[FileCollectionListPage | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    tz: str | Unset = "UTC",
) -> Response[FileCollectionListPage | HTTPValidationError]:
    """List File Collections

     List file collection requests, newest first. Follow next_cursor, with the same filters,
    until it is null.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the
            file_collections screen's slugs: alert, collector, created, id, result, status, type,
            value; repeat for more. Filters are ANDed, the values of one ORed.
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileCollectionListPage | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        f=f,
        cursor=cursor,
        limit=limit,
        tz=tz,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    tz: str | Unset = "UTC",
) -> FileCollectionListPage | HTTPValidationError | None:
    """List File Collections

     List file collection requests, newest first. Follow next_cursor, with the same filters,
    until it is null.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the
            file_collections screen's slugs: alert, collector, created, id, result, status, type,
            value; repeat for more. Filters are ANDed, the values of one ORed.
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileCollectionListPage | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        f=f,
        cursor=cursor,
        limit=limit,
        tz=tz,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    tz: str | Unset = "UTC",
) -> Response[FileCollectionListPage | HTTPValidationError]:
    """List File Collections

     List file collection requests, newest first. Follow next_cursor, with the same filters,
    until it is null.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the
            file_collections screen's slugs: alert, collector, created, id, result, status, type,
            value; repeat for more. Filters are ANDed, the values of one ORed.
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileCollectionListPage | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        f=f,
        cursor=cursor,
        limit=limit,
        tz=tz,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    tz: str | Unset = "UTC",
) -> FileCollectionListPage | HTTPValidationError | None:
    """List File Collections

     List file collection requests, newest first. Follow next_cursor, with the same filters,
    until it is null.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the
            file_collections screen's slugs: alert, collector, created, id, result, status, type,
            value; repeat for more. Filters are ANDed, the values of one ORed.
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileCollectionListPage | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            f=f,
            cursor=cursor,
            limit=limit,
            tz=tz,
        )
    ).parsed
