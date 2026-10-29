import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    f: list[str] | Unset = UNSET,
    changed_since: datetime.datetime | None | Unset = UNSET,
    tz: str | Unset = "UTC",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_f: list[str] | Unset = UNSET
    if not isinstance(f, Unset):
        json_f = f

    params["f"] = json_f

    json_changed_since: None | str | Unset
    if isinstance(changed_since, Unset):
        json_changed_since = UNSET
    elif isinstance(changed_since, datetime.datetime):
        json_changed_since = changed_since.isoformat()
    else:
        json_changed_since = changed_since
    params["changed_since"] = json_changed_since

    params["tz"] = tz

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/detection-points/export/csv",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | str | None:
    if response.status_code == 200:
        response_200 = response.text
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
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
    changed_since: datetime.datetime | None | Unset = UNSET,
    tz: str | Unset = "UTC",
) -> Response[HTTPValidationError | str]:
    """Export Detection Points Csv

     Stream every detection the listing matches as CSV: a header line, then one row per
    detection (details written as JSON).

    A failure part-way through cannot change the status code that was already sent: the CSV is
    then truncated, and the failure is logged.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the
            detection points screen's slugs: signature, family, alert_date, queue, verdict, source,
            has_override (see docs/SVS_API.md); repeat for more. Filters are ANDed, the values of one
            ORed.
        changed_since (datetime.datetime | None | Unset): only detections that may have changed at
            or after this time (UTC if no offset is given): the alert's row changed, the detection was
            synced, or its verdict was set or cleared. At-least-once: pass the time the previous pull
            started.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
    """

    kwargs = _get_kwargs(
        f=f,
        changed_since=changed_since,
        tz=tz,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
    changed_since: datetime.datetime | None | Unset = UNSET,
    tz: str | Unset = "UTC",
) -> HTTPValidationError | str | None:
    """Export Detection Points Csv

     Stream every detection the listing matches as CSV: a header line, then one row per
    detection (details written as JSON).

    A failure part-way through cannot change the status code that was already sent: the CSV is
    then truncated, and the failure is logged.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the
            detection points screen's slugs: signature, family, alert_date, queue, verdict, source,
            has_override (see docs/SVS_API.md); repeat for more. Filters are ANDed, the values of one
            ORed.
        changed_since (datetime.datetime | None | Unset): only detections that may have changed at
            or after this time (UTC if no offset is given): the alert's row changed, the detection was
            synced, or its verdict was set or cleared. At-least-once: pass the time the previous pull
            started.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
    """

    return sync_detailed(
        client=client,
        f=f,
        changed_since=changed_since,
        tz=tz,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
    changed_since: datetime.datetime | None | Unset = UNSET,
    tz: str | Unset = "UTC",
) -> Response[HTTPValidationError | str]:
    """Export Detection Points Csv

     Stream every detection the listing matches as CSV: a header line, then one row per
    detection (details written as JSON).

    A failure part-way through cannot change the status code that was already sent: the CSV is
    then truncated, and the failure is logged.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the
            detection points screen's slugs: signature, family, alert_date, queue, verdict, source,
            has_override (see docs/SVS_API.md); repeat for more. Filters are ANDed, the values of one
            ORed.
        changed_since (datetime.datetime | None | Unset): only detections that may have changed at
            or after this time (UTC if no offset is given): the alert's row changed, the detection was
            synced, or its verdict was set or cleared. At-least-once: pass the time the previous pull
            started.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
    """

    kwargs = _get_kwargs(
        f=f,
        changed_since=changed_since,
        tz=tz,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
    changed_since: datetime.datetime | None | Unset = UNSET,
    tz: str | Unset = "UTC",
) -> HTTPValidationError | str | None:
    """Export Detection Points Csv

     Stream every detection the listing matches as CSV: a header line, then one row per
    detection (details written as JSON).

    A failure part-way through cannot change the status code that was already sent: the CSV is
    then truncated, and the failure is logged.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the
            detection points screen's slugs: signature, family, alert_date, queue, verdict, source,
            has_override (see docs/SVS_API.md); repeat for more. Filters are ANDed, the values of one
            ORed.
        changed_since (datetime.datetime | None | Unset): only detections that may have changed at
            or after this time (UTC if no offset is given): the alert's row changed, the detection was
            synced, or its verdict was set or cleared. At-least-once: pass the time the previous pull
            started.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
    """

    return (
        await asyncio_detailed(
            client=client,
            f=f,
            changed_since=changed_since,
            tz=tz,
        )
    ).parsed
