from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_read import UserRead
from ...models.user_self_update import UserSelfUpdate
from ...types import Response


def _get_kwargs(
    *,
    body: UserSelfUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/users/me",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UserRead | None:
    if response.status_code == 200:
        response_200 = UserRead.from_dict(response.json())

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
) -> Response[HTTPValidationError | UserRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UserSelfUpdate,
) -> Response[HTTPValidationError | UserRead]:
    """Update Me

     Edit the caller's own display name, timezone or default queue. Needs no permission
    beyond being authenticated as a user: the admin ``user:write`` endpoints are for editing
    OTHER accounts.

    Args:
        body (UserSelfUpdate): The fields a user may change on their OWN account from the
            preferences page. Username,
            email, password and enablement stay with the admin endpoints (and the change-password
            page), so this is deliberately not UserUpdate with the id removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserRead]
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
    body: UserSelfUpdate,
) -> HTTPValidationError | UserRead | None:
    """Update Me

     Edit the caller's own display name, timezone or default queue. Needs no permission
    beyond being authenticated as a user: the admin ``user:write`` endpoints are for editing
    OTHER accounts.

    Args:
        body (UserSelfUpdate): The fields a user may change on their OWN account from the
            preferences page. Username,
            email, password and enablement stay with the admin endpoints (and the change-password
            page), so this is deliberately not UserUpdate with the id removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserRead
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UserSelfUpdate,
) -> Response[HTTPValidationError | UserRead]:
    """Update Me

     Edit the caller's own display name, timezone or default queue. Needs no permission
    beyond being authenticated as a user: the admin ``user:write`` endpoints are for editing
    OTHER accounts.

    Args:
        body (UserSelfUpdate): The fields a user may change on their OWN account from the
            preferences page. Username,
            email, password and enablement stay with the admin endpoints (and the change-password
            page), so this is deliberately not UserUpdate with the id removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserRead]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UserSelfUpdate,
) -> HTTPValidationError | UserRead | None:
    """Update Me

     Edit the caller's own display name, timezone or default queue. Needs no permission
    beyond being authenticated as a user: the admin ``user:write`` endpoints are for editing
    OTHER accounts.

    Args:
        body (UserSelfUpdate): The fields a user may change on their OWN account from the
            preferences page. Username,
            email, password and enablement stay with the admin endpoints (and the change-password
            page), so this is deliberately not UserUpdate with the id removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserRead
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
