from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hunt_validation_result import HuntValidationResult
from ...models.validate_hunt_hunt_validate_post_hunt_validation_request import (
    ValidateHuntHuntValidatePostHuntValidationRequest,
)
from ...types import Response


def _get_kwargs(
    *,
    body: ValidateHuntHuntValidatePostHuntValidationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/hunt/validate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HuntValidationResult | None:
    if response.status_code == 200:
        response_200 = HuntValidationResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = HuntValidationResult.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HuntValidationResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ValidateHuntHuntValidatePostHuntValidationRequest,
) -> Response[HuntValidationResult]:
    """Validate Hunt

     Check a hunt package the way the hunter loads it and, with execution_arguments, run it,
    optionally analyzing its results or creating alerts, which belong to the caller. The answer
    carries every log line the run wrote.

    Args:
        body (ValidateHuntHuntValidatePostHuntValidationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HuntValidationResult]
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
    body: ValidateHuntHuntValidatePostHuntValidationRequest,
) -> HuntValidationResult | None:
    """Validate Hunt

     Check a hunt package the way the hunter loads it and, with execution_arguments, run it,
    optionally analyzing its results or creating alerts, which belong to the caller. The answer
    carries every log line the run wrote.

    Args:
        body (ValidateHuntHuntValidatePostHuntValidationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HuntValidationResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ValidateHuntHuntValidatePostHuntValidationRequest,
) -> Response[HuntValidationResult]:
    """Validate Hunt

     Check a hunt package the way the hunter loads it and, with execution_arguments, run it,
    optionally analyzing its results or creating alerts, which belong to the caller. The answer
    carries every log line the run wrote.

    Args:
        body (ValidateHuntHuntValidatePostHuntValidationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HuntValidationResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ValidateHuntHuntValidatePostHuntValidationRequest,
) -> HuntValidationResult | None:
    """Validate Hunt

     Check a hunt package the way the hunter loads it and, with execution_arguments, run it,
    optionally analyzing its results or creating alerts, which belong to the caller. The answer
    carries every log line the run wrote.

    Args:
        body (ValidateHuntHuntValidatePostHuntValidationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HuntValidationResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
