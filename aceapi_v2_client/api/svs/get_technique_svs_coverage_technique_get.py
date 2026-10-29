from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.technique_coverage import TechniqueCoverage
from ...types import Response


def _get_kwargs(
    technique: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/svs/coverage/{technique}".format(
            technique=quote(str(technique), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TechniqueCoverage | None:
    if response.status_code == 200:
        response_200 = TechniqueCoverage.from_dict(response.json())

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
) -> Response[HTTPValidationError | TechniqueCoverage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    technique: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | TechniqueCoverage]:
    """Get Technique

     A technique's coverage: its rows and its sub-techniques' as of the last refresh, and the tests
    and signatures that count toward them now. A revoked id answers for its successor; 400 for
    something that isn't a technique id, 404 for a technique with no rows that the release doesn't
    have.

    Args:
        technique (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TechniqueCoverage]
    """

    kwargs = _get_kwargs(
        technique=technique,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    technique: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | TechniqueCoverage | None:
    """Get Technique

     A technique's coverage: its rows and its sub-techniques' as of the last refresh, and the tests
    and signatures that count toward them now. A revoked id answers for its successor; 400 for
    something that isn't a technique id, 404 for a technique with no rows that the release doesn't
    have.

    Args:
        technique (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TechniqueCoverage
    """

    return sync_detailed(
        technique=technique,
        client=client,
    ).parsed


async def asyncio_detailed(
    technique: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | TechniqueCoverage]:
    """Get Technique

     A technique's coverage: its rows and its sub-techniques' as of the last refresh, and the tests
    and signatures that count toward them now. A revoked id answers for its successor; 400 for
    something that isn't a technique id, 404 for a technique with no rows that the release doesn't
    have.

    Args:
        technique (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TechniqueCoverage]
    """

    kwargs = _get_kwargs(
        technique=technique,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    technique: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | TechniqueCoverage | None:
    """Get Technique

     A technique's coverage: its rows and its sub-techniques' as of the last refresh, and the tests
    and signatures that count toward them now. A revoked id answers for its successor; 400 for
    something that isn't a technique id, 404 for a technique with no rows that the release doesn't
    have.

    Args:
        technique (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TechniqueCoverage
    """

    return (
        await asyncio_detailed(
            technique=technique,
            client=client,
        )
    ).parsed
