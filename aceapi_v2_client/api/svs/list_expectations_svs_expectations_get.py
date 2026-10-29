import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.expectation_page import ExpectationPage
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    test: None | str | Unset = UNSET,
    platform: None | str | Unset = UNSET,
    signature: None | str | Unset = UNSET,
    state: None | str | Unset = UNSET,
    changed_since: datetime.datetime | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_test: None | str | Unset
    if isinstance(test, Unset):
        json_test = UNSET
    else:
        json_test = test
    params["test"] = json_test

    json_platform: None | str | Unset
    if isinstance(platform, Unset):
        json_platform = UNSET
    else:
        json_platform = platform
    params["platform"] = json_platform

    json_signature: None | str | Unset
    if isinstance(signature, Unset):
        json_signature = UNSET
    else:
        json_signature = signature
    params["signature"] = json_signature

    json_state: None | str | Unset
    if isinstance(state, Unset):
        json_state = UNSET
    else:
        json_state = state
    params["state"] = json_state

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
        "url": "/svs/expectations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExpectationPage | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ExpectationPage.from_dict(response.json())

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
) -> Response[ExpectationPage | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    test: None | str | Unset = UNSET,
    platform: None | str | Unset = UNSET,
    signature: None | str | Unset = UNSET,
    state: None | str | Unset = UNSET,
    changed_since: datetime.datetime | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[ExpectationPage | HTTPValidationError]:
    """List Expectations

     Every test's decided signatures, per platform. Follow next_cursor, with the same filters, until it
    is null.

    Args:
        test (None | str | Unset): only this test's (its guid)
        platform (None | str | Unset): only those about this platform (windows, linux, macos, ...)
        signature (None | str | Unset): only this signature's (its uuid)
        state (None | str | Unset): only expected or only rejected
        changed_since (datetime.datetime | None | Unset): only decisions made or changed at or
            after this time (UTC if no offset is given); the rows then come in (updated_at, id) order
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExpectationPage | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        test=test,
        platform=platform,
        signature=signature,
        state=state,
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
    test: None | str | Unset = UNSET,
    platform: None | str | Unset = UNSET,
    signature: None | str | Unset = UNSET,
    state: None | str | Unset = UNSET,
    changed_since: datetime.datetime | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> ExpectationPage | HTTPValidationError | None:
    """List Expectations

     Every test's decided signatures, per platform. Follow next_cursor, with the same filters, until it
    is null.

    Args:
        test (None | str | Unset): only this test's (its guid)
        platform (None | str | Unset): only those about this platform (windows, linux, macos, ...)
        signature (None | str | Unset): only this signature's (its uuid)
        state (None | str | Unset): only expected or only rejected
        changed_since (datetime.datetime | None | Unset): only decisions made or changed at or
            after this time (UTC if no offset is given); the rows then come in (updated_at, id) order
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExpectationPage | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        test=test,
        platform=platform,
        signature=signature,
        state=state,
        changed_since=changed_since,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    test: None | str | Unset = UNSET,
    platform: None | str | Unset = UNSET,
    signature: None | str | Unset = UNSET,
    state: None | str | Unset = UNSET,
    changed_since: datetime.datetime | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[ExpectationPage | HTTPValidationError]:
    """List Expectations

     Every test's decided signatures, per platform. Follow next_cursor, with the same filters, until it
    is null.

    Args:
        test (None | str | Unset): only this test's (its guid)
        platform (None | str | Unset): only those about this platform (windows, linux, macos, ...)
        signature (None | str | Unset): only this signature's (its uuid)
        state (None | str | Unset): only expected or only rejected
        changed_since (datetime.datetime | None | Unset): only decisions made or changed at or
            after this time (UTC if no offset is given); the rows then come in (updated_at, id) order
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExpectationPage | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        test=test,
        platform=platform,
        signature=signature,
        state=state,
        changed_since=changed_since,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    test: None | str | Unset = UNSET,
    platform: None | str | Unset = UNSET,
    signature: None | str | Unset = UNSET,
    state: None | str | Unset = UNSET,
    changed_since: datetime.datetime | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> ExpectationPage | HTTPValidationError | None:
    """List Expectations

     Every test's decided signatures, per platform. Follow next_cursor, with the same filters, until it
    is null.

    Args:
        test (None | str | Unset): only this test's (its guid)
        platform (None | str | Unset): only those about this platform (windows, linux, macos, ...)
        signature (None | str | Unset): only this signature's (its uuid)
        state (None | str | Unset): only expected or only rejected
        changed_since (datetime.datetime | None | Unset): only decisions made or changed at or
            after this time (UTC if no offset is given); the rows then come in (updated_at, id) order
        cursor (None | str | Unset): the next_cursor of the previous page
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExpectationPage | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            test=test,
            platform=platform,
            signature=signature,
            state=state,
            changed_since=changed_since,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
