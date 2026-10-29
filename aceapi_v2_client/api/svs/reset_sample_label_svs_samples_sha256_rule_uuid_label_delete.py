from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.label_action_result import LabelActionResult
from ...types import Response


def _get_kwargs(
    sha256: str,
    rule_uuid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/svs/samples/{sha256}/{rule_uuid}/label".format(
            sha256=quote(str(sha256), safe=""),
            rule_uuid=quote(str(rule_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | LabelActionResult | None:
    if response.status_code == 200:
        response_200 = LabelActionResult.from_dict(response.json())

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
) -> Response[HTTPValidationError | LabelActionResult]:
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
) -> Response[HTTPValidationError | LabelActionResult]:
    """Reset Sample Label

     Reset the sample's label to inherited: clear the explicit verdicts on its contributing
    detections, so they inherit from their alerts' dispositions again.

    Args:
        sha256 (str):
        rule_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LabelActionResult]
    """

    kwargs = _get_kwargs(
        sha256=sha256,
        rule_uuid=rule_uuid,
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
) -> HTTPValidationError | LabelActionResult | None:
    """Reset Sample Label

     Reset the sample's label to inherited: clear the explicit verdicts on its contributing
    detections, so they inherit from their alerts' dispositions again.

    Args:
        sha256 (str):
        rule_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LabelActionResult
    """

    return sync_detailed(
        sha256=sha256,
        rule_uuid=rule_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    sha256: str,
    rule_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | LabelActionResult]:
    """Reset Sample Label

     Reset the sample's label to inherited: clear the explicit verdicts on its contributing
    detections, so they inherit from their alerts' dispositions again.

    Args:
        sha256 (str):
        rule_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LabelActionResult]
    """

    kwargs = _get_kwargs(
        sha256=sha256,
        rule_uuid=rule_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sha256: str,
    rule_uuid: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | LabelActionResult | None:
    """Reset Sample Label

     Reset the sample's label to inherited: clear the explicit verdicts on its contributing
    detections, so they inherit from their alerts' dispositions again.

    Args:
        sha256 (str):
        rule_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LabelActionResult
    """

    return (
        await asyncio_detailed(
            sha256=sha256,
            rule_uuid=rule_uuid,
            client=client,
        )
    ).parsed
