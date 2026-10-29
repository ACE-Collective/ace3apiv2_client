from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_resolution_request import BulkResolutionRequest
from ...models.bulk_resolution_result import BulkResolutionResult
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: BulkResolutionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/svs/worklist/bulk/resolve",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BulkResolutionResult | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BulkResolutionResult.from_dict(response.json())

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
) -> Response[BulkResolutionResult | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkResolutionRequest,
) -> Response[BulkResolutionResult | HTTPValidationError]:
    """Bulk Resolve

     Resolve many rows alike, in one transaction; rows that don't exist or can't be resolved are
    reported and left alone. 422 for a resolution, reason or reference that isn't valid.

    Args:
        body (BulkResolutionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkResolutionResult | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BulkResolutionRequest,
) -> BulkResolutionResult | HTTPValidationError | None:
    """Bulk Resolve

     Resolve many rows alike, in one transaction; rows that don't exist or can't be resolved are
    reported and left alone. 422 for a resolution, reason or reference that isn't valid.

    Args:
        body (BulkResolutionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkResolutionResult | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkResolutionRequest,
) -> Response[BulkResolutionResult | HTTPValidationError]:
    """Bulk Resolve

     Resolve many rows alike, in one transaction; rows that don't exist or can't be resolved are
    reported and left alone. 422 for a resolution, reason or reference that isn't valid.

    Args:
        body (BulkResolutionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkResolutionResult | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BulkResolutionRequest,
) -> BulkResolutionResult | HTTPValidationError | None:
    """Bulk Resolve

     Resolve many rows alike, in one transaction; rows that don't exist or can't be resolved are
    reported and left alone. 422 for a resolution, reason or reference that isn't valid.

    Args:
        body (BulkResolutionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkResolutionResult | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
