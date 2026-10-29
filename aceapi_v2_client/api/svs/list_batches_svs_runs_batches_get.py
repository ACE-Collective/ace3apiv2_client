from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.run_batch_page import RunBatchPage
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
        "url": "/svs/runs/batches",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | RunBatchPage | None:
    if response.status_code == 200:
        response_200 = RunBatchPage.from_dict(response.json())

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
) -> Response[HTTPValidationError | RunBatchPage]:
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
) -> Response[HTTPValidationError | RunBatchPage]:
    """List Batches

     One row per batch_id over the runs the filters match, summing only those runs: their states,
    how many need attention, and their results. The batch with the latest run comes first; runs
    without a batch_id are left out. Follow next_cursor, with the same filters, until it is null.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the runs
            screen's slugs: needs_attention, state, test, test_name, technique (T1059 also finds its
            sub-techniques), target, platform, launcher, batch, created, started, ended, reviewed,
            owner, reviewer, reason, changed_since_review, has_open_alerts, has_missing,
            has_possibly_suppressed, has_candidates, has_late, has_context_only (see docs/SVS_API.md);
            repeat for more. Filters are ANDed, the values of one ORed.
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RunBatchPage]
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
) -> HTTPValidationError | RunBatchPage | None:
    """List Batches

     One row per batch_id over the runs the filters match, summing only those runs: their states,
    how many need attention, and their results. The batch with the latest run comes first; runs
    without a batch_id are left out. Follow next_cursor, with the same filters, until it is null.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the runs
            screen's slugs: needs_attention, state, test, test_name, technique (T1059 also finds its
            sub-techniques), target, platform, launcher, batch, created, started, ended, reviewed,
            owner, reviewer, reason, changed_since_review, has_open_alerts, has_missing,
            has_possibly_suppressed, has_candidates, has_late, has_context_only (see docs/SVS_API.md);
            repeat for more. Filters are ANDed, the values of one ORed.
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RunBatchPage
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
) -> Response[HTTPValidationError | RunBatchPage]:
    """List Batches

     One row per batch_id over the runs the filters match, summing only those runs: their states,
    how many need attention, and their results. The batch with the latest run comes first; runs
    without a batch_id are left out. Follow next_cursor, with the same filters, until it is null.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the runs
            screen's slugs: needs_attention, state, test, test_name, technique (T1059 also finds its
            sub-techniques), target, platform, launcher, batch, created, started, ended, reviewed,
            owner, reviewer, reason, changed_since_review, has_open_alerts, has_missing,
            has_possibly_suppressed, has_candidates, has_late, has_context_only (see docs/SVS_API.md);
            repeat for more. Filters are ANDed, the values of one ORed.
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RunBatchPage]
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
) -> HTTPValidationError | RunBatchPage | None:
    """List Batches

     One row per batch_id over the runs the filters match, summing only those runs: their states,
    how many need attention, and their results. The batch with the latest run comes first; runs
    without a batch_id are left out. Follow next_cursor, with the same filters, until it is null.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the runs
            screen's slugs: needs_attention, state, test, test_name, technique (T1059 also finds its
            sub-techniques), target, platform, launcher, batch, created, started, ended, reviewed,
            owner, reviewer, reason, changed_since_review, has_open_alerts, has_missing,
            has_possibly_suppressed, has_candidates, has_late, has_context_only (see docs/SVS_API.md);
            repeat for more. Filters are ANDed, the values of one ORed.
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RunBatchPage
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
