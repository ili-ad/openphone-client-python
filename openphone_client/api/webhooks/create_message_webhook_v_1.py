from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_message_webhook_v1_body import CreateMessageWebhookV1Body
from ...models.create_message_webhook_v1_response_201 import CreateMessageWebhookV1Response201
from ...models.create_message_webhook_v1_response_400 import CreateMessageWebhookV1Response400
from ...models.create_message_webhook_v1_response_401 import CreateMessageWebhookV1Response401
from ...models.create_message_webhook_v1_response_403 import CreateMessageWebhookV1Response403
from ...models.create_message_webhook_v1_response_404 import CreateMessageWebhookV1Response404
from ...models.create_message_webhook_v1_response_500 import CreateMessageWebhookV1Response500
from ...types import Response


def _get_kwargs(
    *,
    body: CreateMessageWebhookV1Body,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/webhooks/messages",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        CreateMessageWebhookV1Response201,
        CreateMessageWebhookV1Response400,
        CreateMessageWebhookV1Response401,
        CreateMessageWebhookV1Response403,
        CreateMessageWebhookV1Response404,
        CreateMessageWebhookV1Response500,
    ]
]:
    if response.status_code == 201:
        response_201 = CreateMessageWebhookV1Response201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = CreateMessageWebhookV1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = CreateMessageWebhookV1Response401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = CreateMessageWebhookV1Response403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = CreateMessageWebhookV1Response404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = CreateMessageWebhookV1Response500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        CreateMessageWebhookV1Response201,
        CreateMessageWebhookV1Response400,
        CreateMessageWebhookV1Response401,
        CreateMessageWebhookV1Response403,
        CreateMessageWebhookV1Response404,
        CreateMessageWebhookV1Response500,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateMessageWebhookV1Body,
) -> Response[
    Union[
        CreateMessageWebhookV1Response201,
        CreateMessageWebhookV1Response400,
        CreateMessageWebhookV1Response401,
        CreateMessageWebhookV1Response403,
        CreateMessageWebhookV1Response404,
        CreateMessageWebhookV1Response500,
    ]
]:
    """Create a new webhook for messages

     Creates a new webhook that triggers on events from messages.

    Args:
        body (CreateMessageWebhookV1Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateMessageWebhookV1Response201, CreateMessageWebhookV1Response400, CreateMessageWebhookV1Response401, CreateMessageWebhookV1Response403, CreateMessageWebhookV1Response404, CreateMessageWebhookV1Response500]]
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
    body: CreateMessageWebhookV1Body,
) -> Optional[
    Union[
        CreateMessageWebhookV1Response201,
        CreateMessageWebhookV1Response400,
        CreateMessageWebhookV1Response401,
        CreateMessageWebhookV1Response403,
        CreateMessageWebhookV1Response404,
        CreateMessageWebhookV1Response500,
    ]
]:
    """Create a new webhook for messages

     Creates a new webhook that triggers on events from messages.

    Args:
        body (CreateMessageWebhookV1Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateMessageWebhookV1Response201, CreateMessageWebhookV1Response400, CreateMessageWebhookV1Response401, CreateMessageWebhookV1Response403, CreateMessageWebhookV1Response404, CreateMessageWebhookV1Response500]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateMessageWebhookV1Body,
) -> Response[
    Union[
        CreateMessageWebhookV1Response201,
        CreateMessageWebhookV1Response400,
        CreateMessageWebhookV1Response401,
        CreateMessageWebhookV1Response403,
        CreateMessageWebhookV1Response404,
        CreateMessageWebhookV1Response500,
    ]
]:
    """Create a new webhook for messages

     Creates a new webhook that triggers on events from messages.

    Args:
        body (CreateMessageWebhookV1Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateMessageWebhookV1Response201, CreateMessageWebhookV1Response400, CreateMessageWebhookV1Response401, CreateMessageWebhookV1Response403, CreateMessageWebhookV1Response404, CreateMessageWebhookV1Response500]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateMessageWebhookV1Body,
) -> Optional[
    Union[
        CreateMessageWebhookV1Response201,
        CreateMessageWebhookV1Response400,
        CreateMessageWebhookV1Response401,
        CreateMessageWebhookV1Response403,
        CreateMessageWebhookV1Response404,
        CreateMessageWebhookV1Response500,
    ]
]:
    """Create a new webhook for messages

     Creates a new webhook that triggers on events from messages.

    Args:
        body (CreateMessageWebhookV1Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateMessageWebhookV1Response201, CreateMessageWebhookV1Response400, CreateMessageWebhookV1Response401, CreateMessageWebhookV1Response403, CreateMessageWebhookV1Response404, CreateMessageWebhookV1Response500]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
