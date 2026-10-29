from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    alert_uuid: str,
    observable_uuid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/alerts/{alert_uuid}/observables/{observable_uuid}/text".format(
            alert_uuid=quote(str(alert_uuid), safe=""),
            observable_uuid=quote(str(observable_uuid), safe=""),
        ),
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
    alert_uuid: str,
    observable_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | str]:
    """View Observable File As Text

     A file observable of the alert, as text: its bytes as they are, served as text/plain
    (the alert page's View As Text).

    Args:
        alert_uuid (str):
        observable_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
    """

    kwargs = _get_kwargs(
        alert_uuid=alert_uuid,
        observable_uuid=observable_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_uuid: str,
    observable_uuid: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | str | None:
    """View Observable File As Text

     A file observable of the alert, as text: its bytes as they are, served as text/plain
    (the alert page's View As Text).

    Args:
        alert_uuid (str):
        observable_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
    """

    return sync_detailed(
        alert_uuid=alert_uuid,
        observable_uuid=observable_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    alert_uuid: str,
    observable_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | str]:
    """View Observable File As Text

     A file observable of the alert, as text: its bytes as they are, served as text/plain
    (the alert page's View As Text).

    Args:
        alert_uuid (str):
        observable_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
    """

    kwargs = _get_kwargs(
        alert_uuid=alert_uuid,
        observable_uuid=observable_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_uuid: str,
    observable_uuid: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | str | None:
    """View Observable File As Text

     A file observable of the alert, as text: its bytes as they are, served as text/plain
    (the alert page's View As Text).

    Args:
        alert_uuid (str):
        observable_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
    """

    return (
        await asyncio_detailed(
            alert_uuid=alert_uuid,
            observable_uuid=observable_uuid,
            client=client,
        )
    ).parsed
