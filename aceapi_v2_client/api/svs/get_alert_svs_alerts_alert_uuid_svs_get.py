from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_svs import AlertSVS
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    alert_uuid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/alerts/{alert_uuid}/svs".format(
            alert_uuid=quote(str(alert_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertSVS | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AlertSVS.from_dict(response.json())

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
) -> Response[AlertSVS | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[AlertSVS | HTTPValidationError]:
    """Get Alert Svs

     The alert's SVS status, the runs it is attributed to, which of its detections each holds,
    and the markers in it that disagree with their run. 404 for an unknown alert.

    Args:
        alert_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertSVS | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        alert_uuid=alert_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
) -> AlertSVS | HTTPValidationError | None:
    """Get Alert Svs

     The alert's SVS status, the runs it is attributed to, which of its detections each holds,
    and the markers in it that disagree with their run. 404 for an unknown alert.

    Args:
        alert_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertSVS | HTTPValidationError
    """

    return sync_detailed(
        alert_uuid=alert_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[AlertSVS | HTTPValidationError]:
    """Get Alert Svs

     The alert's SVS status, the runs it is attributed to, which of its detections each holds,
    and the markers in it that disagree with their run. 404 for an unknown alert.

    Args:
        alert_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertSVS | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        alert_uuid=alert_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
) -> AlertSVS | HTTPValidationError | None:
    """Get Alert Svs

     The alert's SVS status, the runs it is attributed to, which of its detections each holds,
    and the markers in it that disagree with their run. 404 for an unknown alert.

    Args:
        alert_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertSVS | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            alert_uuid=alert_uuid,
            client=client,
        )
    ).parsed
