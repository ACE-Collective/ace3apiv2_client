from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key_created import ApiKeyCreated
from ...models.api_key_self_write import ApiKeySelfWrite
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: ApiKeySelfWrite,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/me/apikeys",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiKeyCreated | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = ApiKeyCreated.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiKeyCreated | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiKeySelfWrite,
) -> Response[ApiKeyCreated | HTTPValidationError]:
    """Create My Api Key

     Mint a scoped API key for the caller. Every pattern in the scope must cover only
    permissions the caller holds; the plaintext is returned exactly once.

    Args:
        body (ApiKeySelfWrite): A user's request to create or change one of their OWN keys. Self-
            service keys are always
            scoped -- only an admin mints a key that inherits its owner's full permissions -- so there
            is
            no inherit field, and this is deliberately not ApiKeyCreate with one removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyCreated | HTTPValidationError]
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
    body: ApiKeySelfWrite,
) -> ApiKeyCreated | HTTPValidationError | None:
    """Create My Api Key

     Mint a scoped API key for the caller. Every pattern in the scope must cover only
    permissions the caller holds; the plaintext is returned exactly once.

    Args:
        body (ApiKeySelfWrite): A user's request to create or change one of their OWN keys. Self-
            service keys are always
            scoped -- only an admin mints a key that inherits its owner's full permissions -- so there
            is
            no inherit field, and this is deliberately not ApiKeyCreate with one removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyCreated | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiKeySelfWrite,
) -> Response[ApiKeyCreated | HTTPValidationError]:
    """Create My Api Key

     Mint a scoped API key for the caller. Every pattern in the scope must cover only
    permissions the caller holds; the plaintext is returned exactly once.

    Args:
        body (ApiKeySelfWrite): A user's request to create or change one of their OWN keys. Self-
            service keys are always
            scoped -- only an admin mints a key that inherits its owner's full permissions -- so there
            is
            no inherit field, and this is deliberately not ApiKeyCreate with one removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyCreated | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ApiKeySelfWrite,
) -> ApiKeyCreated | HTTPValidationError | None:
    """Create My Api Key

     Mint a scoped API key for the caller. Every pattern in the scope must cover only
    permissions the caller holds; the plaintext is returned exactly once.

    Args:
        body (ApiKeySelfWrite): A user's request to create or change one of their OWN keys. Self-
            service keys are always
            scoped -- only an admin mints a key that inherits its owner's full permissions -- so there
            is
            no inherit field, and this is deliberately not ApiKeyCreate with one removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyCreated | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
