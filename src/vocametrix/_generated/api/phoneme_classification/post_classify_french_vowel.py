from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_classify_french_vowel_body import PostClassifyFrenchVowelBody
from ...models.post_classify_french_vowel_response_200 import PostClassifyFrenchVowelResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostClassifyFrenchVowelBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/classify-french-vowel",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostClassifyFrenchVowelResponse200 | None:
    if response.status_code == 200:
        response_200 = PostClassifyFrenchVowelResponse200.from_dict(response.json())

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
) -> Response[Any | PostClassifyFrenchVowelResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostClassifyFrenchVowelBody,
) -> Response[Any | PostClassifyFrenchVowelResponse200]:
    """Synchronous classifier for an isolated French vowel recording (11 classes: a, e, i, o, u, y, ø, ɑ̃,
    ɔ̃, ɛ, ɛ̃), built…

    Args:
        body (PostClassifyFrenchVowelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostClassifyFrenchVowelResponse200]
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
    body: PostClassifyFrenchVowelBody,
) -> Any | PostClassifyFrenchVowelResponse200 | None:
    """Synchronous classifier for an isolated French vowel recording (11 classes: a, e, i, o, u, y, ø, ɑ̃,
    ɔ̃, ɛ, ɛ̃), built…

    Args:
        body (PostClassifyFrenchVowelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostClassifyFrenchVowelResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostClassifyFrenchVowelBody,
) -> Response[Any | PostClassifyFrenchVowelResponse200]:
    """Synchronous classifier for an isolated French vowel recording (11 classes: a, e, i, o, u, y, ø, ɑ̃,
    ɔ̃, ɛ, ɛ̃), built…

    Args:
        body (PostClassifyFrenchVowelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostClassifyFrenchVowelResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostClassifyFrenchVowelBody,
) -> Any | PostClassifyFrenchVowelResponse200 | None:
    """Synchronous classifier for an isolated French vowel recording (11 classes: a, e, i, o, u, y, ø, ɑ̃,
    ɔ̃, ɛ, ɛ̃), built…

    Args:
        body (PostClassifyFrenchVowelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostClassifyFrenchVowelResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
