from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.saved_filter_read import SavedFilterRead
from ...types import Response


def _get_kwargs(
    filter_uuid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/saved-filters/{filter_uuid}".format(
            filter_uuid=quote(str(filter_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SavedFilterRead | None:
    if response.status_code == 200:
        response_200 = SavedFilterRead.from_dict(response.json())

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
) -> Response[HTTPValidationError | SavedFilterRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    filter_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | SavedFilterRead]:
    """Get Saved Filter

    Args:
        filter_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SavedFilterRead]
    """

    kwargs = _get_kwargs(
        filter_uuid=filter_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    filter_uuid: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | SavedFilterRead | None:
    """Get Saved Filter

    Args:
        filter_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SavedFilterRead
    """

    return sync_detailed(
        filter_uuid=filter_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    filter_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | SavedFilterRead]:
    """Get Saved Filter

    Args:
        filter_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SavedFilterRead]
    """

    kwargs = _get_kwargs(
        filter_uuid=filter_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    filter_uuid: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | SavedFilterRead | None:
    """Get Saved Filter

    Args:
        filter_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SavedFilterRead
    """

    return (
        await asyncio_detailed(
            filter_uuid=filter_uuid,
            client=client,
        )
    ).parsed
