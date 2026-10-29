from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key_read import ApiKeyRead
from ...models.api_key_self_write import ApiKeySelfWrite
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    key_id: int,
    *,
    body: ApiKeySelfWrite,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/users/me/apikeys/{key_id}".format(
            key_id=quote(str(key_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiKeyRead | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ApiKeyRead.from_dict(response.json())

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
) -> Response[ApiKeyRead | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key_id: int,
    *,
    client: AuthenticatedClient,
    body: ApiKeySelfWrite,
) -> Response[ApiKeyRead | HTTPValidationError]:
    """Update My Api Key

     Rename one of the caller's keys and replace its scope, under the same rules as minting.
    Another user's key is reported as not found.

    Args:
        key_id (int):
        body (ApiKeySelfWrite): A user's request to create or change one of their OWN keys. Self-
            service keys are always
            scoped -- only an admin mints a key that inherits its owner's full permissions -- so there
            is
            no inherit field, and this is deliberately not ApiKeyCreate with one removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyRead | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key_id: int,
    *,
    client: AuthenticatedClient,
    body: ApiKeySelfWrite,
) -> ApiKeyRead | HTTPValidationError | None:
    """Update My Api Key

     Rename one of the caller's keys and replace its scope, under the same rules as minting.
    Another user's key is reported as not found.

    Args:
        key_id (int):
        body (ApiKeySelfWrite): A user's request to create or change one of their OWN keys. Self-
            service keys are always
            scoped -- only an admin mints a key that inherits its owner's full permissions -- so there
            is
            no inherit field, and this is deliberately not ApiKeyCreate with one removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyRead | HTTPValidationError
    """

    return sync_detailed(
        key_id=key_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    key_id: int,
    *,
    client: AuthenticatedClient,
    body: ApiKeySelfWrite,
) -> Response[ApiKeyRead | HTTPValidationError]:
    """Update My Api Key

     Rename one of the caller's keys and replace its scope, under the same rules as minting.
    Another user's key is reported as not found.

    Args:
        key_id (int):
        body (ApiKeySelfWrite): A user's request to create or change one of their OWN keys. Self-
            service keys are always
            scoped -- only an admin mints a key that inherits its owner's full permissions -- so there
            is
            no inherit field, and this is deliberately not ApiKeyCreate with one removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyRead | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key_id: int,
    *,
    client: AuthenticatedClient,
    body: ApiKeySelfWrite,
) -> ApiKeyRead | HTTPValidationError | None:
    """Update My Api Key

     Rename one of the caller's keys and replace its scope, under the same rules as minting.
    Another user's key is reported as not found.

    Args:
        key_id (int):
        body (ApiKeySelfWrite): A user's request to create or change one of their OWN keys. Self-
            service keys are always
            scoped -- only an admin mints a key that inherits its owner's full permissions -- so there
            is
            no inherit field, and this is deliberately not ApiKeyCreate with one removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyRead | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            key_id=key_id,
            client=client,
            body=body,
        )
    ).parsed
