from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_count import AlertCount
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    f: list[str] | Unset = UNSET,
    tz: str | Unset = "UTC",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_f: list[str] | Unset = UNSET
    if not isinstance(f, Unset):
        json_f = f

    params["f"] = json_f

    params["tz"] = tz

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/alerts/count",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertCount | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AlertCount.from_dict(response.json())

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
) -> Response[AlertCount | HTTPValidationError]:
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
    tz: str | Unset = "UTC",
) -> Response[AlertCount | HTTPValidationError]:
    """Count Alerts

     How many alerts GET /alerts lists for these filters.

    The alert management page's browser tab polls this with the "Reset" filter to show a dot
    while alerts are waiting.

    Args:
        f (list[str] | Unset): a filter in the manage page's share-link encoding (`[!]slug:v1,v2`,
            see docs/ALERT_FILTER_URLS.md); repeat for more. Filters are ANDed.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertCount | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        f=f,
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
    tz: str | Unset = "UTC",
) -> AlertCount | HTTPValidationError | None:
    """Count Alerts

     How many alerts GET /alerts lists for these filters.

    The alert management page's browser tab polls this with the "Reset" filter to show a dot
    while alerts are waiting.

    Args:
        f (list[str] | Unset): a filter in the manage page's share-link encoding (`[!]slug:v1,v2`,
            see docs/ALERT_FILTER_URLS.md); repeat for more. Filters are ANDed.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertCount | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        f=f,
        tz=tz,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
    tz: str | Unset = "UTC",
) -> Response[AlertCount | HTTPValidationError]:
    """Count Alerts

     How many alerts GET /alerts lists for these filters.

    The alert management page's browser tab polls this with the "Reset" filter to show a dot
    while alerts are waiting.

    Args:
        f (list[str] | Unset): a filter in the manage page's share-link encoding (`[!]slug:v1,v2`,
            see docs/ALERT_FILTER_URLS.md); repeat for more. Filters are ANDed.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertCount | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        f=f,
        tz=tz,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
    tz: str | Unset = "UTC",
) -> AlertCount | HTTPValidationError | None:
    """Count Alerts

     How many alerts GET /alerts lists for these filters.

    The alert management page's browser tab polls this with the "Reset" filter to show a dot
    while alerts are waiting.

    Args:
        f (list[str] | Unset): a filter in the manage page's share-link encoding (`[!]slug:v1,v2`,
            see docs/ALERT_FILTER_URLS.md); repeat for more. Filters are ANDed.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertCount | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            f=f,
            tz=tz,
        )
    ).parsed
