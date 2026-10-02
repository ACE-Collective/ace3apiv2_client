from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.qa_match_detail import QAMatchDetail
from ...types import Response


def _get_kwargs(
    match_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/signatures/yara-qa/matches/{match_id}".format(
            match_id=quote(str(match_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | QAMatchDetail | None:
    if response.status_code == 200:
        response_200 = QAMatchDetail.from_dict(response.json())

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
) -> Response[HTTPValidationError | QAMatchDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    match_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | QAMatchDetail]:
    """Get Match

     One stored match, with a summary of the match record (meta, tags, and per string how many
    times it matched and where first).

    Args:
        match_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | QAMatchDetail]
    """

    kwargs = _get_kwargs(
        match_id=match_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    match_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | QAMatchDetail | None:
    """Get Match

     One stored match, with a summary of the match record (meta, tags, and per string how many
    times it matched and where first).

    Args:
        match_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | QAMatchDetail
    """

    return sync_detailed(
        match_id=match_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    match_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | QAMatchDetail]:
    """Get Match

     One stored match, with a summary of the match record (meta, tags, and per string how many
    times it matched and where first).

    Args:
        match_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | QAMatchDetail]
    """

    kwargs = _get_kwargs(
        match_id=match_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    match_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | QAMatchDetail | None:
    """Get Match

     One stored match, with a summary of the match record (meta, tags, and per string how many
    times it matched and where first).

    Args:
        match_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | QAMatchDetail
    """

    return (
        await asyncio_detailed(
            match_id=match_id,
            client=client,
        )
    ).parsed
