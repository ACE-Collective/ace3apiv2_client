from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.coverage_summary import CoverageSummary
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    f: list[str] | Unset = UNSET,
    tz: str | Unset = "UTC",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_f: list[str] | Unset = UNSET
    if not isinstance(f, Unset):
        json_f = f

    params["f"] = json_f

    params["tz"] = tz

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/svs/coverage/summary",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CoverageSummary | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CoverageSummary.from_dict(response.json())

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
) -> Response[CoverageSummary | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
    tz: str | Unset = "UTC",
) -> Response[CoverageSummary | HTTPValidationError]:
    """Get Summary

     The rows the filters match, counted per state and per own state, overall and per platform, with
    what the last refresh did.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the
            coverage screen's slugs: technique (T1059 also finds its sub-techniques), name, tactic (an
            id or a shortname), platform, state, own_state, level, attack_platform, catalog_status,
            has_manual, state_changed, retired (see docs/SVS_API.md); repeat for more. Filters are
            ANDed, the values of one ORed.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CoverageSummary | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        f=f,
        tz=tz,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
    tz: str | Unset = "UTC",
) -> CoverageSummary | HTTPValidationError | None:
    """Get Summary

     The rows the filters match, counted per state and per own state, overall and per platform, with
    what the last refresh did.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the
            coverage screen's slugs: technique (T1059 also finds its sub-techniques), name, tactic (an
            id or a shortname), platform, state, own_state, level, attack_platform, catalog_status,
            has_manual, state_changed, retired (see docs/SVS_API.md); repeat for more. Filters are
            ANDed, the values of one ORed.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CoverageSummary | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        f=f,
        tz=tz,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
    tz: str | Unset = "UTC",
) -> Response[CoverageSummary | HTTPValidationError]:
    """Get Summary

     The rows the filters match, counted per state and per own state, overall and per platform, with
    what the last refresh did.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the
            coverage screen's slugs: technique (T1059 also finds its sub-techniques), name, tactic (an
            id or a shortname), platform, state, own_state, level, attack_platform, catalog_status,
            has_manual, state_changed, retired (see docs/SVS_API.md); repeat for more. Filters are
            ANDed, the values of one ORed.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CoverageSummary | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        f=f,
        tz=tz,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
    tz: str | Unset = "UTC",
) -> CoverageSummary | HTTPValidationError | None:
    """Get Summary

     The rows the filters match, counted per state and per own state, overall and per platform, with
    what the last refresh did.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the
            coverage screen's slugs: technique (T1059 also finds its sub-techniques), name, tactic (an
            id or a shortname), platform, state, own_state, level, attack_platform, catalog_status,
            has_manual, state_changed, retired (see docs/SVS_API.md); repeat for more. Filters are
            ANDed, the values of one ORed.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CoverageSummary | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            f=f,
            tz=tz,
        )
    ).parsed
