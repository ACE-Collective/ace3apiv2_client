from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.reason_request import ReasonRequest
from ...models.sample_deletion import SampleDeletion
from ...types import Response


def _get_kwargs(
    sha256: str,
    *,
    body: ReasonRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/svs/samples/{sha256}".format(
            sha256=quote(str(sha256), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SampleDeletion | None:
    if response.status_code == 200:
        response_200 = SampleDeletion.from_dict(response.json())

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
) -> Response[HTTPValidationError | SampleDeletion]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sha256: str,
    *,
    client: AuthenticatedClient,
    body: ReasonRequest,
) -> Response[HTTPValidationError | SampleDeletion]:
    """Delete Sample

     Delete the file from SVS, for every rule: its captures and retirements are removed, its
    bytes purged from the pool, and an audit row is kept (GET /svs/samples/deletions) that also
    keeps the file from being captured again. Not reached: the alerts' own files and the YARA QA
    store.

    Deleting a deleted sample retries an unfinished purge. 409 wrong_node when the bytes are on
    another node's local pool, 409 legal_hold when the file is under legal hold.

    Args:
        sha256 (str):
        body (ReasonRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SampleDeletion]
    """

    kwargs = _get_kwargs(
        sha256=sha256,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sha256: str,
    *,
    client: AuthenticatedClient,
    body: ReasonRequest,
) -> HTTPValidationError | SampleDeletion | None:
    """Delete Sample

     Delete the file from SVS, for every rule: its captures and retirements are removed, its
    bytes purged from the pool, and an audit row is kept (GET /svs/samples/deletions) that also
    keeps the file from being captured again. Not reached: the alerts' own files and the YARA QA
    store.

    Deleting a deleted sample retries an unfinished purge. 409 wrong_node when the bytes are on
    another node's local pool, 409 legal_hold when the file is under legal hold.

    Args:
        sha256 (str):
        body (ReasonRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SampleDeletion
    """

    return sync_detailed(
        sha256=sha256,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    sha256: str,
    *,
    client: AuthenticatedClient,
    body: ReasonRequest,
) -> Response[HTTPValidationError | SampleDeletion]:
    """Delete Sample

     Delete the file from SVS, for every rule: its captures and retirements are removed, its
    bytes purged from the pool, and an audit row is kept (GET /svs/samples/deletions) that also
    keeps the file from being captured again. Not reached: the alerts' own files and the YARA QA
    store.

    Deleting a deleted sample retries an unfinished purge. 409 wrong_node when the bytes are on
    another node's local pool, 409 legal_hold when the file is under legal hold.

    Args:
        sha256 (str):
        body (ReasonRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SampleDeletion]
    """

    kwargs = _get_kwargs(
        sha256=sha256,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sha256: str,
    *,
    client: AuthenticatedClient,
    body: ReasonRequest,
) -> HTTPValidationError | SampleDeletion | None:
    """Delete Sample

     Delete the file from SVS, for every rule: its captures and retirements are removed, its
    bytes purged from the pool, and an audit row is kept (GET /svs/samples/deletions) that also
    keeps the file from being captured again. Not reached: the alerts' own files and the YARA QA
    store.

    Deleting a deleted sample retries an unfinished purge. 409 wrong_node when the bytes are on
    another node's local pool, 409 legal_hold when the file is under legal hold.

    Args:
        sha256 (str):
        body (ReasonRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SampleDeletion
    """

    return (
        await asyncio_detailed(
            sha256=sha256,
            client=client,
            body=body,
        )
    ).parsed
