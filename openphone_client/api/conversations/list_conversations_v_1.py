import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_conversations_v1_response_200 import ListConversationsV1Response200
from ...models.list_conversations_v1_response_400 import ListConversationsV1Response400
from ...models.list_conversations_v1_response_401 import ListConversationsV1Response401
from ...models.list_conversations_v1_response_403 import ListConversationsV1Response403
from ...models.list_conversations_v1_response_404 import ListConversationsV1Response404
from ...models.list_conversations_v1_response_500 import ListConversationsV1Response500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    phone_number: Union[Unset, str] = UNSET,
    phone_numbers: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    exclude_inactive: Union[Unset, bool] = UNSET,
    updated_after: Union[Unset, datetime.datetime] = UNSET,
    updated_before: Union[Unset, datetime.datetime] = UNSET,
    max_results: int = 10,
    page_token: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_phone_number: Union[Unset, str]
    if isinstance(phone_number, Unset):
        json_phone_number = UNSET
    else:
        json_phone_number = phone_number
    params["phoneNumber"] = json_phone_number

    json_phone_numbers: Union[Unset, list[str]] = UNSET
    if not isinstance(phone_numbers, Unset):
        json_phone_numbers = []
        for phone_numbers_item_data in phone_numbers:
            phone_numbers_item: str
            phone_numbers_item = phone_numbers_item_data
            json_phone_numbers.append(phone_numbers_item)

    params["phoneNumbers"] = json_phone_numbers

    params["userId"] = user_id

    json_created_after: Union[Unset, str] = UNSET
    if not isinstance(created_after, Unset):
        json_created_after = created_after.isoformat()
    params["createdAfter"] = json_created_after

    json_created_before: Union[Unset, str] = UNSET
    if not isinstance(created_before, Unset):
        json_created_before = created_before.isoformat()
    params["createdBefore"] = json_created_before

    params["excludeInactive"] = exclude_inactive

    json_updated_after: Union[Unset, str] = UNSET
    if not isinstance(updated_after, Unset):
        json_updated_after = updated_after.isoformat()
    params["updatedAfter"] = json_updated_after

    json_updated_before: Union[Unset, str] = UNSET
    if not isinstance(updated_before, Unset):
        json_updated_before = updated_before.isoformat()
    params["updatedBefore"] = json_updated_before

    params["maxResults"] = max_results

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/conversations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ListConversationsV1Response200,
        ListConversationsV1Response400,
        ListConversationsV1Response401,
        ListConversationsV1Response403,
        ListConversationsV1Response404,
        ListConversationsV1Response500,
    ]
]:
    if response.status_code == 200:
        response_200 = ListConversationsV1Response200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ListConversationsV1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ListConversationsV1Response401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ListConversationsV1Response403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ListConversationsV1Response404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ListConversationsV1Response500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ListConversationsV1Response200,
        ListConversationsV1Response400,
        ListConversationsV1Response401,
        ListConversationsV1Response403,
        ListConversationsV1Response404,
        ListConversationsV1Response500,
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
    phone_number: Union[Unset, str] = UNSET,
    phone_numbers: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    exclude_inactive: Union[Unset, bool] = UNSET,
    updated_after: Union[Unset, datetime.datetime] = UNSET,
    updated_before: Union[Unset, datetime.datetime] = UNSET,
    max_results: int = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListConversationsV1Response200,
        ListConversationsV1Response400,
        ListConversationsV1Response401,
        ListConversationsV1Response403,
        ListConversationsV1Response404,
        ListConversationsV1Response500,
    ]
]:
    """List Conversations

     Fetch a paginated list of conversations of OpenPhone conversations. Can be filtered by user and/or
    phone numbers. Defaults to all conversations in the OpenPhone organization. Results are returned in
    descending order based on the most recent conversation.

    Args:
        phone_number (Union[Unset, str]): DEPRECATED, use `phoneNumbers` instead. If both
            `phoneNumber` and `phoneNumbers` are provided, `phoneNumbers` will be used. Filters
            results to only include conversations with the specified OpenPhone phone number. Can be
            either your OpenPhone phone number ID or the full phone number in E.164 format.
        phone_numbers (Union[Unset, list[str]]): Filters results to only include conversations
            with the specified OpenPhone phone numbers. Each item can be either an OpenPhone phone
            number ID or a full phone number in E.164 format.
        user_id (Union[Unset, str]): The unique identifier of the user the making the request.
            Used to filter results to only include the user's conversations.
        created_after (Union[Unset, datetime.datetime]): Filter results to only include
            conversations created after the specified date and time, in ISO_8601 format.
        created_before (Union[Unset, datetime.datetime]): Filter results to only include
            conversations created before the specified date and time, in ISO_8601 format.
        exclude_inactive (Union[Unset, bool]): Exclude inactive conversations from the results.
        updated_after (Union[Unset, datetime.datetime]): Filter results to only include
            conversations updated after the specified date and time, in ISO_8601 format.
        updated_before (Union[Unset, datetime.datetime]): Filter results to only include
            conversations updated before the specified date and time, in ISO_8601 format.
        max_results (int): Maximum number of results to return per page. Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListConversationsV1Response200, ListConversationsV1Response400, ListConversationsV1Response401, ListConversationsV1Response403, ListConversationsV1Response404, ListConversationsV1Response500]]
    """

    kwargs = _get_kwargs(
        phone_number=phone_number,
        phone_numbers=phone_numbers,
        user_id=user_id,
        created_after=created_after,
        created_before=created_before,
        exclude_inactive=exclude_inactive,
        updated_after=updated_after,
        updated_before=updated_before,
        max_results=max_results,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    phone_number: Union[Unset, str] = UNSET,
    phone_numbers: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    exclude_inactive: Union[Unset, bool] = UNSET,
    updated_after: Union[Unset, datetime.datetime] = UNSET,
    updated_before: Union[Unset, datetime.datetime] = UNSET,
    max_results: int = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListConversationsV1Response200,
        ListConversationsV1Response400,
        ListConversationsV1Response401,
        ListConversationsV1Response403,
        ListConversationsV1Response404,
        ListConversationsV1Response500,
    ]
]:
    """List Conversations

     Fetch a paginated list of conversations of OpenPhone conversations. Can be filtered by user and/or
    phone numbers. Defaults to all conversations in the OpenPhone organization. Results are returned in
    descending order based on the most recent conversation.

    Args:
        phone_number (Union[Unset, str]): DEPRECATED, use `phoneNumbers` instead. If both
            `phoneNumber` and `phoneNumbers` are provided, `phoneNumbers` will be used. Filters
            results to only include conversations with the specified OpenPhone phone number. Can be
            either your OpenPhone phone number ID or the full phone number in E.164 format.
        phone_numbers (Union[Unset, list[str]]): Filters results to only include conversations
            with the specified OpenPhone phone numbers. Each item can be either an OpenPhone phone
            number ID or a full phone number in E.164 format.
        user_id (Union[Unset, str]): The unique identifier of the user the making the request.
            Used to filter results to only include the user's conversations.
        created_after (Union[Unset, datetime.datetime]): Filter results to only include
            conversations created after the specified date and time, in ISO_8601 format.
        created_before (Union[Unset, datetime.datetime]): Filter results to only include
            conversations created before the specified date and time, in ISO_8601 format.
        exclude_inactive (Union[Unset, bool]): Exclude inactive conversations from the results.
        updated_after (Union[Unset, datetime.datetime]): Filter results to only include
            conversations updated after the specified date and time, in ISO_8601 format.
        updated_before (Union[Unset, datetime.datetime]): Filter results to only include
            conversations updated before the specified date and time, in ISO_8601 format.
        max_results (int): Maximum number of results to return per page. Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListConversationsV1Response200, ListConversationsV1Response400, ListConversationsV1Response401, ListConversationsV1Response403, ListConversationsV1Response404, ListConversationsV1Response500]
    """

    return sync_detailed(
        client=client,
        phone_number=phone_number,
        phone_numbers=phone_numbers,
        user_id=user_id,
        created_after=created_after,
        created_before=created_before,
        exclude_inactive=exclude_inactive,
        updated_after=updated_after,
        updated_before=updated_before,
        max_results=max_results,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    phone_number: Union[Unset, str] = UNSET,
    phone_numbers: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    exclude_inactive: Union[Unset, bool] = UNSET,
    updated_after: Union[Unset, datetime.datetime] = UNSET,
    updated_before: Union[Unset, datetime.datetime] = UNSET,
    max_results: int = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListConversationsV1Response200,
        ListConversationsV1Response400,
        ListConversationsV1Response401,
        ListConversationsV1Response403,
        ListConversationsV1Response404,
        ListConversationsV1Response500,
    ]
]:
    """List Conversations

     Fetch a paginated list of conversations of OpenPhone conversations. Can be filtered by user and/or
    phone numbers. Defaults to all conversations in the OpenPhone organization. Results are returned in
    descending order based on the most recent conversation.

    Args:
        phone_number (Union[Unset, str]): DEPRECATED, use `phoneNumbers` instead. If both
            `phoneNumber` and `phoneNumbers` are provided, `phoneNumbers` will be used. Filters
            results to only include conversations with the specified OpenPhone phone number. Can be
            either your OpenPhone phone number ID or the full phone number in E.164 format.
        phone_numbers (Union[Unset, list[str]]): Filters results to only include conversations
            with the specified OpenPhone phone numbers. Each item can be either an OpenPhone phone
            number ID or a full phone number in E.164 format.
        user_id (Union[Unset, str]): The unique identifier of the user the making the request.
            Used to filter results to only include the user's conversations.
        created_after (Union[Unset, datetime.datetime]): Filter results to only include
            conversations created after the specified date and time, in ISO_8601 format.
        created_before (Union[Unset, datetime.datetime]): Filter results to only include
            conversations created before the specified date and time, in ISO_8601 format.
        exclude_inactive (Union[Unset, bool]): Exclude inactive conversations from the results.
        updated_after (Union[Unset, datetime.datetime]): Filter results to only include
            conversations updated after the specified date and time, in ISO_8601 format.
        updated_before (Union[Unset, datetime.datetime]): Filter results to only include
            conversations updated before the specified date and time, in ISO_8601 format.
        max_results (int): Maximum number of results to return per page. Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListConversationsV1Response200, ListConversationsV1Response400, ListConversationsV1Response401, ListConversationsV1Response403, ListConversationsV1Response404, ListConversationsV1Response500]]
    """

    kwargs = _get_kwargs(
        phone_number=phone_number,
        phone_numbers=phone_numbers,
        user_id=user_id,
        created_after=created_after,
        created_before=created_before,
        exclude_inactive=exclude_inactive,
        updated_after=updated_after,
        updated_before=updated_before,
        max_results=max_results,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    phone_number: Union[Unset, str] = UNSET,
    phone_numbers: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    exclude_inactive: Union[Unset, bool] = UNSET,
    updated_after: Union[Unset, datetime.datetime] = UNSET,
    updated_before: Union[Unset, datetime.datetime] = UNSET,
    max_results: int = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListConversationsV1Response200,
        ListConversationsV1Response400,
        ListConversationsV1Response401,
        ListConversationsV1Response403,
        ListConversationsV1Response404,
        ListConversationsV1Response500,
    ]
]:
    """List Conversations

     Fetch a paginated list of conversations of OpenPhone conversations. Can be filtered by user and/or
    phone numbers. Defaults to all conversations in the OpenPhone organization. Results are returned in
    descending order based on the most recent conversation.

    Args:
        phone_number (Union[Unset, str]): DEPRECATED, use `phoneNumbers` instead. If both
            `phoneNumber` and `phoneNumbers` are provided, `phoneNumbers` will be used. Filters
            results to only include conversations with the specified OpenPhone phone number. Can be
            either your OpenPhone phone number ID or the full phone number in E.164 format.
        phone_numbers (Union[Unset, list[str]]): Filters results to only include conversations
            with the specified OpenPhone phone numbers. Each item can be either an OpenPhone phone
            number ID or a full phone number in E.164 format.
        user_id (Union[Unset, str]): The unique identifier of the user the making the request.
            Used to filter results to only include the user's conversations.
        created_after (Union[Unset, datetime.datetime]): Filter results to only include
            conversations created after the specified date and time, in ISO_8601 format.
        created_before (Union[Unset, datetime.datetime]): Filter results to only include
            conversations created before the specified date and time, in ISO_8601 format.
        exclude_inactive (Union[Unset, bool]): Exclude inactive conversations from the results.
        updated_after (Union[Unset, datetime.datetime]): Filter results to only include
            conversations updated after the specified date and time, in ISO_8601 format.
        updated_before (Union[Unset, datetime.datetime]): Filter results to only include
            conversations updated before the specified date and time, in ISO_8601 format.
        max_results (int): Maximum number of results to return per page. Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListConversationsV1Response200, ListConversationsV1Response400, ListConversationsV1Response401, ListConversationsV1Response403, ListConversationsV1Response404, ListConversationsV1Response500]
    """

    return (
        await asyncio_detailed(
            client=client,
            phone_number=phone_number,
            phone_numbers=phone_numbers,
            user_id=user_id,
            created_after=created_after,
            created_before=created_before,
            exclude_inactive=exclude_inactive,
            updated_after=updated_after,
            updated_before=updated_before,
            max_results=max_results,
            page_token=page_token,
        )
    ).parsed
