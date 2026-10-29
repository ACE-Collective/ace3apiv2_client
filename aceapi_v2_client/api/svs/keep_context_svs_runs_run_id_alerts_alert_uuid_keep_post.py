from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.association_result import AssociationResult
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    run_id: str,
    alert_uuid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/svs/runs/{run_id}/alerts/{alert_uuid}/keep".format(
            run_id=quote(str(run_id), safe=""),
            alert_uuid=quote(str(alert_uuid), safe=""),
        ),
    }

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
) -> Response[AssociationResult | HTTPValidationError]:
    """Keep Context

     Confirm the alert's context attributions to the run (409 when it has none).

    Args:
        run_id (str):
        alert_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssociationResult | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        alert_uuid=alert_uuid,
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
) -> AssociationResult | HTTPValidationError | None:
    """Keep Context

     Confirm the alert's context attributions to the run (409 when it has none).

    Args:
        run_id (str):
        alert_uuid (str):

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
    ).parsed


async def asyncio_detailed(
    run_id: str,
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[AssociationResult | HTTPValidationError]:
    """Keep Context

     Confirm the alert's context attributions to the run (409 when it has none).

    Args:
        run_id (str):
        alert_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssociationResult | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        alert_uuid=alert_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
) -> AssociationResult | HTTPValidationError | None:
    """Keep Context

     Confirm the alert's context attributions to the run (409 when it has none).

    Args:
        run_id (str):
        alert_uuid (str):

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
        )
    ).parsed
