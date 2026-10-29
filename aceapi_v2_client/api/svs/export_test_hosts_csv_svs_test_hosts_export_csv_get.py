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
    changed_since: datetime.datetime | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_changed_since: None | str | Unset
    if isinstance(changed_since, Unset):
        json_changed_since = UNSET
    elif isinstance(changed_since, datetime.datetime):
        json_changed_since = changed_since.isoformat()
    else:
        json_changed_since = changed_since
    params["changed_since"] = json_changed_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/svs/test-hosts/export/csv",
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
    changed_since: datetime.datetime | None | Unset = UNSET,
) -> Response[HTTPValidationError | str]:
    """Export Test Hosts Csv

     Stream every test host as CSV (usernames and ips joined with ",").

    Args:
        changed_since (datetime.datetime | None | Unset): only test hosts added or changed at or
            after this time (UTC if no offset is given)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
    """

    kwargs = _get_kwargs(
        changed_since=changed_since,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    changed_since: datetime.datetime | None | Unset = UNSET,
) -> HTTPValidationError | str | None:
    """Export Test Hosts Csv

     Stream every test host as CSV (usernames and ips joined with ",").

    Args:
        changed_since (datetime.datetime | None | Unset): only test hosts added or changed at or
            after this time (UTC if no offset is given)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
    """

    return sync_detailed(
        client=client,
        changed_since=changed_since,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    changed_since: datetime.datetime | None | Unset = UNSET,
) -> Response[HTTPValidationError | str]:
    """Export Test Hosts Csv

     Stream every test host as CSV (usernames and ips joined with ",").

    Args:
        changed_since (datetime.datetime | None | Unset): only test hosts added or changed at or
            after this time (UTC if no offset is given)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
    """

    kwargs = _get_kwargs(
        changed_since=changed_since,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    changed_since: datetime.datetime | None | Unset = UNSET,
) -> HTTPValidationError | str | None:
    """Export Test Hosts Csv

     Stream every test host as CSV (usernames and ips joined with ",").

    Args:
        changed_since (datetime.datetime | None | Unset): only test hosts added or changed at or
            after this time (UTC if no offset is given)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
    """

    return (
        await asyncio_detailed(
            client=client,
            changed_since=changed_since,
        )
    ).parsed
