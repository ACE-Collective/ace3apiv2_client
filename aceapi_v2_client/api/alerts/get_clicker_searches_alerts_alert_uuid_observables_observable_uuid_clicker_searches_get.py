from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_response_clicker_search import ListResponseClickerSearch
from ...types import Response


def _get_kwargs(
    alert_uuid: str,
    observable_uuid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/alerts/{alert_uuid}/observables/{observable_uuid}/clicker-searches".format(
            alert_uuid=quote(str(alert_uuid), safe=""),
            observable_uuid=quote(str(observable_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ListResponseClickerSearch | None:
    if response.status_code == 200:
        response_200 = ListResponseClickerSearch.from_dict(response.json())

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
) -> Response[HTTPValidationError | ListResponseClickerSearch]:
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
) -> Response[HTTPValidationError | ListResponseClickerSearch]:
    """Get Clicker Searches

     The Splunk searches the clicker check runs for this observable, as Splunk web URLs, to run
    by hand. Empty when none is configured for its type.

    Args:
        alert_uuid (str):
        observable_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListResponseClickerSearch]
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
) -> HTTPValidationError | ListResponseClickerSearch | None:
    """Get Clicker Searches

     The Splunk searches the clicker check runs for this observable, as Splunk web URLs, to run
    by hand. Empty when none is configured for its type.

    Args:
        alert_uuid (str):
        observable_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListResponseClickerSearch
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
) -> Response[HTTPValidationError | ListResponseClickerSearch]:
    """Get Clicker Searches

     The Splunk searches the clicker check runs for this observable, as Splunk web URLs, to run
    by hand. Empty when none is configured for its type.

    Args:
        alert_uuid (str):
        observable_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListResponseClickerSearch]
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
) -> HTTPValidationError | ListResponseClickerSearch | None:
    """Get Clicker Searches

     The Splunk searches the clicker check runs for this observable, as Splunk web URLs, to run
    by hand. Empty when none is configured for its type.

    Args:
        alert_uuid (str):
        observable_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListResponseClickerSearch
    """

    return (
        await asyncio_detailed(
            alert_uuid=alert_uuid,
            observable_uuid=observable_uuid,
            client=client,
        )
    ).parsed
