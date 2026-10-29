import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.ignore_page import IgnorePage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    scope: None | str | Unset = UNSET,
    test: None | str | Unset = UNSET,
    signature: None | str | Unset = UNSET,
    changed_since: datetime.datetime | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_scope: None | str | Unset
    if isinstance(scope, Unset):
        json_scope = UNSET
    else:
        json_scope = scope
    params["scope"] = json_scope

    json_test: None | str | Unset
    if isinstance(test, Unset):
        json_test = UNSET
    else:
        json_test = test
    params["test"] = json_test

    json_signature: None | str | Unset
    if isinstance(signature, Unset):
        json_signature = UNSET
    else:
        json_signature = signature
    params["signature"] = json_signature

    json_changed_since: None | str | Unset
    if isinstance(changed_since, Unset):
        json_changed_since = UNSET
    elif isinstance(changed_since, datetime.datetime):
        json_changed_since = changed_since.isoformat()
    else:
        json_changed_since = changed_since
    params["changed_since"] = json_changed_since

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
        "url": "/svs/ignores/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | IgnorePage | None:
    if response.status_code == 200:
        response_200 = IgnorePage.from_dict(response.json())

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
) -> Response[HTTPValidationError | IgnorePage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    scope: None | str | Unset = UNSET,
    test: None | str | Unset = UNSET,
    signature: None | str | Unset = UNSET,
    changed_since: datetime.datetime | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[HTTPValidationError | IgnorePage]:
    """List Ignores

     The ignores. Follow next_cursor, with the same filters, until it is null.

    Args:
        scope (None | str | Unset): only global or only test ignores
        test (None | str | Unset): the ignores that apply to this test (its guid): its own and the
            global ones
        signature (None | str | Unset): only this signature's (its uuid)
        changed_since (datetime.datetime | None | Unset): only ignores added or changed at or
            after this time (UTC if no offset is given); the rows then come in (updated_at, id) order.
            A removed ignore is gone, not listed
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | IgnorePage]
    """

    kwargs = _get_kwargs(
        scope=scope,
        test=test,
        signature=signature,
        changed_since=changed_since,
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
    scope: None | str | Unset = UNSET,
    test: None | str | Unset = UNSET,
    signature: None | str | Unset = UNSET,
    changed_since: datetime.datetime | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> HTTPValidationError | IgnorePage | None:
    """List Ignores

     The ignores. Follow next_cursor, with the same filters, until it is null.

    Args:
        scope (None | str | Unset): only global or only test ignores
        test (None | str | Unset): the ignores that apply to this test (its guid): its own and the
            global ones
        signature (None | str | Unset): only this signature's (its uuid)
        changed_since (datetime.datetime | None | Unset): only ignores added or changed at or
            after this time (UTC if no offset is given); the rows then come in (updated_at, id) order.
            A removed ignore is gone, not listed
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | IgnorePage
    """

    return sync_detailed(
        client=client,
        scope=scope,
        test=test,
        signature=signature,
        changed_since=changed_since,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    scope: None | str | Unset = UNSET,
    test: None | str | Unset = UNSET,
    signature: None | str | Unset = UNSET,
    changed_since: datetime.datetime | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[HTTPValidationError | IgnorePage]:
    """List Ignores

     The ignores. Follow next_cursor, with the same filters, until it is null.

    Args:
        scope (None | str | Unset): only global or only test ignores
        test (None | str | Unset): the ignores that apply to this test (its guid): its own and the
            global ones
        signature (None | str | Unset): only this signature's (its uuid)
        changed_since (datetime.datetime | None | Unset): only ignores added or changed at or
            after this time (UTC if no offset is given); the rows then come in (updated_at, id) order.
            A removed ignore is gone, not listed
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | IgnorePage]
    """

    kwargs = _get_kwargs(
        scope=scope,
        test=test,
        signature=signature,
        changed_since=changed_since,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    scope: None | str | Unset = UNSET,
    test: None | str | Unset = UNSET,
    signature: None | str | Unset = UNSET,
    changed_since: datetime.datetime | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> HTTPValidationError | IgnorePage | None:
    """List Ignores

     The ignores. Follow next_cursor, with the same filters, until it is null.

    Args:
        scope (None | str | Unset): only global or only test ignores
        test (None | str | Unset): the ignores that apply to this test (its guid): its own and the
            global ones
        signature (None | str | Unset): only this signature's (its uuid)
        changed_since (datetime.datetime | None | Unset): only ignores added or changed at or
            after this time (UTC if no offset is given); the rows then come in (updated_at, id) order.
            A removed ignore is gone, not listed
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | IgnorePage
    """

    return (
        await asyncio_detailed(
            client=client,
            scope=scope,
            test=test,
            signature=signature,
            changed_since=changed_since,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
