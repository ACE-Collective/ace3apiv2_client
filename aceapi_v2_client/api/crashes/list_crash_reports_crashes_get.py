from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_response_crash_report_summary import ListResponseCrashReportSummary
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    root_uuid: None | str | Unset = UNSET,
    module: None | str | Unset = UNSET,
    crash_type: None | str | Unset = UNSET,
    node: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_root_uuid: None | str | Unset
    if isinstance(root_uuid, Unset):
        json_root_uuid = UNSET
    else:
        json_root_uuid = root_uuid
    params["root_uuid"] = json_root_uuid

    json_module: None | str | Unset
    if isinstance(module, Unset):
        json_module = UNSET
    else:
        json_module = module
    params["module"] = json_module

    json_crash_type: None | str | Unset
    if isinstance(crash_type, Unset):
        json_crash_type = UNSET
    else:
        json_crash_type = crash_type
    params["crash_type"] = json_crash_type

    json_node: None | str | Unset
    if isinstance(node, Unset):
        json_node = UNSET
    else:
        json_node = node
    params["node"] = json_node

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/crashes/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ListResponseCrashReportSummary | None:
    if response.status_code == 200:
        response_200 = ListResponseCrashReportSummary.from_dict(response.json())

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
) -> Response[HTTPValidationError | ListResponseCrashReportSummary]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    root_uuid: None | str | Unset = UNSET,
    module: None | str | Unset = UNSET,
    crash_type: None | str | Unset = UNSET,
    node: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> Response[HTTPValidationError | ListResponseCrashReportSummary]:
    """List Crash Reports

     List crash reports, newest first.

    Lists across every node, since the index is cluster-wide, but only reports with
    ``local: true`` can be downloaded from this node -- the rest live on the disk of the node
    whose worker died.

    Args:
        root_uuid (None | str | Unset): only crashes recorded while analyzing this root/alert uuid
        module (None | str | Unset): module name (email_analyzer) or module path
        crash_type (None | str | Unset): one of: exception, timeout, killed
        node (None | str | Unset): only crashes recorded on this node
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListResponseCrashReportSummary]
    """

    kwargs = _get_kwargs(
        root_uuid=root_uuid,
        module=module,
        crash_type=crash_type,
        node=node,
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
    root_uuid: None | str | Unset = UNSET,
    module: None | str | Unset = UNSET,
    crash_type: None | str | Unset = UNSET,
    node: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> HTTPValidationError | ListResponseCrashReportSummary | None:
    """List Crash Reports

     List crash reports, newest first.

    Lists across every node, since the index is cluster-wide, but only reports with
    ``local: true`` can be downloaded from this node -- the rest live on the disk of the node
    whose worker died.

    Args:
        root_uuid (None | str | Unset): only crashes recorded while analyzing this root/alert uuid
        module (None | str | Unset): module name (email_analyzer) or module path
        crash_type (None | str | Unset): one of: exception, timeout, killed
        node (None | str | Unset): only crashes recorded on this node
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListResponseCrashReportSummary
    """

    return sync_detailed(
        client=client,
        root_uuid=root_uuid,
        module=module,
        crash_type=crash_type,
        node=node,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    root_uuid: None | str | Unset = UNSET,
    module: None | str | Unset = UNSET,
    crash_type: None | str | Unset = UNSET,
    node: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> Response[HTTPValidationError | ListResponseCrashReportSummary]:
    """List Crash Reports

     List crash reports, newest first.

    Lists across every node, since the index is cluster-wide, but only reports with
    ``local: true`` can be downloaded from this node -- the rest live on the disk of the node
    whose worker died.

    Args:
        root_uuid (None | str | Unset): only crashes recorded while analyzing this root/alert uuid
        module (None | str | Unset): module name (email_analyzer) or module path
        crash_type (None | str | Unset): one of: exception, timeout, killed
        node (None | str | Unset): only crashes recorded on this node
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListResponseCrashReportSummary]
    """

    kwargs = _get_kwargs(
        root_uuid=root_uuid,
        module=module,
        crash_type=crash_type,
        node=node,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    root_uuid: None | str | Unset = UNSET,
    module: None | str | Unset = UNSET,
    crash_type: None | str | Unset = UNSET,
    node: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> HTTPValidationError | ListResponseCrashReportSummary | None:
    """List Crash Reports

     List crash reports, newest first.

    Lists across every node, since the index is cluster-wide, but only reports with
    ``local: true`` can be downloaded from this node -- the rest live on the disk of the node
    whose worker died.

    Args:
        root_uuid (None | str | Unset): only crashes recorded while analyzing this root/alert uuid
        module (None | str | Unset): module name (email_analyzer) or module path
        crash_type (None | str | Unset): one of: exception, timeout, killed
        node (None | str | Unset): only crashes recorded on this node
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListResponseCrashReportSummary
    """

    return (
        await asyncio_detailed(
            client=client,
            root_uuid=root_uuid,
            module=module,
            crash_type=crash_type,
            node=node,
            limit=limit,
            offset=offset,
        )
    ).parsed
