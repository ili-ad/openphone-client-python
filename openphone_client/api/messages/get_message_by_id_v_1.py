from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_message_by_id_v1_response_200 import GetMessageByIdV1Response200
from ...models.get_message_by_id_v1_response_400 import GetMessageByIdV1Response400
from ...models.get_message_by_id_v1_response_401 import GetMessageByIdV1Response401
from ...models.get_message_by_id_v1_response_402 import GetMessageByIdV1Response402
from ...models.get_message_by_id_v1_response_403 import GetMessageByIdV1Response403
from ...models.get_message_by_id_v1_response_404 import GetMessageByIdV1Response404
from ...models.get_message_by_id_v1_response_500 import GetMessageByIdV1Response500
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/messages/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GetMessageByIdV1Response200,
        GetMessageByIdV1Response400,
        GetMessageByIdV1Response401,
        GetMessageByIdV1Response402,
        GetMessageByIdV1Response403,
        GetMessageByIdV1Response404,
        GetMessageByIdV1Response500,
    ]
]:
    if response.status_code == 200:
        response_200 = GetMessageByIdV1Response200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GetMessageByIdV1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = GetMessageByIdV1Response401.from_dict(response.json())

        return response_401
    if response.status_code == 402:
        response_402 = GetMessageByIdV1Response402.from_dict(response.json())

        return response_402
    if response.status_code == 403:
        response_403 = GetMessageByIdV1Response403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = GetMessageByIdV1Response404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = GetMessageByIdV1Response500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GetMessageByIdV1Response200,
        GetMessageByIdV1Response400,
        GetMessageByIdV1Response401,
        GetMessageByIdV1Response402,
        GetMessageByIdV1Response403,
        GetMessageByIdV1Response404,
        GetMessageByIdV1Response500,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        GetMessageByIdV1Response200,
        GetMessageByIdV1Response400,
        GetMessageByIdV1Response401,
        GetMessageByIdV1Response402,
        GetMessageByIdV1Response403,
        GetMessageByIdV1Response404,
        GetMessageByIdV1Response500,
    ]
]:
    """Get a message by ID

     Get a message by its unique identifier.

    Args:
        id (str): The unique identifier of a message

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetMessageByIdV1Response200, GetMessageByIdV1Response400, GetMessageByIdV1Response401, GetMessageByIdV1Response402, GetMessageByIdV1Response403, GetMessageByIdV1Response404, GetMessageByIdV1Response500]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        GetMessageByIdV1Response200,
        GetMessageByIdV1Response400,
        GetMessageByIdV1Response401,
        GetMessageByIdV1Response402,
        GetMessageByIdV1Response403,
        GetMessageByIdV1Response404,
        GetMessageByIdV1Response500,
    ]
]:
    """Get a message by ID

     Get a message by its unique identifier.

    Args:
        id (str): The unique identifier of a message

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetMessageByIdV1Response200, GetMessageByIdV1Response400, GetMessageByIdV1Response401, GetMessageByIdV1Response402, GetMessageByIdV1Response403, GetMessageByIdV1Response404, GetMessageByIdV1Response500]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        GetMessageByIdV1Response200,
        GetMessageByIdV1Response400,
        GetMessageByIdV1Response401,
        GetMessageByIdV1Response402,
        GetMessageByIdV1Response403,
        GetMessageByIdV1Response404,
        GetMessageByIdV1Response500,
    ]
]:
    """Get a message by ID

     Get a message by its unique identifier.

    Args:
        id (str): The unique identifier of a message

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetMessageByIdV1Response200, GetMessageByIdV1Response400, GetMessageByIdV1Response401, GetMessageByIdV1Response402, GetMessageByIdV1Response403, GetMessageByIdV1Response404, GetMessageByIdV1Response500]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        GetMessageByIdV1Response200,
        GetMessageByIdV1Response400,
        GetMessageByIdV1Response401,
        GetMessageByIdV1Response402,
        GetMessageByIdV1Response403,
        GetMessageByIdV1Response404,
        GetMessageByIdV1Response500,
    ]
]:
    """Get a message by ID

     Get a message by its unique identifier.

    Args:
        id (str): The unique identifier of a message

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetMessageByIdV1Response200, GetMessageByIdV1Response400, GetMessageByIdV1Response401, GetMessageByIdV1Response402, GetMessageByIdV1Response403, GetMessageByIdV1Response404, GetMessageByIdV1Response500]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
