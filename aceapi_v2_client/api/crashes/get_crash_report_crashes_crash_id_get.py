from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.crash_report_detail import CrashReportDetail
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    crash_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/crashes/{crash_id}".format(
            crash_id=quote(str(crash_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CrashReportDetail | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CrashReportDetail.from_dict(response.json())

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
) -> Response[CrashReportDetail | HTTPValidationError]:
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
) -> Response[CrashReportDetail | HTTPValidationError]:
    """Get Crash Report

     Everything recorded about one crash, including an inventory of the report's files.

    A report with ``complete: false`` is one whose worker was killed while it was writing its
    own crash report. What made it to disk is still returned.

    Args:
        crash_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CrashReportDetail | HTTPValidationError]
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
) -> CrashReportDetail | HTTPValidationError | None:
    """Get Crash Report

     Everything recorded about one crash, including an inventory of the report's files.

    A report with ``complete: false`` is one whose worker was killed while it was writing its
    own crash report. What made it to disk is still returned.

    Args:
        crash_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CrashReportDetail | HTTPValidationError
    """

    return sync_detailed(
        crash_id=crash_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    crash_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CrashReportDetail | HTTPValidationError]:
    """Get Crash Report

     Everything recorded about one crash, including an inventory of the report's files.

    A report with ``complete: false`` is one whose worker was killed while it was writing its
    own crash report. What made it to disk is still returned.

    Args:
        crash_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CrashReportDetail | HTTPValidationError]
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
) -> CrashReportDetail | HTTPValidationError | None:
    """Get Crash Report

     Everything recorded about one crash, including an inventory of the report's files.

    A report with ``complete: false`` is one whose worker was killed while it was writing its
    own crash report. What made it to disk is still returned.

    Args:
        crash_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CrashReportDetail | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            crash_id=crash_id,
            client=client,
        )
    ).parsed
