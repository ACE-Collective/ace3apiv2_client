from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_submit_analysis_post import BodySubmitAnalysisPost
from ...models.http_validation_error import HTTPValidationError
from ...models.submit_result import SubmitResult
from ...types import Response


def _get_kwargs(
    *,
    body: BodySubmitAnalysisPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/analysis/",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SubmitResult | None:
    if response.status_code == 201:
        response_201 = SubmitResult.from_dict(response.json())

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
) -> Response[HTTPValidationError | SubmitResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodySubmitAnalysisPost,
) -> Response[HTTPValidationError | SubmitResult]:
    """Submit

     Create a root analysis from a submission and queue it on this node; in correlation mode it
    becomes an alert. 503 while the node is draining.

    Args:
        body (BodySubmitAnalysisPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SubmitResult]
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
    body: BodySubmitAnalysisPost,
) -> HTTPValidationError | SubmitResult | None:
    """Submit

     Create a root analysis from a submission and queue it on this node; in correlation mode it
    becomes an alert. 503 while the node is draining.

    Args:
        body (BodySubmitAnalysisPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SubmitResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodySubmitAnalysisPost,
) -> Response[HTTPValidationError | SubmitResult]:
    """Submit

     Create a root analysis from a submission and queue it on this node; in correlation mode it
    becomes an alert. 503 while the node is draining.

    Args:
        body (BodySubmitAnalysisPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SubmitResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodySubmitAnalysisPost,
) -> HTTPValidationError | SubmitResult | None:
    """Submit

     Create a root analysis from a submission and queue it on this node; in correlation mode it
    becomes an alert. 503 while the node is draining.

    Args:
        body (BodySubmitAnalysisPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SubmitResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
