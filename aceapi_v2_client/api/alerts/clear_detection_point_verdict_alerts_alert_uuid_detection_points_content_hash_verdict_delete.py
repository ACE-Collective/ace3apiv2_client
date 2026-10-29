from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.detection_point_row import DetectionPointRow
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    alert_uuid: str,
    content_hash: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/alerts/{alert_uuid}/detection-points/{content_hash}/verdict".format(
            alert_uuid=quote(str(alert_uuid), safe=""),
            content_hash=quote(str(content_hash), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DetectionPointRow | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DetectionPointRow.from_dict(response.json())

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
) -> Response[DetectionPointRow | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alert_uuid: str,
    content_hash: str,
    *,
    client: AuthenticatedClient,
) -> Response[DetectionPointRow | HTTPValidationError]:
    """Clear Detection Point Verdict

     Remove the explicit verdict on one detection, so it inherits from the alert again.

    Args:
        alert_uuid (str):
        content_hash (str): the detection's content_hash

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DetectionPointRow | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        alert_uuid=alert_uuid,
        content_hash=content_hash,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_uuid: str,
    content_hash: str,
    *,
    client: AuthenticatedClient,
) -> DetectionPointRow | HTTPValidationError | None:
    """Clear Detection Point Verdict

     Remove the explicit verdict on one detection, so it inherits from the alert again.

    Args:
        alert_uuid (str):
        content_hash (str): the detection's content_hash

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DetectionPointRow | HTTPValidationError
    """

    return sync_detailed(
        alert_uuid=alert_uuid,
        content_hash=content_hash,
        client=client,
    ).parsed


async def asyncio_detailed(
    alert_uuid: str,
    content_hash: str,
    *,
    client: AuthenticatedClient,
) -> Response[DetectionPointRow | HTTPValidationError]:
    """Clear Detection Point Verdict

     Remove the explicit verdict on one detection, so it inherits from the alert again.

    Args:
        alert_uuid (str):
        content_hash (str): the detection's content_hash

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DetectionPointRow | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        alert_uuid=alert_uuid,
        content_hash=content_hash,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_uuid: str,
    content_hash: str,
    *,
    client: AuthenticatedClient,
) -> DetectionPointRow | HTTPValidationError | None:
    """Clear Detection Point Verdict

     Remove the explicit verdict on one detection, so it inherits from the alert again.

    Args:
        alert_uuid (str):
        content_hash (str): the detection's content_hash

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DetectionPointRow | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            alert_uuid=alert_uuid,
            content_hash=content_hash,
            client=client,
        )
    ).parsed
