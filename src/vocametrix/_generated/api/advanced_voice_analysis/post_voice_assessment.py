from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_voice_assessment_body import PostVoiceAssessmentBody
from ...models.post_voice_assessment_response_200 import PostVoiceAssessmentResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostVoiceAssessmentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/voice-assessment",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostVoiceAssessmentResponse200 | None:
    if response.status_code == 200:
        response_200 = PostVoiceAssessmentResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostVoiceAssessmentResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostVoiceAssessmentBody,
) -> Response[Any | PostVoiceAssessmentResponse200]:
    """Run the full voice assessment in one call. Send the recordings as multipart/form-data: at least one
    of 'vowel' (susta…

    Args:
        body (PostVoiceAssessmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostVoiceAssessmentResponse200]
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
    body: PostVoiceAssessmentBody,
) -> Any | PostVoiceAssessmentResponse200 | None:
    """Run the full voice assessment in one call. Send the recordings as multipart/form-data: at least one
    of 'vowel' (susta…

    Args:
        body (PostVoiceAssessmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostVoiceAssessmentResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostVoiceAssessmentBody,
) -> Response[Any | PostVoiceAssessmentResponse200]:
    """Run the full voice assessment in one call. Send the recordings as multipart/form-data: at least one
    of 'vowel' (susta…

    Args:
        body (PostVoiceAssessmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostVoiceAssessmentResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostVoiceAssessmentBody,
) -> Any | PostVoiceAssessmentResponse200 | None:
    """Run the full voice assessment in one call. Send the recordings as multipart/form-data: at least one
    of 'vowel' (susta…

    Args:
        body (PostVoiceAssessmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostVoiceAssessmentResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
