from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.test_host import TestHost
from ...models.test_host_request import TestHostRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    host_id: int,
    *,
    body: TestHostRequest,
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
        "url": "/svs/test-hosts/{host_id}".format(
            host_id=quote(str(host_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TestHost | None:
    if response.status_code == 200:
        response_200 = TestHost.from_dict(response.json())

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
) -> Response[HTTPValidationError | TestHost]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    host_id: int,
    *,
    client: AuthenticatedClient,
    body: TestHostRequest,
    if_match: None | str | Unset = UNSET,
    if_none_match: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TestHost]:
    """Update Test Host

     Replace a test host's fields. 412 when an If-Match or If-None-Match precondition no longer holds
    (docs/SVS_API.md, *Conflicting writes*).

    Args:
        host_id (int):
        if_match (None | str | Unset): the row's updated_at as last read: the write applies only
            while the row is unchanged since
        if_none_match (None | str | Unset): *: the write applies only while there is no row yet
        body (TestHostRequest): A test host as an svs:admin adds or replaces it. Names are matched
            case-insensitively.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TestHost]
    """

    kwargs = _get_kwargs(
        host_id=host_id,
        body=body,
        if_match=if_match,
        if_none_match=if_none_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    host_id: int,
    *,
    client: AuthenticatedClient,
    body: TestHostRequest,
    if_match: None | str | Unset = UNSET,
    if_none_match: None | str | Unset = UNSET,
) -> HTTPValidationError | TestHost | None:
    """Update Test Host

     Replace a test host's fields. 412 when an If-Match or If-None-Match precondition no longer holds
    (docs/SVS_API.md, *Conflicting writes*).

    Args:
        host_id (int):
        if_match (None | str | Unset): the row's updated_at as last read: the write applies only
            while the row is unchanged since
        if_none_match (None | str | Unset): *: the write applies only while there is no row yet
        body (TestHostRequest): A test host as an svs:admin adds or replaces it. Names are matched
            case-insensitively.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TestHost
    """

    return sync_detailed(
        host_id=host_id,
        client=client,
        body=body,
        if_match=if_match,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    host_id: int,
    *,
    client: AuthenticatedClient,
    body: TestHostRequest,
    if_match: None | str | Unset = UNSET,
    if_none_match: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TestHost]:
    """Update Test Host

     Replace a test host's fields. 412 when an If-Match or If-None-Match precondition no longer holds
    (docs/SVS_API.md, *Conflicting writes*).

    Args:
        host_id (int):
        if_match (None | str | Unset): the row's updated_at as last read: the write applies only
            while the row is unchanged since
        if_none_match (None | str | Unset): *: the write applies only while there is no row yet
        body (TestHostRequest): A test host as an svs:admin adds or replaces it. Names are matched
            case-insensitively.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TestHost]
    """

    kwargs = _get_kwargs(
        host_id=host_id,
        body=body,
        if_match=if_match,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    host_id: int,
    *,
    client: AuthenticatedClient,
    body: TestHostRequest,
    if_match: None | str | Unset = UNSET,
    if_none_match: None | str | Unset = UNSET,
) -> HTTPValidationError | TestHost | None:
    """Update Test Host

     Replace a test host's fields. 412 when an If-Match or If-None-Match precondition no longer holds
    (docs/SVS_API.md, *Conflicting writes*).

    Args:
        host_id (int):
        if_match (None | str | Unset): the row's updated_at as last read: the write applies only
            while the row is unchanged since
        if_none_match (None | str | Unset): *: the write applies only while there is no row yet
        body (TestHostRequest): A test host as an svs:admin adds or replaces it. Names are matched
            case-insensitively.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TestHost
    """

    return (
        await asyncio_detailed(
            host_id=host_id,
            client=client,
            body=body,
            if_match=if_match,
            if_none_match=if_none_match,
        )
    ).parsed
