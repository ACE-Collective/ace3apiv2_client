from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cli_execution_list_page import CliExecutionListPage
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cli/executions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CliExecutionListPage | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CliExecutionListPage.from_dict(response.json())

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
) -> Response[CliExecutionListPage | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[CliExecutionListPage | HTTPValidationError]:
    """List Executions

     Every recorded run, newest first, without its output.

    Args:
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CliExecutionListPage | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> CliExecutionListPage | HTTPValidationError | None:
    """List Executions

     Every recorded run, newest first, without its output.

    Args:
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CliExecutionListPage | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[CliExecutionListPage | HTTPValidationError]:
    """List Executions

     Every recorded run, newest first, without its output.

    Args:
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CliExecutionListPage | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> CliExecutionListPage | HTTPValidationError | None:
    """List Executions

     Every recorded run, newest first, without its output.

    Args:
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CliExecutionListPage | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
