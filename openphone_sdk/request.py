# openphone_sdk/request.py
from __future__ import annotations

import os
from typing import Final

from openphone_client import Client

# NOTE: generated client exposes async helpers on ``Client`` itself, so
# alias ``AsyncClient`` for upcoming wrappers expecting this name.
AsyncClient = Client


from openphone_client import AuthenticatedClient


BASE: Final[str] = os.getenv("OPENPHONE_BASE_URL", "https://api.openphone.com") 

_sync: Client | None = None
_async: Client | None = None


def _get_key() -> str:
    key = os.getenv("OPENPHONE_API_KEY", "").strip()
    if not key:
        raise RuntimeError(
            "OPENPHONE_API_KEY environment variable is required before making requests."
        )
    return key


def _sync_client() -> Client:
    global _sync
    if _sync is None:
        _sync = Client(base_url=BASE, headers={"X-API-KEY": _get_key()})
    return _sync


def _async_client() -> AsyncClient:
    global _async
    if _async is None:
        _async = AsyncClient(base_url=BASE, headers={"X-API-KEY": _get_key()})
    return _async


# Public helpers -------------------------------------------------------------


def client() -> AuthenticatedClient:
    """Shared synchronous client."""
    return _sync_client()


def aclient() -> AuthenticatedClient:
    """Shared asynchronous client (for upcoming async wrappers)."""
    return _async_client()
