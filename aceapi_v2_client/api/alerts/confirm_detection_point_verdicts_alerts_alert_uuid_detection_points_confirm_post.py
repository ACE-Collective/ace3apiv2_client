from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.confirm_result import ConfirmResult
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    alert_uuid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/alerts/{alert_uuid}/detection-points/confirm".format(
            alert_uuid=quote(str(alert_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConfirmResult | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ConfirmResult.from_dict(response.json())

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
) -> Response[ConfirmResult | HTTPValidationError]:
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
) -> Response[ConfirmResult | HTTPValidationError]:
    """Confirm Detection Point Verdicts

     Confirm every unconfirmed inherited TP on the alert (source inherited_multi): each becomes
    an explicit TP, which weighs more when signature changes are tested.

    Args:
        alert_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmResult | HTTPValidationError]
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
) -> ConfirmResult | HTTPValidationError | None:
    """Confirm Detection Point Verdicts

     Confirm every unconfirmed inherited TP on the alert (source inherited_multi): each becomes
    an explicit TP, which weighs more when signature changes are tested.

    Args:
        alert_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfirmResult | HTTPValidationError
    """

    return sync_detailed(
        alert_uuid=alert_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    alert_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ConfirmResult | HTTPValidationError]:
    """Confirm Detection Point Verdicts

     Confirm every unconfirmed inherited TP on the alert (source inherited_multi): each becomes
    an explicit TP, which weighs more when signature changes are tested.

    Args:
        alert_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmResult | HTTPValidationError]
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
) -> ConfirmResult | HTTPValidationError | None:
    """Confirm Detection Point Verdicts

     Confirm every unconfirmed inherited TP on the alert (source inherited_multi): each becomes
    an explicit TP, which weighs more when signature changes are tested.

    Args:
        alert_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfirmResult | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            alert_uuid=alert_uuid,
            client=client,
        )
    ).parsed
