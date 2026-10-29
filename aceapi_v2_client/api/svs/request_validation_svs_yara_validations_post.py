from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.validation_request import ValidationRequest
from ...models.validation_status import ValidationStatus
from ...types import Response


def _get_kwargs(
    *,
    body: ValidationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/svs/yara/validations/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ValidationStatus | None:
    if response.status_code == 202:
        response_202 = ValidationStatus.from_dict(response.json())

        return response_202

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | ValidationStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ValidationRequest,
) -> Response[HTTPValidationError | ValidationStatus]:
    """Request Validation

     Request a validation of head_sha against base_sha: 202 with a new queued validation, or 200
    with the one that already answers it (queued or running for the same commits, or completed with
    the samples, their labels and the engine unchanged since). Poll GET /{uuid}/status.

    Args:
        body (ValidationRequest): What the signature repository's CI asks for: validate head_sha
            against base_sha.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ValidationStatus]
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
    body: ValidationRequest,
) -> HTTPValidationError | ValidationStatus | None:
    """Request Validation

     Request a validation of head_sha against base_sha: 202 with a new queued validation, or 200
    with the one that already answers it (queued or running for the same commits, or completed with
    the samples, their labels and the engine unchanged since). Poll GET /{uuid}/status.

    Args:
        body (ValidationRequest): What the signature repository's CI asks for: validate head_sha
            against base_sha.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ValidationStatus
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ValidationRequest,
) -> Response[HTTPValidationError | ValidationStatus]:
    """Request Validation

     Request a validation of head_sha against base_sha: 202 with a new queued validation, or 200
    with the one that already answers it (queued or running for the same commits, or completed with
    the samples, their labels and the engine unchanged since). Poll GET /{uuid}/status.

    Args:
        body (ValidationRequest): What the signature repository's CI asks for: validate head_sha
            against base_sha.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ValidationStatus]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ValidationRequest,
) -> HTTPValidationError | ValidationStatus | None:
    """Request Validation

     Request a validation of head_sha against base_sha: 202 with a new queued validation, or 200
    with the one that already answers it (queued or running for the same commits, or completed with
    the samples, their labels and the engine unchanged since). Poll GET /{uuid}/status.

    Args:
        body (ValidationRequest): What the signature repository's CI asks for: validate head_sha
            against base_sha.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ValidationStatus
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
