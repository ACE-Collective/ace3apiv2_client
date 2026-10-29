from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_disassociation import AlertDisassociation
from ...models.alert_disassociation_request import AlertDisassociationRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    alert_uuid: str,
    *,
    body: AlertDisassociationRequest | None | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/alerts/{alert_uuid}/svs/disassociate".format(
            alert_uuid=quote(str(alert_uuid), safe=""),
        ),
    }

    if isinstance(body, AlertDisassociationRequest):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertDisassociation | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AlertDisassociation.from_dict(response.json())

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
) -> Response[AlertDisassociation | HTTPValidationError]:
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
    body: AlertDisassociationRequest | None | Unset = UNSET,
) -> Response[AlertDisassociation | HTTPValidationError]:
    """Disassociate Alert

     Disassociate the alert from every run that holds it: each run's attributions are removed by
    the caller and the router never attributes the alert to those runs again. The alert is given
    back: OPEN if it was SIMULATED, and back in the queue SVS took it from when it is OPEN and
    nobody else has taken it. 409 when no run holds it.

    Args:
        alert_uuid (str):
        body (AlertDisassociationRequest | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertDisassociation | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        alert_uuid=alert_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
    body: AlertDisassociationRequest | None | Unset = UNSET,
) -> AlertDisassociation | HTTPValidationError | None:
    """Disassociate Alert

     Disassociate the alert from every run that holds it: each run's attributions are removed by
    the caller and the router never attributes the alert to those runs again. The alert is given
    back: OPEN if it was SIMULATED, and back in the queue SVS took it from when it is OPEN and
    nobody else has taken it. 409 when no run holds it.

    Args:
        alert_uuid (str):
        body (AlertDisassociationRequest | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertDisassociation | HTTPValidationError
    """

    return sync_detailed(
        alert_uuid=alert_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
    body: AlertDisassociationRequest | None | Unset = UNSET,
) -> Response[AlertDisassociation | HTTPValidationError]:
    """Disassociate Alert

     Disassociate the alert from every run that holds it: each run's attributions are removed by
    the caller and the router never attributes the alert to those runs again. The alert is given
    back: OPEN if it was SIMULATED, and back in the queue SVS took it from when it is OPEN and
    nobody else has taken it. 409 when no run holds it.

    Args:
        alert_uuid (str):
        body (AlertDisassociationRequest | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertDisassociation | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        alert_uuid=alert_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
    body: AlertDisassociationRequest | None | Unset = UNSET,
) -> AlertDisassociation | HTTPValidationError | None:
    """Disassociate Alert

     Disassociate the alert from every run that holds it: each run's attributions are removed by
    the caller and the router never attributes the alert to those runs again. The alert is given
    back: OPEN if it was SIMULATED, and back in the queue SVS took it from when it is OPEN and
    nobody else has taken it. 409 when no run holds it.

    Args:
        alert_uuid (str):
        body (AlertDisassociationRequest | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertDisassociation | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            alert_uuid=alert_uuid,
            client=client,
            body=body,
        )
    ).parsed
