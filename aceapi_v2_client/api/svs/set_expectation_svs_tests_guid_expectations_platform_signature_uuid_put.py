from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.expectation import Expectation
from ...models.expectation_request import ExpectationRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    guid: str,
    platform: str,
    signature_uuid: str,
    *,
    body: ExpectationRequest,
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
        "url": "/svs/tests/{guid}/expectations/{platform}/{signature_uuid}".format(
            guid=quote(str(guid), safe=""),
            platform=quote(str(platform), safe=""),
            signature_uuid=quote(str(signature_uuid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Expectation | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = Expectation.from_dict(response.json())

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
) -> Response[Expectation | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    guid: str,
    platform: str,
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
    body: ExpectationRequest,
    if_match: None | str | Unset = UNSET,
    if_none_match: None | str | Unset = UNSET,
) -> Response[Expectation | HTTPValidationError]:
    """Set Expectation

     Decide a signature for the test's runs on the platform: expected or rejected. 404 for an
    unknown test; 422 for a platform the test doesn't support, a run_id that isn't one of the test's
    runs on the platform, or a config key (a decision records who made it); 412 when an If-Match or If-
    None-Match precondition no longer holds (docs/SVS_API.md, *Conflicting writes*).

    Args:
        guid (str):
        platform (str):
        signature_uuid (str):
        if_match (None | str | Unset): the row's updated_at as last read: the write applies only
            while the row is unchanged since
        if_none_match (None | str | Unset): *: the write applies only while there is no row yet
        body (ExpectationRequest): A decision about a signature for a test on a platform, as
            svs:run_manage makes it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Expectation | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        guid=guid,
        platform=platform,
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
    platform: str,
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
    body: ExpectationRequest,
    if_match: None | str | Unset = UNSET,
    if_none_match: None | str | Unset = UNSET,
) -> Expectation | HTTPValidationError | None:
    """Set Expectation

     Decide a signature for the test's runs on the platform: expected or rejected. 404 for an
    unknown test; 422 for a platform the test doesn't support, a run_id that isn't one of the test's
    runs on the platform, or a config key (a decision records who made it); 412 when an If-Match or If-
    None-Match precondition no longer holds (docs/SVS_API.md, *Conflicting writes*).

    Args:
        guid (str):
        platform (str):
        signature_uuid (str):
        if_match (None | str | Unset): the row's updated_at as last read: the write applies only
            while the row is unchanged since
        if_none_match (None | str | Unset): *: the write applies only while there is no row yet
        body (ExpectationRequest): A decision about a signature for a test on a platform, as
            svs:run_manage makes it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Expectation | HTTPValidationError
    """

    return sync_detailed(
        guid=guid,
        platform=platform,
        signature_uuid=signature_uuid,
        client=client,
        body=body,
        if_match=if_match,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    guid: str,
    platform: str,
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
    body: ExpectationRequest,
    if_match: None | str | Unset = UNSET,
    if_none_match: None | str | Unset = UNSET,
) -> Response[Expectation | HTTPValidationError]:
    """Set Expectation

     Decide a signature for the test's runs on the platform: expected or rejected. 404 for an
    unknown test; 422 for a platform the test doesn't support, a run_id that isn't one of the test's
    runs on the platform, or a config key (a decision records who made it); 412 when an If-Match or If-
    None-Match precondition no longer holds (docs/SVS_API.md, *Conflicting writes*).

    Args:
        guid (str):
        platform (str):
        signature_uuid (str):
        if_match (None | str | Unset): the row's updated_at as last read: the write applies only
            while the row is unchanged since
        if_none_match (None | str | Unset): *: the write applies only while there is no row yet
        body (ExpectationRequest): A decision about a signature for a test on a platform, as
            svs:run_manage makes it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Expectation | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        guid=guid,
        platform=platform,
        signature_uuid=signature_uuid,
        body=body,
        if_match=if_match,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    guid: str,
    platform: str,
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
    body: ExpectationRequest,
    if_match: None | str | Unset = UNSET,
    if_none_match: None | str | Unset = UNSET,
) -> Expectation | HTTPValidationError | None:
    """Set Expectation

     Decide a signature for the test's runs on the platform: expected or rejected. 404 for an
    unknown test; 422 for a platform the test doesn't support, a run_id that isn't one of the test's
    runs on the platform, or a config key (a decision records who made it); 412 when an If-Match or If-
    None-Match precondition no longer holds (docs/SVS_API.md, *Conflicting writes*).

    Args:
        guid (str):
        platform (str):
        signature_uuid (str):
        if_match (None | str | Unset): the row's updated_at as last read: the write applies only
            while the row is unchanged since
        if_none_match (None | str | Unset): *: the write applies only while there is no row yet
        body (ExpectationRequest): A decision about a signature for a test on a platform, as
            svs:run_manage makes it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Expectation | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            guid=guid,
            platform=platform,
            signature_uuid=signature_uuid,
            client=client,
            body=body,
            if_match=if_match,
            if_none_match=if_none_match,
        )
    ).parsed
