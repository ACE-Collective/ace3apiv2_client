from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.qa_signature_page import QASignaturePage
from ...models.qa_sort import QASort
from ...models.qa_status import QAStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: None | str | Unset = UNSET,
    status: None | QAStatus | Unset = UNSET,
    has_matches: bool | None | Unset = UNSET,
    sort: QASort | Unset = UNSET,
    descending: bool | Unset = False,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, QAStatus):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    json_has_matches: bool | None | Unset
    if isinstance(has_matches, Unset):
        json_has_matches = UNSET
    else:
        json_has_matches = has_matches
    params["has_matches"] = json_has_matches

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["descending"] = descending

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/signatures/yara-qa/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | QASignaturePage | None:
    if response.status_code == 200:
        response_200 = QASignaturePage.from_dict(response.json())

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
) -> Response[HTTPValidationError | QASignaturePage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    status: None | QAStatus | Unset = UNSET,
    has_matches: bool | None | Unset = UNSET,
    sort: QASort | Unset = UNSET,
    descending: bool | Unset = False,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> Response[HTTPValidationError | QASignaturePage]:
    """List Signatures

     List YARA rules in QA mode, and rules with recorded QA matches, with their match counts.

    Rules in QA mode that have never matched are included, with zero counts. ``match_count``
    counts every match, including those past the file cap; ``stored_count`` counts the files kept.

    Args:
        q (None | str | Unset): substring of the rule name, uuid, namespace or file
        status (None | QAStatus | Unset): qa (in QA mode now), not_qa (left QA mode) or missing
            (no longer loaded). Omit for all
        has_matches (bool | None | Unset): only rules that have (true) or have not (false) matched
        sort (QASort | Unset):
        descending (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | QASignaturePage]
    """

    kwargs = _get_kwargs(
        q=q,
        status=status,
        has_matches=has_matches,
        sort=sort,
        descending=descending,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    status: None | QAStatus | Unset = UNSET,
    has_matches: bool | None | Unset = UNSET,
    sort: QASort | Unset = UNSET,
    descending: bool | Unset = False,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> HTTPValidationError | QASignaturePage | None:
    """List Signatures

     List YARA rules in QA mode, and rules with recorded QA matches, with their match counts.

    Rules in QA mode that have never matched are included, with zero counts. ``match_count``
    counts every match, including those past the file cap; ``stored_count`` counts the files kept.

    Args:
        q (None | str | Unset): substring of the rule name, uuid, namespace or file
        status (None | QAStatus | Unset): qa (in QA mode now), not_qa (left QA mode) or missing
            (no longer loaded). Omit for all
        has_matches (bool | None | Unset): only rules that have (true) or have not (false) matched
        sort (QASort | Unset):
        descending (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | QASignaturePage
    """

    return sync_detailed(
        client=client,
        q=q,
        status=status,
        has_matches=has_matches,
        sort=sort,
        descending=descending,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    status: None | QAStatus | Unset = UNSET,
    has_matches: bool | None | Unset = UNSET,
    sort: QASort | Unset = UNSET,
    descending: bool | Unset = False,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> Response[HTTPValidationError | QASignaturePage]:
    """List Signatures

     List YARA rules in QA mode, and rules with recorded QA matches, with their match counts.

    Rules in QA mode that have never matched are included, with zero counts. ``match_count``
    counts every match, including those past the file cap; ``stored_count`` counts the files kept.

    Args:
        q (None | str | Unset): substring of the rule name, uuid, namespace or file
        status (None | QAStatus | Unset): qa (in QA mode now), not_qa (left QA mode) or missing
            (no longer loaded). Omit for all
        has_matches (bool | None | Unset): only rules that have (true) or have not (false) matched
        sort (QASort | Unset):
        descending (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | QASignaturePage]
    """

    kwargs = _get_kwargs(
        q=q,
        status=status,
        has_matches=has_matches,
        sort=sort,
        descending=descending,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    status: None | QAStatus | Unset = UNSET,
    has_matches: bool | None | Unset = UNSET,
    sort: QASort | Unset = UNSET,
    descending: bool | Unset = False,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> HTTPValidationError | QASignaturePage | None:
    """List Signatures

     List YARA rules in QA mode, and rules with recorded QA matches, with their match counts.

    Rules in QA mode that have never matched are included, with zero counts. ``match_count``
    counts every match, including those past the file cap; ``stored_count`` counts the files kept.

    Args:
        q (None | str | Unset): substring of the rule name, uuid, namespace or file
        status (None | QAStatus | Unset): qa (in QA mode now), not_qa (left QA mode) or missing
            (no longer loaded). Omit for all
        has_matches (bool | None | Unset): only rules that have (true) or have not (false) matched
        sort (QASort | Unset):
        descending (bool | Unset):  Default: False.
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | QASignaturePage
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            status=status,
            has_matches=has_matches,
            sort=sort,
            descending=descending,
            limit=limit,
            offset=offset,
        )
    ).parsed
