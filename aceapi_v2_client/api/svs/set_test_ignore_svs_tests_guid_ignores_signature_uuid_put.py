from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.ignore import Ignore
from ...models.ignore_request import IgnoreRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    guid: str,
    signature_uuid: str,
    *,
    body: IgnoreRequest,
    if_match: None | str | Unset = UNSET,
    if_none_match: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["if-match"] = if_match

    if not isinstance(if_none_match, Unset):
        headers["if-none-match"] = if_none_match

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/svs/tests/{guid}/ignores/{signature_uuid}".format(
            guid=quote(str(guid), safe=""),
            signature_uuid=quote(str(signature_uuid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Ignore | None:
    if response.status_code == 200:
        response_200 = Ignore.from_dict(response.json())

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
) -> Response[HTTPValidationError | Ignore]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    guid: str,
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
    body: IgnoreRequest,
    if_match: None | str | Unset = UNSET,
    if_none_match: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | Ignore]:
    """Set Test Ignore

     Ignore a signature during the test's runs; setting it again replaces its reason. 412 when an If-
    Match or If-None-Match precondition no longer holds (docs/SVS_API.md, *Conflicting writes*).

    Args:
        guid (str):
        signature_uuid (str):
        if_match (None | str | Unset): the row's updated_at as last read: the write applies only
            while the row is unchanged since
        if_none_match (None | str | Unset): *: the write applies only while there is no row yet
        body (IgnoreRequest): An ignore, as svs:run_manage (a test's) or svs:admin (global) sets
            it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Ignore]
    """

    kwargs = _get_kwargs(
        guid=guid,
        signature_uuid=signature_uuid,
        body=body,
        if_match=if_match,
        if_none_match=if_none_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    guid: str,
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
    body: IgnoreRequest,
    if_match: None | str | Unset = UNSET,
    if_none_match: None | str | Unset = UNSET,
) -> HTTPValidationError | Ignore | None:
    """Set Test Ignore

     Ignore a signature during the test's runs; setting it again replaces its reason. 412 when an If-
    Match or If-None-Match precondition no longer holds (docs/SVS_API.md, *Conflicting writes*).

    Args:
        guid (str):
        signature_uuid (str):
        if_match (None | str | Unset): the row's updated_at as last read: the write applies only
            while the row is unchanged since
        if_none_match (None | str | Unset): *: the write applies only while there is no row yet
        body (IgnoreRequest): An ignore, as svs:run_manage (a test's) or svs:admin (global) sets
            it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Ignore
    """

    return sync_detailed(
        guid=guid,
        signature_uuid=signature_uuid,
        client=client,
        body=body,
        if_match=if_match,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    guid: str,
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
    body: IgnoreRequest,
    if_match: None | str | Unset = UNSET,
    if_none_match: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | Ignore]:
    """Set Test Ignore

     Ignore a signature during the test's runs; setting it again replaces its reason. 412 when an If-
    Match or If-None-Match precondition no longer holds (docs/SVS_API.md, *Conflicting writes*).

    Args:
        guid (str):
        signature_uuid (str):
        if_match (None | str | Unset): the row's updated_at as last read: the write applies only
            while the row is unchanged since
        if_none_match (None | str | Unset): *: the write applies only while there is no row yet
        body (IgnoreRequest): An ignore, as svs:run_manage (a test's) or svs:admin (global) sets
            it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Ignore]
    """

    kwargs = _get_kwargs(
        guid=guid,
        signature_uuid=signature_uuid,
        body=body,
        if_match=if_match,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    guid: str,
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
    body: IgnoreRequest,
    if_match: None | str | Unset = UNSET,
    if_none_match: None | str | Unset = UNSET,
) -> HTTPValidationError | Ignore | None:
    """Set Test Ignore

     Ignore a signature during the test's runs; setting it again replaces its reason. 412 when an If-
    Match or If-None-Match precondition no longer holds (docs/SVS_API.md, *Conflicting writes*).

    Args:
        guid (str):
        signature_uuid (str):
        if_match (None | str | Unset): the row's updated_at as last read: the write applies only
            while the row is unchanged since
        if_none_match (None | str | Unset): *: the write applies only while there is no row yet
        body (IgnoreRequest): An ignore, as svs:run_manage (a test's) or svs:admin (global) sets
            it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Ignore
    """

    return (
        await asyncio_detailed(
            guid=guid,
            signature_uuid=signature_uuid,
            client=client,
            body=body,
            if_match=if_match,
            if_none_match=if_none_match,
        )
    ).parsed
