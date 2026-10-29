from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attribution_page import AttributionPage
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    run_id: str,
    *,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
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
        "url": "/svs/runs/{run_id}/attributions".format(
            run_id=quote(str(run_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AttributionPage | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AttributionPage.from_dict(response.json())

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
) -> Response[AttributionPage | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[AttributionPage | HTTPValidationError]:
    """List Run Attributions

     The run's attributions, one row per (alert, detection), removed ones included.

    Args:
        run_id (str):
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributionPage | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    *,
    client: AuthenticatedClient,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> AttributionPage | HTTPValidationError | None:
    """List Run Attributions

     The run's attributions, one row per (alert, detection), removed ones included.

    Args:
        run_id (str):
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributionPage | HTTPValidationError
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[AttributionPage | HTTPValidationError]:
    """List Run Attributions

     The run's attributions, one row per (alert, detection), removed ones included.

    Args:
        run_id (str):
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributionPage | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    *,
    client: AuthenticatedClient,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> AttributionPage | HTTPValidationError | None:
    """List Run Attributions

     The run's attributions, one row per (alert, detection), removed ones included.

    Args:
        run_id (str):
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributionPage | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
