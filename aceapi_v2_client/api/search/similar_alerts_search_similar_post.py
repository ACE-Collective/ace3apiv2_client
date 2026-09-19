from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_search_response import AlertSearchResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.similar_alerts_request import SimilarAlertsRequest
from ...types import Response


def _get_kwargs(
    *,
    body: SimilarAlertsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/search/similar",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertSearchResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AlertSearchResponse.from_dict(response.json())

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
) -> Response[AlertSearchResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SimilarAlertsRequest,
) -> Response[AlertSearchResponse | HTTPValidationError]:
    """Similar Alerts

     Alerts most similar to the given alert, with their dispositions -- "have we seen this before?".

    Args:
        body (SimilarAlertsRequest): Alerts most similar to a given alert, by the alert's own
            indexed text.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertSearchResponse | HTTPValidationError]
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
    body: SimilarAlertsRequest,
) -> AlertSearchResponse | HTTPValidationError | None:
    """Similar Alerts

     Alerts most similar to the given alert, with their dispositions -- "have we seen this before?".

    Args:
        body (SimilarAlertsRequest): Alerts most similar to a given alert, by the alert's own
            indexed text.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertSearchResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SimilarAlertsRequest,
) -> Response[AlertSearchResponse | HTTPValidationError]:
    """Similar Alerts

     Alerts most similar to the given alert, with their dispositions -- "have we seen this before?".

    Args:
        body (SimilarAlertsRequest): Alerts most similar to a given alert, by the alert's own
            indexed text.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertSearchResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SimilarAlertsRequest,
) -> AlertSearchResponse | HTTPValidationError | None:
    """Similar Alerts

     Alerts most similar to the given alert, with their dispositions -- "have we seen this before?".

    Args:
        body (SimilarAlertsRequest): Alerts most similar to a given alert, by the alert's own
            indexed text.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertSearchResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
