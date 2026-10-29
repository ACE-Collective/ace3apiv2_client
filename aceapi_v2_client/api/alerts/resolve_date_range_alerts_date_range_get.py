from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.date_range import DateRange
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    value: str,
    tz: str | Unset = "UTC",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["value"] = value

    params["tz"] = tz

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/alerts/date-range",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DateRange | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DateRange.from_dict(response.json())

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
) -> Response[DateRange | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    value: str,
    tz: str | Unset = "UTC",
) -> Response[DateRange | HTTPValidationError]:
    """Resolve Date Range

     The window a date filter value means right now, resolved as the alert filters resolve it.

    The manage page shows it under the relative date input, so that `-24h` is never opaque.

    Args:
        value (str): a date filter value: `-7d`, `-1d@d - @d`, or an absolute range
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DateRange | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        value=value,
        tz=tz,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    value: str,
    tz: str | Unset = "UTC",
) -> DateRange | HTTPValidationError | None:
    """Resolve Date Range

     The window a date filter value means right now, resolved as the alert filters resolve it.

    The manage page shows it under the relative date input, so that `-24h` is never opaque.

    Args:
        value (str): a date filter value: `-7d`, `-1d@d - @d`, or an absolute range
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DateRange | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        value=value,
        tz=tz,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    value: str,
    tz: str | Unset = "UTC",
) -> Response[DateRange | HTTPValidationError]:
    """Resolve Date Range

     The window a date filter value means right now, resolved as the alert filters resolve it.

    The manage page shows it under the relative date input, so that `-24h` is never opaque.

    Args:
        value (str): a date filter value: `-7d`, `-1d@d - @d`, or an absolute range
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DateRange | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        value=value,
        tz=tz,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    value: str,
    tz: str | Unset = "UTC",
) -> DateRange | HTTPValidationError | None:
    """Resolve Date Range

     The window a date filter value means right now, resolved as the alert filters resolve it.

    The manage page shows it under the relative date input, so that `-24h` is never opaque.

    Args:
        value (str): a date filter value: `-7d`, `-1d@d - @d`, or an absolute range
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DateRange | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            value=value,
            tz=tz,
        )
    ).parsed
