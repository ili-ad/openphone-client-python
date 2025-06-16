from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_call_webhook_v1_body import CreateCallWebhookV1Body
from ...models.create_call_webhook_v1_response_201 import CreateCallWebhookV1Response201
from ...models.create_call_webhook_v1_response_400 import CreateCallWebhookV1Response400
from ...models.create_call_webhook_v1_response_401 import CreateCallWebhookV1Response401
from ...models.create_call_webhook_v1_response_403 import CreateCallWebhookV1Response403
from ...models.create_call_webhook_v1_response_404 import CreateCallWebhookV1Response404
from ...models.create_call_webhook_v1_response_500 import CreateCallWebhookV1Response500
from ...types import Response


def _get_kwargs(
    *,
    body: CreateCallWebhookV1Body,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/webhooks/calls",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        CreateCallWebhookV1Response201,
        CreateCallWebhookV1Response400,
        CreateCallWebhookV1Response401,
        CreateCallWebhookV1Response403,
        CreateCallWebhookV1Response404,
        CreateCallWebhookV1Response500,
    ]
]:
    if response.status_code == 201:
        response_201 = CreateCallWebhookV1Response201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = CreateCallWebhookV1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = CreateCallWebhookV1Response401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = CreateCallWebhookV1Response403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = CreateCallWebhookV1Response404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = CreateCallWebhookV1Response500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        CreateCallWebhookV1Response201,
        CreateCallWebhookV1Response400,
        CreateCallWebhookV1Response401,
        CreateCallWebhookV1Response403,
        CreateCallWebhookV1Response404,
        CreateCallWebhookV1Response500,
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
    body: CreateCallWebhookV1Body,
) -> Response[
    Union[
        CreateCallWebhookV1Response201,
        CreateCallWebhookV1Response400,
        CreateCallWebhookV1Response401,
        CreateCallWebhookV1Response403,
        CreateCallWebhookV1Response404,
        CreateCallWebhookV1Response500,
    ]
]:
    """Create a new webhook for calls

     Creates a new webhook that triggers on events from calls.

    Args:
        body (CreateCallWebhookV1Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateCallWebhookV1Response201, CreateCallWebhookV1Response400, CreateCallWebhookV1Response401, CreateCallWebhookV1Response403, CreateCallWebhookV1Response404, CreateCallWebhookV1Response500]]
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
    body: CreateCallWebhookV1Body,
) -> Optional[
    Union[
        CreateCallWebhookV1Response201,
        CreateCallWebhookV1Response400,
        CreateCallWebhookV1Response401,
        CreateCallWebhookV1Response403,
        CreateCallWebhookV1Response404,
        CreateCallWebhookV1Response500,
    ]
]:
    """Create a new webhook for calls

     Creates a new webhook that triggers on events from calls.

    Args:
        body (CreateCallWebhookV1Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateCallWebhookV1Response201, CreateCallWebhookV1Response400, CreateCallWebhookV1Response401, CreateCallWebhookV1Response403, CreateCallWebhookV1Response404, CreateCallWebhookV1Response500]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCallWebhookV1Body,
) -> Response[
    Union[
        CreateCallWebhookV1Response201,
        CreateCallWebhookV1Response400,
        CreateCallWebhookV1Response401,
        CreateCallWebhookV1Response403,
        CreateCallWebhookV1Response404,
        CreateCallWebhookV1Response500,
    ]
]:
    """Create a new webhook for calls

     Creates a new webhook that triggers on events from calls.

    Args:
        body (CreateCallWebhookV1Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateCallWebhookV1Response201, CreateCallWebhookV1Response400, CreateCallWebhookV1Response401, CreateCallWebhookV1Response403, CreateCallWebhookV1Response404, CreateCallWebhookV1Response500]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateCallWebhookV1Body,
) -> Optional[
    Union[
        CreateCallWebhookV1Response201,
        CreateCallWebhookV1Response400,
        CreateCallWebhookV1Response401,
        CreateCallWebhookV1Response403,
        CreateCallWebhookV1Response404,
        CreateCallWebhookV1Response500,
    ]
]:
    """Create a new webhook for calls

     Creates a new webhook that triggers on events from calls.

    Args:
        body (CreateCallWebhookV1Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateCallWebhookV1Response201, CreateCallWebhookV1Response400, CreateCallWebhookV1Response401, CreateCallWebhookV1Response403, CreateCallWebhookV1Response404, CreateCallWebhookV1Response500]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
