from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_response_remediation_target_read import (
    ListResponseRemediationTargetRead,
)
from ...models.target_lookup_request import TargetLookupRequest
from ...types import Response


def _get_kwargs(
    *,
    body: TargetLookupRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/remediation/targets/lookup",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ListResponseRemediationTargetRead | None:
    if response.status_code == 200:
        response_200 = ListResponseRemediationTargetRead.from_dict(response.json())

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
) -> Response[HTTPValidationError | ListResponseRemediationTargetRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: TargetLookupRequest,
) -> Response[HTTPValidationError | ListResponseRemediationTargetRead]:
    """Lookup Targets

     The remediation targets of the observables in these alerts, or of these observables, each
    with its latest remediation.

    A POST so that a long selection fits in the body. Each alert's analysis is loaded from disk.
    An observable value its type rejects is a 422.

    Args:
        body (TargetLookupRequest): The alerts, or the observables, to find the remediation
            targets of: exactly one of the two.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListResponseRemediationTargetRead]
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
    body: TargetLookupRequest,
) -> HTTPValidationError | ListResponseRemediationTargetRead | None:
    """Lookup Targets

     The remediation targets of the observables in these alerts, or of these observables, each
    with its latest remediation.

    A POST so that a long selection fits in the body. Each alert's analysis is loaded from disk.
    An observable value its type rejects is a 422.

    Args:
        body (TargetLookupRequest): The alerts, or the observables, to find the remediation
            targets of: exactly one of the two.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListResponseRemediationTargetRead
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TargetLookupRequest,
) -> Response[HTTPValidationError | ListResponseRemediationTargetRead]:
    """Lookup Targets

     The remediation targets of the observables in these alerts, or of these observables, each
    with its latest remediation.

    A POST so that a long selection fits in the body. Each alert's analysis is loaded from disk.
    An observable value its type rejects is a 422.

    Args:
        body (TargetLookupRequest): The alerts, or the observables, to find the remediation
            targets of: exactly one of the two.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListResponseRemediationTargetRead]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: TargetLookupRequest,
) -> HTTPValidationError | ListResponseRemediationTargetRead | None:
    """Lookup Targets

     The remediation targets of the observables in these alerts, or of these observables, each
    with its latest remediation.

    A POST so that a long selection fits in the body. Each alert's analysis is loaded from disk.
    An observable value its type rejects is a 422.

    Args:
        body (TargetLookupRequest): The alerts, or the observables, to find the remediation
            targets of: exactly one of the two.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListResponseRemediationTargetRead
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
