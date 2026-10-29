from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.association_request import AssociationRequest
from ...models.association_result import AssociationResult
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    run_id: str,
    alert_uuid: str,
    *,
    body: AssociationRequest | None | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/svs/runs/{run_id}/alerts/{alert_uuid}/disassociate".format(
            run_id=quote(str(run_id), safe=""),
            alert_uuid=quote(str(alert_uuid), safe=""),
        ),
    }

    if isinstance(body, AssociationRequest):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AssociationResult | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AssociationResult.from_dict(response.json())

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
) -> Response[AssociationResult | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    run_id: str,
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
    body: AssociationRequest | None | Unset = UNSET,
) -> Response[AssociationResult | HTTPValidationError]:
    """Disassociate Alert

     Remove the alert's attributions to the run, by hand; the router never attributes it to the run
    again. An alert no longer fully attributed is given back: OPEN if it was SIMULATED, and back in
    the queue SVS took it from. 409 when it isn't attributed to the run.

    Args:
        run_id (str):
        alert_uuid (str):
        body (AssociationRequest | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssociationResult | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        alert_uuid=alert_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
    body: AssociationRequest | None | Unset = UNSET,
) -> AssociationResult | HTTPValidationError | None:
    """Disassociate Alert

     Remove the alert's attributions to the run, by hand; the router never attributes it to the run
    again. An alert no longer fully attributed is given back: OPEN if it was SIMULATED, and back in
    the queue SVS took it from. 409 when it isn't attributed to the run.

    Args:
        run_id (str):
        alert_uuid (str):
        body (AssociationRequest | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssociationResult | HTTPValidationError
    """

    return sync_detailed(
        run_id=run_id,
        alert_uuid=alert_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
    body: AssociationRequest | None | Unset = UNSET,
) -> Response[AssociationResult | HTTPValidationError]:
    """Disassociate Alert

     Remove the alert's attributions to the run, by hand; the router never attributes it to the run
    again. An alert no longer fully attributed is given back: OPEN if it was SIMULATED, and back in
    the queue SVS took it from. 409 when it isn't attributed to the run.

    Args:
        run_id (str):
        alert_uuid (str):
        body (AssociationRequest | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssociationResult | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        alert_uuid=alert_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
    body: AssociationRequest | None | Unset = UNSET,
) -> AssociationResult | HTTPValidationError | None:
    """Disassociate Alert

     Remove the alert's attributions to the run, by hand; the router never attributes it to the run
    again. An alert no longer fully attributed is given back: OPEN if it was SIMULATED, and back in
    the queue SVS took it from. 409 when it isn't attributed to the run.

    Args:
        run_id (str):
        alert_uuid (str):
        body (AssociationRequest | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssociationResult | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            alert_uuid=alert_uuid,
            client=client,
            body=body,
        )
    ).parsed
