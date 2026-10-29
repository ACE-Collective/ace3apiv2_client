from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cli_execution_create import CliExecutionCreate
from ...models.http_validation_error import HTTPValidationError
from ...models.list_response_cli_execution_read import ListResponseCliExecutionRead
from ...types import Response


def _get_kwargs(
    *,
    body: CliExecutionCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cli/executions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ListResponseCliExecutionRead | None:
    if response.status_code == 202:
        response_202 = ListResponseCliExecutionRead.from_dict(response.json())

        return response_202

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | ListResponseCliExecutionRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CliExecutionCreate,
) -> Response[HTTPValidationError | ListResponseCliExecutionRead]:
    """Create Execution

     Run `ace <command>` on each of node_ids (the primary node by default), once per node.

    Answers once every node has been asked to start, with one execution per node: a node that could
    not be asked is already failed. Follow the others with GET /cli/executions/{id}.

    Args:
        body (CliExecutionCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListResponseCliExecutionRead]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CliExecutionCreate,
) -> HTTPValidationError | ListResponseCliExecutionRead | None:
    """Create Execution

     Run `ace <command>` on each of node_ids (the primary node by default), once per node.

    Answers once every node has been asked to start, with one execution per node: a node that could
    not be asked is already failed. Follow the others with GET /cli/executions/{id}.

    Args:
        body (CliExecutionCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListResponseCliExecutionRead
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CliExecutionCreate,
) -> Response[HTTPValidationError | ListResponseCliExecutionRead]:
    """Create Execution

     Run `ace <command>` on each of node_ids (the primary node by default), once per node.

    Answers once every node has been asked to start, with one execution per node: a node that could
    not be asked is already failed. Follow the others with GET /cli/executions/{id}.

    Args:
        body (CliExecutionCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListResponseCliExecutionRead]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CliExecutionCreate,
) -> HTTPValidationError | ListResponseCliExecutionRead | None:
    """Create Execution

     Run `ace <command>` on each of node_ids (the primary node by default), once per node.

    Answers once every node has been asked to start, with one execution per node: a node that could
    not be asked is already failed. Follow the others with GET /cli/executions/{id}.

    Args:
        body (CliExecutionCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListResponseCliExecutionRead
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
