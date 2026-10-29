from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.validation_status import ValidationStatus
from ...types import Response


def _get_kwargs(
    validation_uuid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/svs/yara/validations/{validation_uuid}/status".format(
            validation_uuid=quote(str(validation_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ValidationStatus | None:
    if response.status_code == 200:
        response_200 = ValidationStatus.from_dict(response.json())

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
) -> Response[HTTPValidationError | ValidationStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    validation_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | ValidationStatus]:
    """Get Validation Status

     A validation's state and, once completed, its counts per category, the rules with samples
    in each listed category, and the head's compile errors. Names no sample.

    Args:
        validation_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ValidationStatus]
    """

    kwargs = _get_kwargs(
        validation_uuid=validation_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    validation_uuid: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | ValidationStatus | None:
    """Get Validation Status

     A validation's state and, once completed, its counts per category, the rules with samples
    in each listed category, and the head's compile errors. Names no sample.

    Args:
        validation_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ValidationStatus
    """

    return sync_detailed(
        validation_uuid=validation_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    validation_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | ValidationStatus]:
    """Get Validation Status

     A validation's state and, once completed, its counts per category, the rules with samples
    in each listed category, and the head's compile errors. Names no sample.

    Args:
        validation_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ValidationStatus]
    """

    kwargs = _get_kwargs(
        validation_uuid=validation_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    validation_uuid: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | ValidationStatus | None:
    """Get Validation Status

     A validation's state and, once completed, its counts per category, the rules with samples
    in each listed category, and the head's compile errors. Names no sample.

    Args:
        validation_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ValidationStatus
    """

    return (
        await asyncio_detailed(
            validation_uuid=validation_uuid,
            client=client,
        )
    ).parsed
