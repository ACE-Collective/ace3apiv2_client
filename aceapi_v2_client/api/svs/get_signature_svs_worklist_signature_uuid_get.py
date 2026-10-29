from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.signature_worklist import SignatureWorklist
from ...types import Response


def _get_kwargs(
    signature_uuid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/svs/worklist/{signature_uuid}".format(
            signature_uuid=quote(str(signature_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SignatureWorklist | None:
    if response.status_code == 200:
        response_200 = SignatureWorklist.from_dict(response.json())

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
) -> Response[HTTPValidationError | SignatureWorklist]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | SignatureWorklist]:
    """Get Signature

     A signature's rows, retired ones included, and what it is measured on now; 404 when it has
    none.

    Args:
        signature_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SignatureWorklist]
    """

    kwargs = _get_kwargs(
        signature_uuid=signature_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | SignatureWorklist | None:
    """Get Signature

     A signature's rows, retired ones included, and what it is measured on now; 404 when it has
    none.

    Args:
        signature_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SignatureWorklist
    """

    return sync_detailed(
        signature_uuid=signature_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | SignatureWorklist]:
    """Get Signature

     A signature's rows, retired ones included, and what it is measured on now; 404 when it has
    none.

    Args:
        signature_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SignatureWorklist]
    """

    kwargs = _get_kwargs(
        signature_uuid=signature_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | SignatureWorklist | None:
    """Get Signature

     A signature's rows, retired ones included, and what it is measured on now; 404 when it has
    none.

    Args:
        signature_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SignatureWorklist
    """

    return (
        await asyncio_detailed(
            signature_uuid=signature_uuid,
            client=client,
        )
    ).parsed
