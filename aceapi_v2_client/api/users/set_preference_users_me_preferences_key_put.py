from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.preference_read import PreferenceRead
from ...models.set_preference_users_me_preferences_key_put_body import (
    SetPreferenceUsersMePreferencesKeyPutBody,
)
from ...types import Response


def _get_kwargs(
    key: str,
    *,
    body: SetPreferenceUsersMePreferencesKeyPutBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/users/me/preferences/{key}".format(
            key=quote(str(key), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PreferenceRead | None:
    if response.status_code == 200:
        response_200 = PreferenceRead.from_dict(response.json())

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
) -> Response[HTTPValidationError | PreferenceRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key: str,
    *,
    client: AuthenticatedClient,
    body: SetPreferenceUsersMePreferencesKeyPutBody,
) -> Response[HTTPValidationError | PreferenceRead]:
    """Set Preference

     Replace the caller's value for one preference. The body is the value itself, in the
    shape the key's schema declares; it is normalized before it is stored and the response
    carries the normalized form.

    Args:
        key (str):
        body (SetPreferenceUsersMePreferencesKeyPutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PreferenceRead]
    """

    kwargs = _get_kwargs(
        key=key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key: str,
    *,
    client: AuthenticatedClient,
    body: SetPreferenceUsersMePreferencesKeyPutBody,
) -> HTTPValidationError | PreferenceRead | None:
    """Set Preference

     Replace the caller's value for one preference. The body is the value itself, in the
    shape the key's schema declares; it is normalized before it is stored and the response
    carries the normalized form.

    Args:
        key (str):
        body (SetPreferenceUsersMePreferencesKeyPutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PreferenceRead
    """

    return sync_detailed(
        key=key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    key: str,
    *,
    client: AuthenticatedClient,
    body: SetPreferenceUsersMePreferencesKeyPutBody,
) -> Response[HTTPValidationError | PreferenceRead]:
    """Set Preference

     Replace the caller's value for one preference. The body is the value itself, in the
    shape the key's schema declares; it is normalized before it is stored and the response
    carries the normalized form.

    Args:
        key (str):
        body (SetPreferenceUsersMePreferencesKeyPutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PreferenceRead]
    """

    kwargs = _get_kwargs(
        key=key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key: str,
    *,
    client: AuthenticatedClient,
    body: SetPreferenceUsersMePreferencesKeyPutBody,
) -> HTTPValidationError | PreferenceRead | None:
    """Set Preference

     Replace the caller's value for one preference. The body is the value itself, in the
    shape the key's schema declares; it is normalized before it is stored and the response
    carries the normalized form.

    Args:
        key (str):
        body (SetPreferenceUsersMePreferencesKeyPutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PreferenceRead
    """

    return (
        await asyncio_detailed(
            key=key,
            client=client,
            body=body,
        )
    ).parsed
