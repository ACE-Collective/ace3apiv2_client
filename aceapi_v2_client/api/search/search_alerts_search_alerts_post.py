from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_search_request import AlertSearchRequest
from ...models.alert_search_response import AlertSearchResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: AlertSearchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/search/alerts",
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
    body: AlertSearchRequest,
) -> Response[AlertSearchResponse | HTTPValidationError]:
    """Search Alerts

     Search alerts by free text, indicator, tag or uuid.

    Exact matches (an observable value, file hash, tag or alert uuid found verbatim) are returned
    first, newest first, with tier "exact"; semantic matches over the alert's text follow. The
    ranking happens before pagination, so page one always holds the best matches.

    Args:
        body (AlertSearchRequest): Hybrid search over alerts: exact matches for the things named
            with a `field:value` term,
            plus semantic matches over the alert's text (description, comments, detections, email
            content, command lines, ...).

            Either `query` or `filters` is required. With filters and no query the response is a plain
            newest-first listing: no ranking, and every result's `tier` is null.

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
    body: AlertSearchRequest,
) -> AlertSearchResponse | HTTPValidationError | None:
    """Search Alerts

     Search alerts by free text, indicator, tag or uuid.

    Exact matches (an observable value, file hash, tag or alert uuid found verbatim) are returned
    first, newest first, with tier "exact"; semantic matches over the alert's text follow. The
    ranking happens before pagination, so page one always holds the best matches.

    Args:
        body (AlertSearchRequest): Hybrid search over alerts: exact matches for the things named
            with a `field:value` term,
            plus semantic matches over the alert's text (description, comments, detections, email
            content, command lines, ...).

            Either `query` or `filters` is required. With filters and no query the response is a plain
            newest-first listing: no ranking, and every result's `tier` is null.

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
    body: AlertSearchRequest,
) -> Response[AlertSearchResponse | HTTPValidationError]:
    """Search Alerts

     Search alerts by free text, indicator, tag or uuid.

    Exact matches (an observable value, file hash, tag or alert uuid found verbatim) are returned
    first, newest first, with tier "exact"; semantic matches over the alert's text follow. The
    ranking happens before pagination, so page one always holds the best matches.

    Args:
        body (AlertSearchRequest): Hybrid search over alerts: exact matches for the things named
            with a `field:value` term,
            plus semantic matches over the alert's text (description, comments, detections, email
            content, command lines, ...).

            Either `query` or `filters` is required. With filters and no query the response is a plain
            newest-first listing: no ranking, and every result's `tier` is null.

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
    body: AlertSearchRequest,
) -> AlertSearchResponse | HTTPValidationError | None:
    """Search Alerts

     Search alerts by free text, indicator, tag or uuid.

    Exact matches (an observable value, file hash, tag or alert uuid found verbatim) are returned
    first, newest first, with tier "exact"; semantic matches over the alert's text follow. The
    ranking happens before pagination, so page one always holds the best matches.

    Args:
        body (AlertSearchRequest): Hybrid search over alerts: exact matches for the things named
            with a `field:value` term,
            plus semantic matches over the alert's text (description, comments, detections, email
            content, command lines, ...).

            Either `query` or `filters` is required. With filters and no query the response is a plain
            newest-first listing: no ranking, and every result's `tier` is null.

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
