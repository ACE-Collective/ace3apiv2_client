from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    crash_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/crashes/{crash_id}/download".format(
            crash_id=quote(str(crash_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.content)
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
) -> Response[HTTPValidationError | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    crash_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | str]:
    """Download Crash Report

     Download the whole crash report as a zip encrypted with password 'infected'.

    Encrypted because the archive contains the file observable the module crashed on.

    Args:
        crash_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
    """

    kwargs = _get_kwargs(
        crash_id=crash_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    crash_id: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | str | None:
    """Download Crash Report

     Download the whole crash report as a zip encrypted with password 'infected'.

    Encrypted because the archive contains the file observable the module crashed on.

    Args:
        crash_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
    """

    return sync_detailed(
        crash_id=crash_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    crash_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | str]:
    """Download Crash Report

     Download the whole crash report as a zip encrypted with password 'infected'.

    Encrypted because the archive contains the file observable the module crashed on.

    Args:
        crash_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
    """

    kwargs = _get_kwargs(
        crash_id=crash_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    crash_id: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | str | None:
    """Download Crash Report

     Download the whole crash report as a zip encrypted with password 'infected'.

    Encrypted because the archive contains the file observable the module crashed on.

    Args:
        crash_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
    """

    return (
        await asyncio_detailed(
            crash_id=crash_id,
            client=client,
        )
    ).parsed
