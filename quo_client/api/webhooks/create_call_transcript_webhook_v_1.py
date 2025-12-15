from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_call_transcript_webhook_v1_body import CreateCallTranscriptWebhookV1Body
from ...models.create_call_transcript_webhook_v1_response_201 import CreateCallTranscriptWebhookV1Response201
from ...models.create_call_transcript_webhook_v1_response_400 import CreateCallTranscriptWebhookV1Response400
from ...models.create_call_transcript_webhook_v1_response_401 import CreateCallTranscriptWebhookV1Response401
from ...models.create_call_transcript_webhook_v1_response_403 import CreateCallTranscriptWebhookV1Response403
from ...models.create_call_transcript_webhook_v1_response_404 import CreateCallTranscriptWebhookV1Response404
from ...models.create_call_transcript_webhook_v1_response_500 import CreateCallTranscriptWebhookV1Response500
from ...types import Response


def _get_kwargs(
    *,
    body: CreateCallTranscriptWebhookV1Body,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/webhooks/call-transcripts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        CreateCallTranscriptWebhookV1Response201,
        CreateCallTranscriptWebhookV1Response400,
        CreateCallTranscriptWebhookV1Response401,
        CreateCallTranscriptWebhookV1Response403,
        CreateCallTranscriptWebhookV1Response404,
        CreateCallTranscriptWebhookV1Response500,
    ]
]:
    if response.status_code == 201:
        response_201 = CreateCallTranscriptWebhookV1Response201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = CreateCallTranscriptWebhookV1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = CreateCallTranscriptWebhookV1Response401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = CreateCallTranscriptWebhookV1Response403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = CreateCallTranscriptWebhookV1Response404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = CreateCallTranscriptWebhookV1Response500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        CreateCallTranscriptWebhookV1Response201,
        CreateCallTranscriptWebhookV1Response400,
        CreateCallTranscriptWebhookV1Response401,
        CreateCallTranscriptWebhookV1Response403,
        CreateCallTranscriptWebhookV1Response404,
        CreateCallTranscriptWebhookV1Response500,
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
    body: CreateCallTranscriptWebhookV1Body,
) -> Response[
    Union[
        CreateCallTranscriptWebhookV1Response201,
        CreateCallTranscriptWebhookV1Response400,
        CreateCallTranscriptWebhookV1Response401,
        CreateCallTranscriptWebhookV1Response403,
        CreateCallTranscriptWebhookV1Response404,
        CreateCallTranscriptWebhookV1Response500,
    ]
]:
    """Create a new webhook for call transcripts

     Creates a new webhook that triggers on events from call transcripts.

    Args:
        body (CreateCallTranscriptWebhookV1Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateCallTranscriptWebhookV1Response201, CreateCallTranscriptWebhookV1Response400, CreateCallTranscriptWebhookV1Response401, CreateCallTranscriptWebhookV1Response403, CreateCallTranscriptWebhookV1Response404, CreateCallTranscriptWebhookV1Response500]]
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
    body: CreateCallTranscriptWebhookV1Body,
) -> Optional[
    Union[
        CreateCallTranscriptWebhookV1Response201,
        CreateCallTranscriptWebhookV1Response400,
        CreateCallTranscriptWebhookV1Response401,
        CreateCallTranscriptWebhookV1Response403,
        CreateCallTranscriptWebhookV1Response404,
        CreateCallTranscriptWebhookV1Response500,
    ]
]:
    """Create a new webhook for call transcripts

     Creates a new webhook that triggers on events from call transcripts.

    Args:
        body (CreateCallTranscriptWebhookV1Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateCallTranscriptWebhookV1Response201, CreateCallTranscriptWebhookV1Response400, CreateCallTranscriptWebhookV1Response401, CreateCallTranscriptWebhookV1Response403, CreateCallTranscriptWebhookV1Response404, CreateCallTranscriptWebhookV1Response500]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCallTranscriptWebhookV1Body,
) -> Response[
    Union[
        CreateCallTranscriptWebhookV1Response201,
        CreateCallTranscriptWebhookV1Response400,
        CreateCallTranscriptWebhookV1Response401,
        CreateCallTranscriptWebhookV1Response403,
        CreateCallTranscriptWebhookV1Response404,
        CreateCallTranscriptWebhookV1Response500,
    ]
]:
    """Create a new webhook for call transcripts

     Creates a new webhook that triggers on events from call transcripts.

    Args:
        body (CreateCallTranscriptWebhookV1Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateCallTranscriptWebhookV1Response201, CreateCallTranscriptWebhookV1Response400, CreateCallTranscriptWebhookV1Response401, CreateCallTranscriptWebhookV1Response403, CreateCallTranscriptWebhookV1Response404, CreateCallTranscriptWebhookV1Response500]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateCallTranscriptWebhookV1Body,
) -> Optional[
    Union[
        CreateCallTranscriptWebhookV1Response201,
        CreateCallTranscriptWebhookV1Response400,
        CreateCallTranscriptWebhookV1Response401,
        CreateCallTranscriptWebhookV1Response403,
        CreateCallTranscriptWebhookV1Response404,
        CreateCallTranscriptWebhookV1Response500,
    ]
]:
    """Create a new webhook for call transcripts

     Creates a new webhook that triggers on events from call transcripts.

    Args:
        body (CreateCallTranscriptWebhookV1Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateCallTranscriptWebhookV1Response201, CreateCallTranscriptWebhookV1Response400, CreateCallTranscriptWebhookV1Response401, CreateCallTranscriptWebhookV1Response403, CreateCallTranscriptWebhookV1Response404, CreateCallTranscriptWebhookV1Response500]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
