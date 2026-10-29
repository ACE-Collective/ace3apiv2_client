from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
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
        "url": "/svs/samples/download",
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
    *,
    client: AuthenticatedClient,
    f: list[str] | Unset = UNSET,
    tz: str | Unset = "UTC",
) -> Response[HTTPValidationError | str]:
    """Download Samples

     Download the files of every sample the filters match, with their match records and a
    manifest, as one zip encrypted with password 'infected'.

    Each file is in the zip once, whatever the number of rules it matched. Limited to
    svs.samples.max_bulk_download_files files and svs.samples.max_bulk_download_bytes bytes (413
    past either). Files stored on another node's local pool are listed in the manifest under
    skipped.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the
            samples screen's slugs: signature, rule, sha256, alert, file_name, label, label_source,
            last_captured, stored, missing_data, unknown_version, retired (see docs/SVS_API.md);
            repeat for more. Filters are ANDed, the values of one ORed.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
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
) -> HTTPValidationError | str | None:
    """Download Samples

     Download the files of every sample the filters match, with their match records and a
    manifest, as one zip encrypted with password 'infected'.

    Each file is in the zip once, whatever the number of rules it matched. Limited to
    svs.samples.max_bulk_download_files files and svs.samples.max_bulk_download_bytes bytes (413
    past either). Files stored on another node's local pool are listed in the manifest under
    skipped.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the
            samples screen's slugs: signature, rule, sha256, alert, file_name, label, label_source,
            last_captured, stored, missing_data, unknown_version, retired (see docs/SVS_API.md);
            repeat for more. Filters are ANDed, the values of one ORed.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
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
) -> Response[HTTPValidationError | str]:
    """Download Samples

     Download the files of every sample the filters match, with their match records and a
    manifest, as one zip encrypted with password 'infected'.

    Each file is in the zip once, whatever the number of rules it matched. Limited to
    svs.samples.max_bulk_download_files files and svs.samples.max_bulk_download_bytes bytes (413
    past either). Files stored on another node's local pool are listed in the manifest under
    skipped.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the
            samples screen's slugs: signature, rule, sha256, alert, file_name, label, label_source,
            last_captured, stored, missing_data, unknown_version, retired (see docs/SVS_API.md);
            repeat for more. Filters are ANDed, the values of one ORed.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
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
) -> HTTPValidationError | str | None:
    """Download Samples

     Download the files of every sample the filters match, with their match records and a
    manifest, as one zip encrypted with password 'infected'.

    Each file is in the zip once, whatever the number of rules it matched. Limited to
    svs.samples.max_bulk_download_files files and svs.samples.max_bulk_download_bytes bytes (413
    past either). Files stored on another node's local pool are listed in the manifest under
    skipped.

    Args:
        f (list[str] | Unset): a filter in the share-link encoding (`[!]slug:v1,v2`) with the
            samples screen's slugs: signature, rule, sha256, alert, file_name, label, label_source,
            last_captured, stored, missing_data, unknown_version, retired (see docs/SVS_API.md);
            repeat for more. Filters are ANDed, the values of one ORed.
        tz (str | Unset): the timezone relative date filters (`-7d`, `@d`) resolve in Default:
            'UTC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
    """

    return (
        await asyncio_detailed(
            client=client,
            f=f,
            tz=tz,
        )
    ).parsed
