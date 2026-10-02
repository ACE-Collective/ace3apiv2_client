from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.qa_page_qa_match import QAPageQAMatch
from ...types import UNSET, Response, Unset


def _get_kwargs(
    signature_uuid: str,
    *,
    version: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_version: None | str | Unset
    if isinstance(version, Unset):
        json_version = UNSET
    else:
        json_version = version
    params["version"] = json_version

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/signatures/yara-qa/{signature_uuid}/matches".format(
            signature_uuid=quote(str(signature_uuid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | QAPageQAMatch | None:
    if response.status_code == 200:
        response_200 = QAPageQAMatch.from_dict(response.json())

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
) -> Response[HTTPValidationError | QAPageQAMatch]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
    version: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> Response[HTTPValidationError | QAPageQAMatch]:
    """List Matches

     The stored files of one signature, newest first. ``local`` says whether this node can
    serve the file.

    Args:
        signature_uuid (str):
        version (None | str | Unset): only matches under this version of the rule
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | QAPageQAMatch]
    """

    kwargs = _get_kwargs(
        signature_uuid=signature_uuid,
        version=version,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
    version: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> HTTPValidationError | QAPageQAMatch | None:
    """List Matches

     The stored files of one signature, newest first. ``local`` says whether this node can
    serve the file.

    Args:
        signature_uuid (str):
        version (None | str | Unset): only matches under this version of the rule
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | QAPageQAMatch
    """

    return sync_detailed(
        signature_uuid=signature_uuid,
        client=client,
        version=version,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
    version: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> Response[HTTPValidationError | QAPageQAMatch]:
    """List Matches

     The stored files of one signature, newest first. ``local`` says whether this node can
    serve the file.

    Args:
        signature_uuid (str):
        version (None | str | Unset): only matches under this version of the rule
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | QAPageQAMatch]
    """

    kwargs = _get_kwargs(
        signature_uuid=signature_uuid,
        version=version,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
    version: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> HTTPValidationError | QAPageQAMatch | None:
    """List Matches

     The stored files of one signature, newest first. ``local`` says whether this node can
    serve the file.

    Args:
        signature_uuid (str):
        version (None | str | Unset): only matches under this version of the rule
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | QAPageQAMatch
    """

    return (
        await asyncio_detailed(
            signature_uuid=signature_uuid,
            client=client,
            version=version,
            limit=limit,
            offset=offset,
        )
    ).parsed
