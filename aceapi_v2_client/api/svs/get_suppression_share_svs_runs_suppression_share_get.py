from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.suppression_share import SuppressionShare
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/svs/runs/suppression-share",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SuppressionShare | None:
    if response.status_code == 200:
        response_200 = SuppressionShare.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SuppressionShare]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[SuppressionShare]:
    """Get Suppression Share

     How many of the expected signatures missing from reviewed runs were possibly suppressed, and
    whether the revisit trigger is reached (docs/SVS_API.md, *Suppression share*).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuppressionShare]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> SuppressionShare | None:
    """Get Suppression Share

     How many of the expected signatures missing from reviewed runs were possibly suppressed, and
    whether the revisit trigger is reached (docs/SVS_API.md, *Suppression share*).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuppressionShare
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[SuppressionShare]:
    """Get Suppression Share

     How many of the expected signatures missing from reviewed runs were possibly suppressed, and
    whether the revisit trigger is reached (docs/SVS_API.md, *Suppression share*).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuppressionShare]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> SuppressionShare | None:
    """Get Suppression Share

     How many of the expected signatures missing from reviewed runs were possibly suppressed, and
    whether the revisit trigger is reached (docs/SVS_API.md, *Suppression share*).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuppressionShare
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
