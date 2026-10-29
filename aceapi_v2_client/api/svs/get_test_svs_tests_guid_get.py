from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_test_detail import CatalogTestDetail
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    guid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/svs/tests/{guid}".format(
            guid=quote(str(guid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CatalogTestDetail | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CatalogTestDetail.from_dict(response.json())

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
) -> Response[CatalogTestDetail | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    guid: str,
    *,
    client: AuthenticatedClient,
) -> Response[CatalogTestDetail | HTTPValidationError]:
    """Get Test

     One test with its description and its atomic entry: commands, input arguments, dependencies.

    Args:
        guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogTestDetail | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        guid=guid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    guid: str,
    *,
    client: AuthenticatedClient,
) -> CatalogTestDetail | HTTPValidationError | None:
    """Get Test

     One test with its description and its atomic entry: commands, input arguments, dependencies.

    Args:
        guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogTestDetail | HTTPValidationError
    """

    return sync_detailed(
        guid=guid,
        client=client,
    ).parsed


async def asyncio_detailed(
    guid: str,
    *,
    client: AuthenticatedClient,
) -> Response[CatalogTestDetail | HTTPValidationError]:
    """Get Test

     One test with its description and its atomic entry: commands, input arguments, dependencies.

    Args:
        guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogTestDetail | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        guid=guid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    guid: str,
    *,
    client: AuthenticatedClient,
) -> CatalogTestDetail | HTTPValidationError | None:
    """Get Test

     One test with its description and its atomic entry: commands, input arguments, dependencies.

    Args:
        guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogTestDetail | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            guid=guid,
            client=client,
        )
    ).parsed
