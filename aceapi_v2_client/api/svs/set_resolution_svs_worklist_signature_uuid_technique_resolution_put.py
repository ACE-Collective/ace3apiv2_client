from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.resolution_request import ResolutionRequest
from ...models.worklist_row import WorklistRow
from ...types import UNSET, Response, Unset


def _get_kwargs(
    signature_uuid: str,
    technique: str,
    *,
    body: ResolutionRequest,
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
        "url": "/svs/worklist/{signature_uuid}/{technique}/resolution".format(
            signature_uuid=quote(str(signature_uuid), safe=""),
            technique=quote(str(technique), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | WorklistRow | None:
    if response.status_code == 200:
        response_200 = WorklistRow.from_dict(response.json())

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
) -> Response[HTTPValidationError | WorklistRow]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    signature_uuid: str,
    technique: str,
    *,
    client: AuthenticatedClient,
    body: ResolutionRequest,
    if_match: None | str | Unset = UNSET,
    if_none_match: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | WorklistRow]:
    """Set Resolution

     Resolve a tag measurement doesn't confirm: keep it, or remove it (it stops counting toward
    coverage from the next refresh). 404 for an unknown row; 409 for a row that is confirmed,
    informational, retired or removed; 422 for an invalid body or a config key (a resolution records
    who made it); 412 when an If-Match or If-None-Match precondition no longer holds (docs/SVS_API.md,
    *Conflicting writes*).

    Args:
        signature_uuid (str):
        technique (str):
        if_match (None | str | Unset): the row's updated_at as last read: the write applies only
            while the row is unchanged since
        if_none_match (None | str | Unset): *: the write applies only while there is no row yet
        body (ResolutionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WorklistRow]
    """

    kwargs = _get_kwargs(
        signature_uuid=signature_uuid,
        technique=technique,
        body=body,
        if_match=if_match,
        if_none_match=if_none_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    signature_uuid: str,
    technique: str,
    *,
    client: AuthenticatedClient,
    body: ResolutionRequest,
    if_match: None | str | Unset = UNSET,
    if_none_match: None | str | Unset = UNSET,
) -> HTTPValidationError | WorklistRow | None:
    """Set Resolution

     Resolve a tag measurement doesn't confirm: keep it, or remove it (it stops counting toward
    coverage from the next refresh). 404 for an unknown row; 409 for a row that is confirmed,
    informational, retired or removed; 422 for an invalid body or a config key (a resolution records
    who made it); 412 when an If-Match or If-None-Match precondition no longer holds (docs/SVS_API.md,
    *Conflicting writes*).

    Args:
        signature_uuid (str):
        technique (str):
        if_match (None | str | Unset): the row's updated_at as last read: the write applies only
            while the row is unchanged since
        if_none_match (None | str | Unset): *: the write applies only while there is no row yet
        body (ResolutionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WorklistRow
    """

    return sync_detailed(
        signature_uuid=signature_uuid,
        technique=technique,
        client=client,
        body=body,
        if_match=if_match,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    signature_uuid: str,
    technique: str,
    *,
    client: AuthenticatedClient,
    body: ResolutionRequest,
    if_match: None | str | Unset = UNSET,
    if_none_match: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | WorklistRow]:
    """Set Resolution

     Resolve a tag measurement doesn't confirm: keep it, or remove it (it stops counting toward
    coverage from the next refresh). 404 for an unknown row; 409 for a row that is confirmed,
    informational, retired or removed; 422 for an invalid body or a config key (a resolution records
    who made it); 412 when an If-Match or If-None-Match precondition no longer holds (docs/SVS_API.md,
    *Conflicting writes*).

    Args:
        signature_uuid (str):
        technique (str):
        if_match (None | str | Unset): the row's updated_at as last read: the write applies only
            while the row is unchanged since
        if_none_match (None | str | Unset): *: the write applies only while there is no row yet
        body (ResolutionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WorklistRow]
    """

    kwargs = _get_kwargs(
        signature_uuid=signature_uuid,
        technique=technique,
        body=body,
        if_match=if_match,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    signature_uuid: str,
    technique: str,
    *,
    client: AuthenticatedClient,
    body: ResolutionRequest,
    if_match: None | str | Unset = UNSET,
    if_none_match: None | str | Unset = UNSET,
) -> HTTPValidationError | WorklistRow | None:
    """Set Resolution

     Resolve a tag measurement doesn't confirm: keep it, or remove it (it stops counting toward
    coverage from the next refresh). 404 for an unknown row; 409 for a row that is confirmed,
    informational, retired or removed; 422 for an invalid body or a config key (a resolution records
    who made it); 412 when an If-Match or If-None-Match precondition no longer holds (docs/SVS_API.md,
    *Conflicting writes*).

    Args:
        signature_uuid (str):
        technique (str):
        if_match (None | str | Unset): the row's updated_at as last read: the write applies only
            while the row is unchanged since
        if_none_match (None | str | Unset): *: the write applies only while there is no row yet
        body (ResolutionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WorklistRow
    """

    return (
        await asyncio_detailed(
            signature_uuid=signature_uuid,
            technique=technique,
            client=client,
            body=body,
            if_match=if_match,
            if_none_match=if_none_match,
        )
    ).parsed
