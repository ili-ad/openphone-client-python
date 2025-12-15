from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_contacts_v1_response_200 import ListContactsV1Response200
from ...models.list_contacts_v1_response_400 import ListContactsV1Response400
from ...models.list_contacts_v1_response_401 import ListContactsV1Response401
from ...models.list_contacts_v1_response_403 import ListContactsV1Response403
from ...models.list_contacts_v1_response_404 import ListContactsV1Response404
from ...models.list_contacts_v1_response_409 import ListContactsV1Response409
from ...models.list_contacts_v1_response_500 import ListContactsV1Response500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    external_ids: list[str],
    sources: Union[Unset, list[str]] = UNSET,
    max_results: int = 10,
    page_token: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_external_ids = external_ids

    params["externalIds"] = json_external_ids

    json_sources: Union[Unset, list[str]] = UNSET
    if not isinstance(sources, Unset):
        json_sources = sources

    params["sources"] = json_sources

    params["maxResults"] = max_results

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/contacts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ListContactsV1Response200,
        ListContactsV1Response400,
        ListContactsV1Response401,
        ListContactsV1Response403,
        ListContactsV1Response404,
        ListContactsV1Response409,
        ListContactsV1Response500,
    ]
]:
    if response.status_code == 200:
        response_200 = ListContactsV1Response200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ListContactsV1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ListContactsV1Response401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ListContactsV1Response403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ListContactsV1Response404.from_dict(response.json())

        return response_404
    if response.status_code == 409:
        response_409 = ListContactsV1Response409.from_dict(response.json())

        return response_409
    if response.status_code == 500:
        response_500 = ListContactsV1Response500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ListContactsV1Response200,
        ListContactsV1Response400,
        ListContactsV1Response401,
        ListContactsV1Response403,
        ListContactsV1Response404,
        ListContactsV1Response409,
        ListContactsV1Response500,
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
    external_ids: list[str],
    sources: Union[Unset, list[str]] = UNSET,
    max_results: int = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListContactsV1Response200,
        ListContactsV1Response400,
        ListContactsV1Response401,
        ListContactsV1Response403,
        ListContactsV1Response404,
        ListContactsV1Response409,
        ListContactsV1Response500,
    ]
]:
    """List contacts

     Retrieve a paginated list of contacts associated with specific external IDs. You can optionally
    filter the results further by providing a list of sources. **Note**: The `externalIds` parameter is
    currently required to specify the contacts you want to retrieve.

    Args:
        external_ids (list[str]): A list of unique identifiers from an external system used to
            retrieve specific contacts. This parameter is required and ensures the result set is
            limited to the contacts associated with the provided `externalIds`. These IDs must match
            the ones supplied during contact creation via the "Create Contacts" endpoint. Use this
            parameter to cross-reference and fetch contacts linked to external systems.
        sources (Union[Unset, list[str]]):
        max_results (int): Maximum number of results to return per page. Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListContactsV1Response200, ListContactsV1Response400, ListContactsV1Response401, ListContactsV1Response403, ListContactsV1Response404, ListContactsV1Response409, ListContactsV1Response500]]
    """

    kwargs = _get_kwargs(
        external_ids=external_ids,
        sources=sources,
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
    external_ids: list[str],
    sources: Union[Unset, list[str]] = UNSET,
    max_results: int = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListContactsV1Response200,
        ListContactsV1Response400,
        ListContactsV1Response401,
        ListContactsV1Response403,
        ListContactsV1Response404,
        ListContactsV1Response409,
        ListContactsV1Response500,
    ]
]:
    """List contacts

     Retrieve a paginated list of contacts associated with specific external IDs. You can optionally
    filter the results further by providing a list of sources. **Note**: The `externalIds` parameter is
    currently required to specify the contacts you want to retrieve.

    Args:
        external_ids (list[str]): A list of unique identifiers from an external system used to
            retrieve specific contacts. This parameter is required and ensures the result set is
            limited to the contacts associated with the provided `externalIds`. These IDs must match
            the ones supplied during contact creation via the "Create Contacts" endpoint. Use this
            parameter to cross-reference and fetch contacts linked to external systems.
        sources (Union[Unset, list[str]]):
        max_results (int): Maximum number of results to return per page. Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListContactsV1Response200, ListContactsV1Response400, ListContactsV1Response401, ListContactsV1Response403, ListContactsV1Response404, ListContactsV1Response409, ListContactsV1Response500]
    """

    return sync_detailed(
        client=client,
        external_ids=external_ids,
        sources=sources,
        max_results=max_results,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    external_ids: list[str],
    sources: Union[Unset, list[str]] = UNSET,
    max_results: int = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListContactsV1Response200,
        ListContactsV1Response400,
        ListContactsV1Response401,
        ListContactsV1Response403,
        ListContactsV1Response404,
        ListContactsV1Response409,
        ListContactsV1Response500,
    ]
]:
    """List contacts

     Retrieve a paginated list of contacts associated with specific external IDs. You can optionally
    filter the results further by providing a list of sources. **Note**: The `externalIds` parameter is
    currently required to specify the contacts you want to retrieve.

    Args:
        external_ids (list[str]): A list of unique identifiers from an external system used to
            retrieve specific contacts. This parameter is required and ensures the result set is
            limited to the contacts associated with the provided `externalIds`. These IDs must match
            the ones supplied during contact creation via the "Create Contacts" endpoint. Use this
            parameter to cross-reference and fetch contacts linked to external systems.
        sources (Union[Unset, list[str]]):
        max_results (int): Maximum number of results to return per page. Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListContactsV1Response200, ListContactsV1Response400, ListContactsV1Response401, ListContactsV1Response403, ListContactsV1Response404, ListContactsV1Response409, ListContactsV1Response500]]
    """

    kwargs = _get_kwargs(
        external_ids=external_ids,
        sources=sources,
        max_results=max_results,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    external_ids: list[str],
    sources: Union[Unset, list[str]] = UNSET,
    max_results: int = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListContactsV1Response200,
        ListContactsV1Response400,
        ListContactsV1Response401,
        ListContactsV1Response403,
        ListContactsV1Response404,
        ListContactsV1Response409,
        ListContactsV1Response500,
    ]
]:
    """List contacts

     Retrieve a paginated list of contacts associated with specific external IDs. You can optionally
    filter the results further by providing a list of sources. **Note**: The `externalIds` parameter is
    currently required to specify the contacts you want to retrieve.

    Args:
        external_ids (list[str]): A list of unique identifiers from an external system used to
            retrieve specific contacts. This parameter is required and ensures the result set is
            limited to the contacts associated with the provided `externalIds`. These IDs must match
            the ones supplied during contact creation via the "Create Contacts" endpoint. Use this
            parameter to cross-reference and fetch contacts linked to external systems.
        sources (Union[Unset, list[str]]):
        max_results (int): Maximum number of results to return per page. Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListContactsV1Response200, ListContactsV1Response400, ListContactsV1Response401, ListContactsV1Response403, ListContactsV1Response404, ListContactsV1Response409, ListContactsV1Response500]
    """

    return (
        await asyncio_detailed(
            client=client,
            external_ids=external_ids,
            sources=sources,
            max_results=max_results,
            page_token=page_token,
        )
    ).parsed
