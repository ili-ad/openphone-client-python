from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_webhooks_v1_response_200 import ListWebhooksV1Response200
from ...models.list_webhooks_v1_response_400 import ListWebhooksV1Response400
from ...models.list_webhooks_v1_response_401 import ListWebhooksV1Response401
from ...models.list_webhooks_v1_response_403 import ListWebhooksV1Response403
from ...models.list_webhooks_v1_response_404 import ListWebhooksV1Response404
from ...models.list_webhooks_v1_response_500 import ListWebhooksV1Response500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["userId"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/webhooks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ListWebhooksV1Response200,
        ListWebhooksV1Response400,
        ListWebhooksV1Response401,
        ListWebhooksV1Response403,
        ListWebhooksV1Response404,
        ListWebhooksV1Response500,
    ]
]:
    if response.status_code == 200:
        response_200 = ListWebhooksV1Response200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ListWebhooksV1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ListWebhooksV1Response401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ListWebhooksV1Response403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ListWebhooksV1Response404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ListWebhooksV1Response500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ListWebhooksV1Response200,
        ListWebhooksV1Response400,
        ListWebhooksV1Response401,
        ListWebhooksV1Response403,
        ListWebhooksV1Response404,
        ListWebhooksV1Response500,
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
    user_id: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListWebhooksV1Response200,
        ListWebhooksV1Response400,
        ListWebhooksV1Response401,
        ListWebhooksV1Response403,
        ListWebhooksV1Response404,
        ListWebhooksV1Response500,
    ]
]:
    """Lists all webhooks

     List all webhooks for a user.

    Args:
        user_id (Union[Unset, str]): The unique identifier the user. Defaults to the workspace
            owner.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListWebhooksV1Response200, ListWebhooksV1Response400, ListWebhooksV1Response401, ListWebhooksV1Response403, ListWebhooksV1Response404, ListWebhooksV1Response500]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListWebhooksV1Response200,
        ListWebhooksV1Response400,
        ListWebhooksV1Response401,
        ListWebhooksV1Response403,
        ListWebhooksV1Response404,
        ListWebhooksV1Response500,
    ]
]:
    """Lists all webhooks

     List all webhooks for a user.

    Args:
        user_id (Union[Unset, str]): The unique identifier the user. Defaults to the workspace
            owner.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListWebhooksV1Response200, ListWebhooksV1Response400, ListWebhooksV1Response401, ListWebhooksV1Response403, ListWebhooksV1Response404, ListWebhooksV1Response500]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListWebhooksV1Response200,
        ListWebhooksV1Response400,
        ListWebhooksV1Response401,
        ListWebhooksV1Response403,
        ListWebhooksV1Response404,
        ListWebhooksV1Response500,
    ]
]:
    """Lists all webhooks

     List all webhooks for a user.

    Args:
        user_id (Union[Unset, str]): The unique identifier the user. Defaults to the workspace
            owner.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListWebhooksV1Response200, ListWebhooksV1Response400, ListWebhooksV1Response401, ListWebhooksV1Response403, ListWebhooksV1Response404, ListWebhooksV1Response500]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListWebhooksV1Response200,
        ListWebhooksV1Response400,
        ListWebhooksV1Response401,
        ListWebhooksV1Response403,
        ListWebhooksV1Response404,
        ListWebhooksV1Response500,
    ]
]:
    """Lists all webhooks

     List all webhooks for a user.

    Args:
        user_id (Union[Unset, str]): The unique identifier the user. Defaults to the workspace
            owner.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListWebhooksV1Response200, ListWebhooksV1Response400, ListWebhooksV1Response401, ListWebhooksV1Response403, ListWebhooksV1Response404, ListWebhooksV1Response500]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
        )
    ).parsed
