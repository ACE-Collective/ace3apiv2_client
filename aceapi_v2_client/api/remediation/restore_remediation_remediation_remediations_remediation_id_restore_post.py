from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.remediation_summary import RemediationSummary
from ...types import Response


def _get_kwargs(
    remediation_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/remediation/remediations/{remediation_id}/restore".format(
            remediation_id=quote(str(remediation_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | RemediationSummary | None:
    if response.status_code == 201:
        response_201 = RemediationSummary.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | RemediationSummary]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    remediation_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | RemediationSummary]:
    """Restore Remediation

     Queues a restore of what a successful removal removed, with the restore key that removal
    produced, and returns the restore. Anything but a removal that succeeded is a 409.

    Args:
        remediation_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RemediationSummary]
    """

    kwargs = _get_kwargs(
        remediation_id=remediation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    remediation_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | RemediationSummary | None:
    """Restore Remediation

     Queues a restore of what a successful removal removed, with the restore key that removal
    produced, and returns the restore. Anything but a removal that succeeded is a 409.

    Args:
        remediation_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RemediationSummary
    """

    return sync_detailed(
        remediation_id=remediation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    remediation_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | RemediationSummary]:
    """Restore Remediation

     Queues a restore of what a successful removal removed, with the restore key that removal
    produced, and returns the restore. Anything but a removal that succeeded is a 409.

    Args:
        remediation_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RemediationSummary]
    """

    kwargs = _get_kwargs(
        remediation_id=remediation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    remediation_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | RemediationSummary | None:
    """Restore Remediation

     Queues a restore of what a successful removal removed, with the restore key that removal
    produced, and returns the restore. Anything but a removal that succeeded is a 409.

    Args:
        remediation_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RemediationSummary
    """

    return (
        await asyncio_detailed(
            remediation_id=remediation_id,
            client=client,
        )
    ).parsed
