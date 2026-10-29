from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_comment_read import AlertCommentRead
from ...models.alert_comment_update import AlertCommentUpdate
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    alert_uuid: str,
    comment_id: int,
    *,
    body: AlertCommentUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/alerts/{alert_uuid}/comments/{comment_id}".format(
            alert_uuid=quote(str(alert_uuid), safe=""),
            comment_id=quote(str(comment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertCommentRead | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AlertCommentRead.from_dict(response.json())

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
) -> Response[AlertCommentRead | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alert_uuid: str,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: AlertCommentUpdate,
) -> Response[AlertCommentRead | HTTPValidationError]:
    """Update Alert Comment

     Edit the text of a comment on the alert. Only the comment's author may edit it (403).

    Args:
        alert_uuid (str):
        comment_id (int):
        body (AlertCommentUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertCommentRead | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        alert_uuid=alert_uuid,
        comment_id=comment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_uuid: str,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: AlertCommentUpdate,
) -> AlertCommentRead | HTTPValidationError | None:
    """Update Alert Comment

     Edit the text of a comment on the alert. Only the comment's author may edit it (403).

    Args:
        alert_uuid (str):
        comment_id (int):
        body (AlertCommentUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertCommentRead | HTTPValidationError
    """

    return sync_detailed(
        alert_uuid=alert_uuid,
        comment_id=comment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    alert_uuid: str,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: AlertCommentUpdate,
) -> Response[AlertCommentRead | HTTPValidationError]:
    """Update Alert Comment

     Edit the text of a comment on the alert. Only the comment's author may edit it (403).

    Args:
        alert_uuid (str):
        comment_id (int):
        body (AlertCommentUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertCommentRead | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        alert_uuid=alert_uuid,
        comment_id=comment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_uuid: str,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: AlertCommentUpdate,
) -> AlertCommentRead | HTTPValidationError | None:
    """Update Alert Comment

     Edit the text of a comment on the alert. Only the comment's author may edit it (403).

    Args:
        alert_uuid (str):
        comment_id (int):
        body (AlertCommentUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertCommentRead | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            alert_uuid=alert_uuid,
            comment_id=comment_id,
            client=client,
            body=body,
        )
    ).parsed
