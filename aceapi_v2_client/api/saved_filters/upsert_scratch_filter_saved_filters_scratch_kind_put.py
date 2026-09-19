from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.saved_filter_read import SavedFilterRead
from ...models.scratch_filter_write import ScratchFilterWrite
from ...types import Response


def _get_kwargs(
    kind: str,
    *,
    body: ScratchFilterWrite,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/saved-filters/scratch/{kind}".format(
            kind=quote(str(kind), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SavedFilterRead | None:
    if response.status_code == 200:
        response_200 = SavedFilterRead.from_dict(response.json())

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
) -> Response[HTTPValidationError | SavedFilterRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    kind: str,
    *,
    client: AuthenticatedClient,
    body: ScratchFilterWrite,
) -> Response[HTTPValidationError | SavedFilterRead]:
    """Upsert Scratch Filter

     Replace the caller's singleton `working` (unsaved edits) or `temp` (active pivot)
    row. This is how ad-hoc filter state persists without going in the session cookie.

    Args:
        kind (str):
        body (ScratchFilterWrite): Replace the caller's singleton `working` or `temp` row.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SavedFilterRead]
    """

    kwargs = _get_kwargs(
        kind=kind,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    kind: str,
    *,
    client: AuthenticatedClient,
    body: ScratchFilterWrite,
) -> HTTPValidationError | SavedFilterRead | None:
    """Upsert Scratch Filter

     Replace the caller's singleton `working` (unsaved edits) or `temp` (active pivot)
    row. This is how ad-hoc filter state persists without going in the session cookie.

    Args:
        kind (str):
        body (ScratchFilterWrite): Replace the caller's singleton `working` or `temp` row.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SavedFilterRead
    """

    return sync_detailed(
        kind=kind,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    kind: str,
    *,
    client: AuthenticatedClient,
    body: ScratchFilterWrite,
) -> Response[HTTPValidationError | SavedFilterRead]:
    """Upsert Scratch Filter

     Replace the caller's singleton `working` (unsaved edits) or `temp` (active pivot)
    row. This is how ad-hoc filter state persists without going in the session cookie.

    Args:
        kind (str):
        body (ScratchFilterWrite): Replace the caller's singleton `working` or `temp` row.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SavedFilterRead]
    """

    kwargs = _get_kwargs(
        kind=kind,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    kind: str,
    *,
    client: AuthenticatedClient,
    body: ScratchFilterWrite,
) -> HTTPValidationError | SavedFilterRead | None:
    """Upsert Scratch Filter

     Replace the caller's singleton `working` (unsaved edits) or `temp` (active pivot)
    row. This is how ad-hoc filter state persists without going in the session cookie.

    Args:
        kind (str):
        body (ScratchFilterWrite): Replace the caller's singleton `working` or `temp` row.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SavedFilterRead
    """

    return (
        await asyncio_detailed(
            kind=kind,
            client=client,
            body=body,
        )
    ).parsed
