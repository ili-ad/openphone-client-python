from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.send_message_v1_body import SendMessageV1Body
from ...models.send_message_v1_response_202 import SendMessageV1Response202
from ...models.send_message_v1_response_400 import SendMessageV1Response400
from ...models.send_message_v1_response_401 import SendMessageV1Response401
from ...models.send_message_v1_response_402 import SendMessageV1Response402
from ...models.send_message_v1_response_403 import SendMessageV1Response403
from ...models.send_message_v1_response_404 import SendMessageV1Response404
from ...models.send_message_v1_response_500 import SendMessageV1Response500
from ...types import Response


def _get_kwargs(
    *,
    body: SendMessageV1Body,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/messages",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        SendMessageV1Response202,
        SendMessageV1Response400,
        SendMessageV1Response401,
        SendMessageV1Response402,
        SendMessageV1Response403,
        SendMessageV1Response404,
        SendMessageV1Response500,
    ]
]:
    if response.status_code == 202:
        response_202 = SendMessageV1Response202.from_dict(response.json())

        return response_202
    if response.status_code == 400:
        response_400 = SendMessageV1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = SendMessageV1Response401.from_dict(response.json())

        return response_401
    if response.status_code == 402:
        response_402 = SendMessageV1Response402.from_dict(response.json())

        return response_402
    if response.status_code == 403:
        response_403 = SendMessageV1Response403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = SendMessageV1Response404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = SendMessageV1Response500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        SendMessageV1Response202,
        SendMessageV1Response400,
        SendMessageV1Response401,
        SendMessageV1Response402,
        SendMessageV1Response403,
        SendMessageV1Response404,
        SendMessageV1Response500,
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
    body: SendMessageV1Body,
) -> Response[
    Union[
        SendMessageV1Response202,
        SendMessageV1Response400,
        SendMessageV1Response401,
        SendMessageV1Response402,
        SendMessageV1Response403,
        SendMessageV1Response404,
        SendMessageV1Response500,
    ]
]:
    """Send a text message

     Send a text message from your OpenPhone number to a recipient.

    Args:
        body (SendMessageV1Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SendMessageV1Response202, SendMessageV1Response400, SendMessageV1Response401, SendMessageV1Response402, SendMessageV1Response403, SendMessageV1Response404, SendMessageV1Response500]]
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
    body: SendMessageV1Body,
) -> Optional[
    Union[
        SendMessageV1Response202,
        SendMessageV1Response400,
        SendMessageV1Response401,
        SendMessageV1Response402,
        SendMessageV1Response403,
        SendMessageV1Response404,
        SendMessageV1Response500,
    ]
]:
    """Send a text message

     Send a text message from your OpenPhone number to a recipient.

    Args:
        body (SendMessageV1Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SendMessageV1Response202, SendMessageV1Response400, SendMessageV1Response401, SendMessageV1Response402, SendMessageV1Response403, SendMessageV1Response404, SendMessageV1Response500]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SendMessageV1Body,
) -> Response[
    Union[
        SendMessageV1Response202,
        SendMessageV1Response400,
        SendMessageV1Response401,
        SendMessageV1Response402,
        SendMessageV1Response403,
        SendMessageV1Response404,
        SendMessageV1Response500,
    ]
]:
    """Send a text message

     Send a text message from your OpenPhone number to a recipient.

    Args:
        body (SendMessageV1Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SendMessageV1Response202, SendMessageV1Response400, SendMessageV1Response401, SendMessageV1Response402, SendMessageV1Response403, SendMessageV1Response404, SendMessageV1Response500]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SendMessageV1Body,
) -> Optional[
    Union[
        SendMessageV1Response202,
        SendMessageV1Response400,
        SendMessageV1Response401,
        SendMessageV1Response402,
        SendMessageV1Response403,
        SendMessageV1Response404,
        SendMessageV1Response500,
    ]
]:
    """Send a text message

     Send a text message from your OpenPhone number to a recipient.

    Args:
        body (SendMessageV1Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SendMessageV1Response202, SendMessageV1Response400, SendMessageV1Response401, SendMessageV1Response402, SendMessageV1Response403, SendMessageV1Response404, SendMessageV1Response500]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
