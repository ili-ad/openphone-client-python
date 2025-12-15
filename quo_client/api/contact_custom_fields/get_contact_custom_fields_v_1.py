from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_contact_custom_fields_v1_response_200 import GetContactCustomFieldsV1Response200
from ...models.get_contact_custom_fields_v1_response_400 import GetContactCustomFieldsV1Response400
from ...models.get_contact_custom_fields_v1_response_401 import GetContactCustomFieldsV1Response401
from ...models.get_contact_custom_fields_v1_response_403 import GetContactCustomFieldsV1Response403
from ...models.get_contact_custom_fields_v1_response_404 import GetContactCustomFieldsV1Response404
from ...models.get_contact_custom_fields_v1_response_500 import GetContactCustomFieldsV1Response500
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/contact-custom-fields",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GetContactCustomFieldsV1Response200,
        GetContactCustomFieldsV1Response400,
        GetContactCustomFieldsV1Response401,
        GetContactCustomFieldsV1Response403,
        GetContactCustomFieldsV1Response404,
        GetContactCustomFieldsV1Response500,
    ]
]:
    if response.status_code == 200:
        response_200 = GetContactCustomFieldsV1Response200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GetContactCustomFieldsV1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = GetContactCustomFieldsV1Response401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = GetContactCustomFieldsV1Response403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = GetContactCustomFieldsV1Response404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = GetContactCustomFieldsV1Response500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GetContactCustomFieldsV1Response200,
        GetContactCustomFieldsV1Response400,
        GetContactCustomFieldsV1Response401,
        GetContactCustomFieldsV1Response403,
        GetContactCustomFieldsV1Response404,
        GetContactCustomFieldsV1Response500,
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
) -> Response[
    Union[
        GetContactCustomFieldsV1Response200,
        GetContactCustomFieldsV1Response400,
        GetContactCustomFieldsV1Response401,
        GetContactCustomFieldsV1Response403,
        GetContactCustomFieldsV1Response404,
        GetContactCustomFieldsV1Response500,
    ]
]:
    """Get contact custom fields

     Custom contact fields enhance your OpenPhone contacts with additional information beyond standard
    details like name, company, role, emails and phone numbers. These user-defined fields let you
    capture business-specific data. While you can only create or modify these fields in OpenPhone
    itself, this endpoint retrieves your existing custom properties. Use this information to accurately
    map and include important custom data when creating new contacts via the API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetContactCustomFieldsV1Response200, GetContactCustomFieldsV1Response400, GetContactCustomFieldsV1Response401, GetContactCustomFieldsV1Response403, GetContactCustomFieldsV1Response404, GetContactCustomFieldsV1Response500]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        GetContactCustomFieldsV1Response200,
        GetContactCustomFieldsV1Response400,
        GetContactCustomFieldsV1Response401,
        GetContactCustomFieldsV1Response403,
        GetContactCustomFieldsV1Response404,
        GetContactCustomFieldsV1Response500,
    ]
]:
    """Get contact custom fields

     Custom contact fields enhance your OpenPhone contacts with additional information beyond standard
    details like name, company, role, emails and phone numbers. These user-defined fields let you
    capture business-specific data. While you can only create or modify these fields in OpenPhone
    itself, this endpoint retrieves your existing custom properties. Use this information to accurately
    map and include important custom data when creating new contacts via the API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetContactCustomFieldsV1Response200, GetContactCustomFieldsV1Response400, GetContactCustomFieldsV1Response401, GetContactCustomFieldsV1Response403, GetContactCustomFieldsV1Response404, GetContactCustomFieldsV1Response500]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        GetContactCustomFieldsV1Response200,
        GetContactCustomFieldsV1Response400,
        GetContactCustomFieldsV1Response401,
        GetContactCustomFieldsV1Response403,
        GetContactCustomFieldsV1Response404,
        GetContactCustomFieldsV1Response500,
    ]
]:
    """Get contact custom fields

     Custom contact fields enhance your OpenPhone contacts with additional information beyond standard
    details like name, company, role, emails and phone numbers. These user-defined fields let you
    capture business-specific data. While you can only create or modify these fields in OpenPhone
    itself, this endpoint retrieves your existing custom properties. Use this information to accurately
    map and include important custom data when creating new contacts via the API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetContactCustomFieldsV1Response200, GetContactCustomFieldsV1Response400, GetContactCustomFieldsV1Response401, GetContactCustomFieldsV1Response403, GetContactCustomFieldsV1Response404, GetContactCustomFieldsV1Response500]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        GetContactCustomFieldsV1Response200,
        GetContactCustomFieldsV1Response400,
        GetContactCustomFieldsV1Response401,
        GetContactCustomFieldsV1Response403,
        GetContactCustomFieldsV1Response404,
        GetContactCustomFieldsV1Response500,
    ]
]:
    """Get contact custom fields

     Custom contact fields enhance your OpenPhone contacts with additional information beyond standard
    details like name, company, role, emails and phone numbers. These user-defined fields let you
    capture business-specific data. While you can only create or modify these fields in OpenPhone
    itself, this endpoint retrieves your existing custom properties. Use this information to accurately
    map and include important custom data when creating new contacts via the API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetContactCustomFieldsV1Response200, GetContactCustomFieldsV1Response400, GetContactCustomFieldsV1Response401, GetContactCustomFieldsV1Response403, GetContactCustomFieldsV1Response404, GetContactCustomFieldsV1Response500]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
