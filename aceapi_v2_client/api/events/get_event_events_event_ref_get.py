from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_read import EventRead
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    event_ref: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events/{event_ref}".format(
            event_ref=quote(str(event_ref), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EventRead | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EventRead.from_dict(response.json())

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
) -> Response[EventRead | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_ref: str,
    *,
    client: AuthenticatedClient,
) -> Response[EventRead | HTTPValidationError]:
    """Get Event

     Return one event by numeric id or uuid: its metadata, the UUIDs of its alerts
    (``alerts``), each alert's current version token (``alert_versions``, uuid -> version) and
    each alert's database state (``alert_details``: insert_date, owner, owner_time, disposition,
    disposition_time, disposition_user).

    Args:
        event_ref (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventRead | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        event_ref=event_ref,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_ref: str,
    *,
    client: AuthenticatedClient,
) -> EventRead | HTTPValidationError | None:
    """Get Event

     Return one event by numeric id or uuid: its metadata, the UUIDs of its alerts
    (``alerts``), each alert's current version token (``alert_versions``, uuid -> version) and
    each alert's database state (``alert_details``: insert_date, owner, owner_time, disposition,
    disposition_time, disposition_user).

    Args:
        event_ref (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventRead | HTTPValidationError
    """

    return sync_detailed(
        event_ref=event_ref,
        client=client,
    ).parsed


async def asyncio_detailed(
    event_ref: str,
    *,
    client: AuthenticatedClient,
) -> Response[EventRead | HTTPValidationError]:
    """Get Event

     Return one event by numeric id or uuid: its metadata, the UUIDs of its alerts
    (``alerts``), each alert's current version token (``alert_versions``, uuid -> version) and
    each alert's database state (``alert_details``: insert_date, owner, owner_time, disposition,
    disposition_time, disposition_user).

    Args:
        event_ref (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventRead | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        event_ref=event_ref,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_ref: str,
    *,
    client: AuthenticatedClient,
) -> EventRead | HTTPValidationError | None:
    """Get Event

     Return one event by numeric id or uuid: its metadata, the UUIDs of its alerts
    (``alerts``), each alert's current version token (``alert_versions``, uuid -> version) and
    each alert's database state (``alert_details``: insert_date, owner, owner_time, disposition,
    disposition_time, disposition_user).

    Args:
        event_ref (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventRead | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            event_ref=event_ref,
            client=client,
        )
    ).parsed
