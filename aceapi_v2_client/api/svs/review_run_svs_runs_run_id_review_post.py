from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.review_request import ReviewRequest
from ...models.review_result import ReviewResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    run_id: str,
    *,
    body: None | ReviewRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/svs/runs/{run_id}/review".format(
            run_id=quote(str(run_id), safe=""),
        ),
    }

    if isinstance(body, ReviewRequest):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ReviewResult | None:
    if response.status_code == 200:
        response_200 = ReviewResult.from_dict(response.json())

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
) -> Response[HTTPValidationError | ReviewResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
    body: None | ReviewRequest | Unset = UNSET,
) -> Response[HTTPValidationError | ReviewResult]:
    """Review Run

     Sign the run's result off: an ended run becomes reviewed, a reviewed one is reviewed again.
    Its fully attributed open alerts become SIMULATED and its ignored detections get an FP verdict.
    Reviewing takes the run when nobody owns it. 409 with what stands in the way: another person's
    ownership (owner), the state, a stale result (stale), undecided candidates (candidates), or
    context-only alerts neither kept nor marked not a test (context_alerts).

    Args:
        run_id (str):
        body (None | ReviewRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ReviewResult]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    *,
    client: AuthenticatedClient,
    body: None | ReviewRequest | Unset = UNSET,
) -> HTTPValidationError | ReviewResult | None:
    """Review Run

     Sign the run's result off: an ended run becomes reviewed, a reviewed one is reviewed again.
    Its fully attributed open alerts become SIMULATED and its ignored detections get an FP verdict.
    Reviewing takes the run when nobody owns it. 409 with what stands in the way: another person's
    ownership (owner), the state, a stale result (stale), undecided candidates (candidates), or
    context-only alerts neither kept nor marked not a test (context_alerts).

    Args:
        run_id (str):
        body (None | ReviewRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ReviewResult
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
    body: None | ReviewRequest | Unset = UNSET,
) -> Response[HTTPValidationError | ReviewResult]:
    """Review Run

     Sign the run's result off: an ended run becomes reviewed, a reviewed one is reviewed again.
    Its fully attributed open alerts become SIMULATED and its ignored detections get an FP verdict.
    Reviewing takes the run when nobody owns it. 409 with what stands in the way: another person's
    ownership (owner), the state, a stale result (stale), undecided candidates (candidates), or
    context-only alerts neither kept nor marked not a test (context_alerts).

    Args:
        run_id (str):
        body (None | ReviewRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ReviewResult]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    *,
    client: AuthenticatedClient,
    body: None | ReviewRequest | Unset = UNSET,
) -> HTTPValidationError | ReviewResult | None:
    """Review Run

     Sign the run's result off: an ended run becomes reviewed, a reviewed one is reviewed again.
    Its fully attributed open alerts become SIMULATED and its ignored detections get an FP verdict.
    Reviewing takes the run when nobody owns it. 409 with what stands in the way: another person's
    ownership (owner), the state, a stale result (stale), undecided candidates (candidates), or
    context-only alerts neither kept nor marked not a test (context_alerts).

    Args:
        run_id (str):
        body (None | ReviewRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ReviewResult
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
            body=body,
        )
    ).parsed
