from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.set_owner_request import SetOwnerRequest
from ...models.set_owner_result import SetOwnerResult
from ...types import Response


def _get_kwargs(
    *,
    body: SetOwnerRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/alerts/owner",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SetOwnerResult | None:
    if response.status_code == 200:
        response_200 = SetOwnerResult.from_dict(response.json())

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
) -> Response[HTTPValidationError | SetOwnerResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SetOwnerRequest,
) -> Response[HTTPValidationError | SetOwnerResult]:
    """Set Alert Owner

     Sets the owner of the alerts: the caller takes them when `owner_id` is their own id, assigns
    them to someone else otherwise, and unassigns them when it is null. An alert another analyst
    owns is left alone unless `take_owned` confirms taking it from them
    (saq.database.util.alert.check_alert_ownership).

    Args:
        body (SetOwnerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SetOwnerResult]
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
    body: SetOwnerRequest,
) -> HTTPValidationError | SetOwnerResult | None:
    """Set Alert Owner

     Sets the owner of the alerts: the caller takes them when `owner_id` is their own id, assigns
    them to someone else otherwise, and unassigns them when it is null. An alert another analyst
    owns is left alone unless `take_owned` confirms taking it from them
    (saq.database.util.alert.check_alert_ownership).

    Args:
        body (SetOwnerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SetOwnerResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SetOwnerRequest,
) -> Response[HTTPValidationError | SetOwnerResult]:
    """Set Alert Owner

     Sets the owner of the alerts: the caller takes them when `owner_id` is their own id, assigns
    them to someone else otherwise, and unassigns them when it is null. An alert another analyst
    owns is left alone unless `take_owned` confirms taking it from them
    (saq.database.util.alert.check_alert_ownership).

    Args:
        body (SetOwnerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SetOwnerResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SetOwnerRequest,
) -> HTTPValidationError | SetOwnerResult | None:
    """Set Alert Owner

     Sets the owner of the alerts: the caller takes them when `owner_id` is their own id, assigns
    them to someone else otherwise, and unassigns them when it is null. An alert another analyst
    owns is left alone unless `take_owned` confirms taking it from them
    (saq.database.util.alert.check_alert_ownership).

    Args:
        body (SetOwnerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SetOwnerResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
