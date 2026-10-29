from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.validation_detail import ValidationDetail
from ...types import Response


def _get_kwargs(
    validation_uuid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/svs/yara/validations/{validation_uuid}".format(
            validation_uuid=quote(str(validation_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ValidationDetail | None:
    if response.status_code == 200:
        response_200 = ValidationDetail.from_dict(response.json())

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
) -> Response[HTTPValidationError | ValidationDetail]:
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
) -> Response[HTTPValidationError | ValidationDetail]:
    """Get Validation

     One validation with its report; the pairs it lists are GET /{uuid}/results.

    Args:
        validation_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ValidationDetail]
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
) -> HTTPValidationError | ValidationDetail | None:
    """Get Validation

     One validation with its report; the pairs it lists are GET /{uuid}/results.

    Args:
        validation_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ValidationDetail
    """

    return sync_detailed(
        validation_uuid=validation_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    validation_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | ValidationDetail]:
    """Get Validation

     One validation with its report; the pairs it lists are GET /{uuid}/results.

    Args:
        validation_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ValidationDetail]
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
) -> HTTPValidationError | ValidationDetail | None:
    """Get Validation

     One validation with its report; the pairs it lists are GET /{uuid}/results.

    Args:
        validation_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ValidationDetail
    """

    return (
        await asyncio_detailed(
            validation_uuid=validation_uuid,
            client=client,
        )
    ).parsed
