from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_meta import AlertMeta
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    alert_uuid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/alerts/{alert_uuid}/meta".format(
            alert_uuid=quote(str(alert_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertMeta | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AlertMeta.from_dict(response.json())

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
) -> Response[AlertMeta | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[AlertMeta | HTTPValidationError]:
    """Get Alert Meta

     The alert's ownership, disposition, lock and version, which the alert page polls for
    while it is open. Read from the database alone, without loading the alert.

    Args:
        alert_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertMeta | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        alert_uuid=alert_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
) -> AlertMeta | HTTPValidationError | None:
    """Get Alert Meta

     The alert's ownership, disposition, lock and version, which the alert page polls for
    while it is open. Read from the database alone, without loading the alert.

    Args:
        alert_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertMeta | HTTPValidationError
    """

    return sync_detailed(
        alert_uuid=alert_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[AlertMeta | HTTPValidationError]:
    """Get Alert Meta

     The alert's ownership, disposition, lock and version, which the alert page polls for
    while it is open. Read from the database alone, without loading the alert.

    Args:
        alert_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertMeta | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        alert_uuid=alert_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
) -> AlertMeta | HTTPValidationError | None:
    """Get Alert Meta

     The alert's ownership, disposition, lock and version, which the alert page polls for
    while it is open. Read from the database alone, without loading the alert.

    Args:
        alert_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertMeta | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            alert_uuid=alert_uuid,
            client=client,
        )
    ).parsed
