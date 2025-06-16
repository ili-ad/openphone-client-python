import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_calls_v1_response_200 import ListCallsV1Response200
from ...models.list_calls_v1_response_400 import ListCallsV1Response400
from ...models.list_calls_v1_response_401 import ListCallsV1Response401
from ...models.list_calls_v1_response_403 import ListCallsV1Response403
from ...models.list_calls_v1_response_404 import ListCallsV1Response404
from ...models.list_calls_v1_response_500 import ListCallsV1Response500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    phone_number_id: str,
    user_id: Union[Unset, str] = UNSET,
    participants: list[str],
    since: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    max_results: int = 10,
    page_token: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["phoneNumberId"] = phone_number_id

    params["userId"] = user_id

    json_participants = participants

    params["participants"] = json_participants

    json_since: Union[Unset, str] = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat()
    params["since"] = json_since

    json_created_after: Union[Unset, str] = UNSET
    if not isinstance(created_after, Unset):
        json_created_after = created_after.isoformat()
    params["createdAfter"] = json_created_after

    json_created_before: Union[Unset, str] = UNSET
    if not isinstance(created_before, Unset):
        json_created_before = created_before.isoformat()
    params["createdBefore"] = json_created_before

    params["maxResults"] = max_results

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/calls",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ListCallsV1Response200,
        ListCallsV1Response400,
        ListCallsV1Response401,
        ListCallsV1Response403,
        ListCallsV1Response404,
        ListCallsV1Response500,
    ]
]:
    if response.status_code == 200:
        response_200 = ListCallsV1Response200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ListCallsV1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ListCallsV1Response401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ListCallsV1Response403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ListCallsV1Response404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ListCallsV1Response500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ListCallsV1Response200,
        ListCallsV1Response400,
        ListCallsV1Response401,
        ListCallsV1Response403,
        ListCallsV1Response404,
        ListCallsV1Response500,
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
    phone_number_id: str,
    user_id: Union[Unset, str] = UNSET,
    participants: list[str],
    since: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    max_results: int = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListCallsV1Response200,
        ListCallsV1Response400,
        ListCallsV1Response401,
        ListCallsV1Response403,
        ListCallsV1Response404,
        ListCallsV1Response500,
    ]
]:
    """List calls

     Fetch a paginated list of calls associated with a specific OpenPhone number and another number.

    Args:
        phone_number_id (str): The unique identifier of the OpenPhone number associated with the
            call.
        user_id (Union[Unset, str]): The unique identifier of the OpenPhone user who either placed
            or received the call. Defaults to the workspace owner.
        participants (list[str]): The phone numbers of participants involved in the call
            conversation, excluding your OpenPhone number. Each number should contain the country code
            and conform to the E.164 format. Currently limited to one-to-one (1:1) conversations only.
        since (Union[Unset, datetime.datetime]): DEPRECATED, use "createdAfter" or "createdBefore"
            instead. "since" incorrectly behaves as "createdBefore" and will be removed in an upcoming
            release.
        created_after (Union[Unset, datetime.datetime]): Filter results to only include calls
            created after the specified date and time, in ISO 8601 format.
        created_before (Union[Unset, datetime.datetime]): Filter results to only include calls
            created before the specified date and time, in ISO 8601 format.
        max_results (int): Maximum number of results to return per page. Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListCallsV1Response200, ListCallsV1Response400, ListCallsV1Response401, ListCallsV1Response403, ListCallsV1Response404, ListCallsV1Response500]]
    """

    kwargs = _get_kwargs(
        phone_number_id=phone_number_id,
        user_id=user_id,
        participants=participants,
        since=since,
        created_after=created_after,
        created_before=created_before,
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
    phone_number_id: str,
    user_id: Union[Unset, str] = UNSET,
    participants: list[str],
    since: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    max_results: int = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListCallsV1Response200,
        ListCallsV1Response400,
        ListCallsV1Response401,
        ListCallsV1Response403,
        ListCallsV1Response404,
        ListCallsV1Response500,
    ]
]:
    """List calls

     Fetch a paginated list of calls associated with a specific OpenPhone number and another number.

    Args:
        phone_number_id (str): The unique identifier of the OpenPhone number associated with the
            call.
        user_id (Union[Unset, str]): The unique identifier of the OpenPhone user who either placed
            or received the call. Defaults to the workspace owner.
        participants (list[str]): The phone numbers of participants involved in the call
            conversation, excluding your OpenPhone number. Each number should contain the country code
            and conform to the E.164 format. Currently limited to one-to-one (1:1) conversations only.
        since (Union[Unset, datetime.datetime]): DEPRECATED, use "createdAfter" or "createdBefore"
            instead. "since" incorrectly behaves as "createdBefore" and will be removed in an upcoming
            release.
        created_after (Union[Unset, datetime.datetime]): Filter results to only include calls
            created after the specified date and time, in ISO 8601 format.
        created_before (Union[Unset, datetime.datetime]): Filter results to only include calls
            created before the specified date and time, in ISO 8601 format.
        max_results (int): Maximum number of results to return per page. Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListCallsV1Response200, ListCallsV1Response400, ListCallsV1Response401, ListCallsV1Response403, ListCallsV1Response404, ListCallsV1Response500]
    """

    return sync_detailed(
        client=client,
        phone_number_id=phone_number_id,
        user_id=user_id,
        participants=participants,
        since=since,
        created_after=created_after,
        created_before=created_before,
        max_results=max_results,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    phone_number_id: str,
    user_id: Union[Unset, str] = UNSET,
    participants: list[str],
    since: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    max_results: int = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListCallsV1Response200,
        ListCallsV1Response400,
        ListCallsV1Response401,
        ListCallsV1Response403,
        ListCallsV1Response404,
        ListCallsV1Response500,
    ]
]:
    """List calls

     Fetch a paginated list of calls associated with a specific OpenPhone number and another number.

    Args:
        phone_number_id (str): The unique identifier of the OpenPhone number associated with the
            call.
        user_id (Union[Unset, str]): The unique identifier of the OpenPhone user who either placed
            or received the call. Defaults to the workspace owner.
        participants (list[str]): The phone numbers of participants involved in the call
            conversation, excluding your OpenPhone number. Each number should contain the country code
            and conform to the E.164 format. Currently limited to one-to-one (1:1) conversations only.
        since (Union[Unset, datetime.datetime]): DEPRECATED, use "createdAfter" or "createdBefore"
            instead. "since" incorrectly behaves as "createdBefore" and will be removed in an upcoming
            release.
        created_after (Union[Unset, datetime.datetime]): Filter results to only include calls
            created after the specified date and time, in ISO 8601 format.
        created_before (Union[Unset, datetime.datetime]): Filter results to only include calls
            created before the specified date and time, in ISO 8601 format.
        max_results (int): Maximum number of results to return per page. Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListCallsV1Response200, ListCallsV1Response400, ListCallsV1Response401, ListCallsV1Response403, ListCallsV1Response404, ListCallsV1Response500]]
    """

    kwargs = _get_kwargs(
        phone_number_id=phone_number_id,
        user_id=user_id,
        participants=participants,
        since=since,
        created_after=created_after,
        created_before=created_before,
        max_results=max_results,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    phone_number_id: str,
    user_id: Union[Unset, str] = UNSET,
    participants: list[str],
    since: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    max_results: int = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListCallsV1Response200,
        ListCallsV1Response400,
        ListCallsV1Response401,
        ListCallsV1Response403,
        ListCallsV1Response404,
        ListCallsV1Response500,
    ]
]:
    """List calls

     Fetch a paginated list of calls associated with a specific OpenPhone number and another number.

    Args:
        phone_number_id (str): The unique identifier of the OpenPhone number associated with the
            call.
        user_id (Union[Unset, str]): The unique identifier of the OpenPhone user who either placed
            or received the call. Defaults to the workspace owner.
        participants (list[str]): The phone numbers of participants involved in the call
            conversation, excluding your OpenPhone number. Each number should contain the country code
            and conform to the E.164 format. Currently limited to one-to-one (1:1) conversations only.
        since (Union[Unset, datetime.datetime]): DEPRECATED, use "createdAfter" or "createdBefore"
            instead. "since" incorrectly behaves as "createdBefore" and will be removed in an upcoming
            release.
        created_after (Union[Unset, datetime.datetime]): Filter results to only include calls
            created after the specified date and time, in ISO 8601 format.
        created_before (Union[Unset, datetime.datetime]): Filter results to only include calls
            created before the specified date and time, in ISO 8601 format.
        max_results (int): Maximum number of results to return per page. Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListCallsV1Response200, ListCallsV1Response400, ListCallsV1Response401, ListCallsV1Response403, ListCallsV1Response404, ListCallsV1Response500]
    """

    return (
        await asyncio_detailed(
            client=client,
            phone_number_id=phone_number_id,
            user_id=user_id,
            participants=participants,
            since=since,
            created_after=created_after,
            created_before=created_before,
            max_results=max_results,
            page_token=page_token,
        )
    ).parsed
