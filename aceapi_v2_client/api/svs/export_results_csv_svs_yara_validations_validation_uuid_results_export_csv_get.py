from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    validation_uuid: str,
    *,
    category: list[str] | Unset = UNSET,
    rule_uuid: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_category: list[str] | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = category

    params["category"] = json_category

    json_rule_uuid: list[str] | Unset = UNSET
    if not isinstance(rule_uuid, Unset):
        json_rule_uuid = rule_uuid

    params["rule_uuid"] = json_rule_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/svs/yara/validations/{validation_uuid}/results/export/csv".format(
            validation_uuid=quote(str(validation_uuid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | str | None:
    if response.status_code == 200:
        response_200 = response.text
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
) -> Response[HTTPValidationError | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    validation_uuid: str,
    *,
    client: AuthenticatedClient,
    category: list[str] | Unset = UNSET,
    rule_uuid: list[str] | Unset = UNSET,
) -> Response[HTTPValidationError | str]:
    """Export Results Csv

     Stream the selected rows as CSV.

    Args:
        validation_uuid (str):
        category (list[str] | Unset): only rows of these categories (repeat for more)
        rule_uuid (list[str] | Unset): only rows of these rule uuids (repeat for more)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
    """

    kwargs = _get_kwargs(
        validation_uuid=validation_uuid,
        category=category,
        rule_uuid=rule_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    validation_uuid: str,
    *,
    client: AuthenticatedClient,
    category: list[str] | Unset = UNSET,
    rule_uuid: list[str] | Unset = UNSET,
) -> HTTPValidationError | str | None:
    """Export Results Csv

     Stream the selected rows as CSV.

    Args:
        validation_uuid (str):
        category (list[str] | Unset): only rows of these categories (repeat for more)
        rule_uuid (list[str] | Unset): only rows of these rule uuids (repeat for more)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
    """

    return sync_detailed(
        validation_uuid=validation_uuid,
        client=client,
        category=category,
        rule_uuid=rule_uuid,
    ).parsed


async def asyncio_detailed(
    validation_uuid: str,
    *,
    client: AuthenticatedClient,
    category: list[str] | Unset = UNSET,
    rule_uuid: list[str] | Unset = UNSET,
) -> Response[HTTPValidationError | str]:
    """Export Results Csv

     Stream the selected rows as CSV.

    Args:
        validation_uuid (str):
        category (list[str] | Unset): only rows of these categories (repeat for more)
        rule_uuid (list[str] | Unset): only rows of these rule uuids (repeat for more)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
    """

    kwargs = _get_kwargs(
        validation_uuid=validation_uuid,
        category=category,
        rule_uuid=rule_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    validation_uuid: str,
    *,
    client: AuthenticatedClient,
    category: list[str] | Unset = UNSET,
    rule_uuid: list[str] | Unset = UNSET,
) -> HTTPValidationError | str | None:
    """Export Results Csv

     Stream the selected rows as CSV.

    Args:
        validation_uuid (str):
        category (list[str] | Unset): only rows of these categories (repeat for more)
        rule_uuid (list[str] | Unset): only rows of these rule uuids (repeat for more)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
    """

    return (
        await asyncio_detailed(
            validation_uuid=validation_uuid,
            client=client,
            category=category,
            rule_uuid=rule_uuid,
        )
    ).parsed
