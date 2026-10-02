from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    signature_uuid: str,
    *,
    version: None | str | Unset = UNSET,
    match_id: list[int] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_version: None | str | Unset
    if isinstance(version, Unset):
        json_version = UNSET
    else:
        json_version = version
    params["version"] = json_version

    json_match_id: list[int] | Unset = UNSET
    if not isinstance(match_id, Unset):
        json_match_id = match_id

    params["match_id"] = json_match_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/signatures/yara-qa/{signature_uuid}/download".format(
            signature_uuid=quote(str(signature_uuid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.content)
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
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
    version: None | str | Unset = UNSET,
    match_id: list[int] | Unset = UNSET,
) -> Response[HTTPValidationError | str]:
    """Download Signature Matches

     Download stored files of one signature, with their match records and a manifest, as one
    zip encrypted with password 'infected'.

    Without match_id, every stored file of the signature (or of one version). Limited to
    yara_qa.max_bulk_download_files files and yara_qa.max_bulk_download_bytes bytes (413 past
    either). Files stored on another node's local pool are listed in the manifest under skipped.

    Args:
        signature_uuid (str):
        version (None | str | Unset): only matches under this version of the rule
        match_id (list[int] | Unset): only these matches (repeat the parameter); every one must
            belong to this signature

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
    """

    kwargs = _get_kwargs(
        signature_uuid=signature_uuid,
        version=version,
        match_id=match_id,
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
    match_id: list[int] | Unset = UNSET,
) -> HTTPValidationError | str | None:
    """Download Signature Matches

     Download stored files of one signature, with their match records and a manifest, as one
    zip encrypted with password 'infected'.

    Without match_id, every stored file of the signature (or of one version). Limited to
    yara_qa.max_bulk_download_files files and yara_qa.max_bulk_download_bytes bytes (413 past
    either). Files stored on another node's local pool are listed in the manifest under skipped.

    Args:
        signature_uuid (str):
        version (None | str | Unset): only matches under this version of the rule
        match_id (list[int] | Unset): only these matches (repeat the parameter); every one must
            belong to this signature

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
    """

    return sync_detailed(
        signature_uuid=signature_uuid,
        client=client,
        version=version,
        match_id=match_id,
    ).parsed


async def asyncio_detailed(
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
    version: None | str | Unset = UNSET,
    match_id: list[int] | Unset = UNSET,
) -> Response[HTTPValidationError | str]:
    """Download Signature Matches

     Download stored files of one signature, with their match records and a manifest, as one
    zip encrypted with password 'infected'.

    Without match_id, every stored file of the signature (or of one version). Limited to
    yara_qa.max_bulk_download_files files and yara_qa.max_bulk_download_bytes bytes (413 past
    either). Files stored on another node's local pool are listed in the manifest under skipped.

    Args:
        signature_uuid (str):
        version (None | str | Unset): only matches under this version of the rule
        match_id (list[int] | Unset): only these matches (repeat the parameter); every one must
            belong to this signature

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
    """

    kwargs = _get_kwargs(
        signature_uuid=signature_uuid,
        version=version,
        match_id=match_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    signature_uuid: str,
    *,
    client: AuthenticatedClient,
    version: None | str | Unset = UNSET,
    match_id: list[int] | Unset = UNSET,
) -> HTTPValidationError | str | None:
    """Download Signature Matches

     Download stored files of one signature, with their match records and a manifest, as one
    zip encrypted with password 'infected'.

    Without match_id, every stored file of the signature (or of one version). Limited to
    yara_qa.max_bulk_download_files files and yara_qa.max_bulk_download_bytes bytes (413 past
    either). Files stored on another node's local pool are listed in the manifest under skipped.

    Args:
        signature_uuid (str):
        version (None | str | Unset): only matches under this version of the rule
        match_id (list[int] | Unset): only these matches (repeat the parameter); every one must
            belong to this signature

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
    """

    return (
        await asyncio_detailed(
            signature_uuid=signature_uuid,
            client=client,
            version=version,
            match_id=match_id,
        )
    ).parsed
