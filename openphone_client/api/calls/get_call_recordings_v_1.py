from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_call_recordings_v1_response_200 import GetCallRecordingsV1Response200
from ...models.get_call_recordings_v1_response_400 import GetCallRecordingsV1Response400
from ...models.get_call_recordings_v1_response_401 import GetCallRecordingsV1Response401
from ...models.get_call_recordings_v1_response_403 import GetCallRecordingsV1Response403
from ...models.get_call_recordings_v1_response_404 import GetCallRecordingsV1Response404
from ...models.get_call_recordings_v1_response_500 import GetCallRecordingsV1Response500
from ...types import Response


def _get_kwargs(
    call_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/call-recordings/{call_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GetCallRecordingsV1Response200,
        GetCallRecordingsV1Response400,
        GetCallRecordingsV1Response401,
        GetCallRecordingsV1Response403,
        GetCallRecordingsV1Response404,
        GetCallRecordingsV1Response500,
    ]
]:
    if response.status_code == 200:
        response_200 = GetCallRecordingsV1Response200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GetCallRecordingsV1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = GetCallRecordingsV1Response401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = GetCallRecordingsV1Response403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = GetCallRecordingsV1Response404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = GetCallRecordingsV1Response500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GetCallRecordingsV1Response200,
        GetCallRecordingsV1Response400,
        GetCallRecordingsV1Response401,
        GetCallRecordingsV1Response403,
        GetCallRecordingsV1Response404,
        GetCallRecordingsV1Response500,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    call_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        GetCallRecordingsV1Response200,
        GetCallRecordingsV1Response400,
        GetCallRecordingsV1Response401,
        GetCallRecordingsV1Response403,
        GetCallRecordingsV1Response404,
        GetCallRecordingsV1Response500,
    ]
]:
    """Get recordings for a call

     Retrieve a list of recordings associated with a specific call. The results are sorted
    chronologically, with the oldest recording segment appearing first in the list.

    Args:
        call_id (str): The unique identifier of the call for which recordings are being retrieved.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetCallRecordingsV1Response200, GetCallRecordingsV1Response400, GetCallRecordingsV1Response401, GetCallRecordingsV1Response403, GetCallRecordingsV1Response404, GetCallRecordingsV1Response500]]
    """

    kwargs = _get_kwargs(
        call_id=call_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    call_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        GetCallRecordingsV1Response200,
        GetCallRecordingsV1Response400,
        GetCallRecordingsV1Response401,
        GetCallRecordingsV1Response403,
        GetCallRecordingsV1Response404,
        GetCallRecordingsV1Response500,
    ]
]:
    """Get recordings for a call

     Retrieve a list of recordings associated with a specific call. The results are sorted
    chronologically, with the oldest recording segment appearing first in the list.

    Args:
        call_id (str): The unique identifier of the call for which recordings are being retrieved.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetCallRecordingsV1Response200, GetCallRecordingsV1Response400, GetCallRecordingsV1Response401, GetCallRecordingsV1Response403, GetCallRecordingsV1Response404, GetCallRecordingsV1Response500]
    """

    return sync_detailed(
        call_id=call_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    call_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        GetCallRecordingsV1Response200,
        GetCallRecordingsV1Response400,
        GetCallRecordingsV1Response401,
        GetCallRecordingsV1Response403,
        GetCallRecordingsV1Response404,
        GetCallRecordingsV1Response500,
    ]
]:
    """Get recordings for a call

     Retrieve a list of recordings associated with a specific call. The results are sorted
    chronologically, with the oldest recording segment appearing first in the list.

    Args:
        call_id (str): The unique identifier of the call for which recordings are being retrieved.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetCallRecordingsV1Response200, GetCallRecordingsV1Response400, GetCallRecordingsV1Response401, GetCallRecordingsV1Response403, GetCallRecordingsV1Response404, GetCallRecordingsV1Response500]]
    """

    kwargs = _get_kwargs(
        call_id=call_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    call_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        GetCallRecordingsV1Response200,
        GetCallRecordingsV1Response400,
        GetCallRecordingsV1Response401,
        GetCallRecordingsV1Response403,
        GetCallRecordingsV1Response404,
        GetCallRecordingsV1Response500,
    ]
]:
    """Get recordings for a call

     Retrieve a list of recordings associated with a specific call. The results are sorted
    chronologically, with the oldest recording segment appearing first in the list.

    Args:
        call_id (str): The unique identifier of the call for which recordings are being retrieved.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetCallRecordingsV1Response200, GetCallRecordingsV1Response400, GetCallRecordingsV1Response401, GetCallRecordingsV1Response403, GetCallRecordingsV1Response404, GetCallRecordingsV1Response500]
    """

    return (
        await asyncio_detailed(
            call_id=call_id,
            client=client,
        )
    ).parsed
