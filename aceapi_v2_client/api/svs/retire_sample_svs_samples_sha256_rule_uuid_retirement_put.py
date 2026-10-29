from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.reason_request import ReasonRequest
from ...models.retirement import Retirement
from ...types import Response


def _get_kwargs(
    sha256: str,
    rule_uuid: str,
    *,
    body: ReasonRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/svs/samples/{sha256}/{rule_uuid}/retirement".format(
            sha256=quote(str(sha256), safe=""),
            rule_uuid=quote(str(rule_uuid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Retirement | None:
    if response.status_code == 200:
        response_200 = Retirement.from_dict(response.json())

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
) -> Response[HTTPValidationError | Retirement]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sha256: str,
    rule_uuid: str,
    *,
    client: AuthenticatedClient,
    body: ReasonRequest,
) -> Response[HTTPValidationError | Retirement]:
    """Retire Sample

     Retire the sample for its rule: it is no longer expected to match, and YARA validation only
    counts it. Retiring a retired sample changes nothing.

    Args:
        sha256 (str):
        rule_uuid (str):
        body (ReasonRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Retirement]
    """

    kwargs = _get_kwargs(
        sha256=sha256,
        rule_uuid=rule_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sha256: str,
    rule_uuid: str,
    *,
    client: AuthenticatedClient,
    body: ReasonRequest,
) -> HTTPValidationError | Retirement | None:
    """Retire Sample

     Retire the sample for its rule: it is no longer expected to match, and YARA validation only
    counts it. Retiring a retired sample changes nothing.

    Args:
        sha256 (str):
        rule_uuid (str):
        body (ReasonRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Retirement
    """

    return sync_detailed(
        sha256=sha256,
        rule_uuid=rule_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    sha256: str,
    rule_uuid: str,
    *,
    client: AuthenticatedClient,
    body: ReasonRequest,
) -> Response[HTTPValidationError | Retirement]:
    """Retire Sample

     Retire the sample for its rule: it is no longer expected to match, and YARA validation only
    counts it. Retiring a retired sample changes nothing.

    Args:
        sha256 (str):
        rule_uuid (str):
        body (ReasonRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Retirement]
    """

    kwargs = _get_kwargs(
        sha256=sha256,
        rule_uuid=rule_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sha256: str,
    rule_uuid: str,
    *,
    client: AuthenticatedClient,
    body: ReasonRequest,
) -> HTTPValidationError | Retirement | None:
    """Retire Sample

     Retire the sample for its rule: it is no longer expected to match, and YARA validation only
    counts it. Retiring a retired sample changes nothing.

    Args:
        sha256 (str):
        rule_uuid (str):
        body (ReasonRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Retirement
    """

    return (
        await asyncio_detailed(
            sha256=sha256,
            rule_uuid=rule_uuid,
            client=client,
            body=body,
        )
    ).parsed
