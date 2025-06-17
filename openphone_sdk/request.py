# openphone_sdk/request.py
from __future__ import annotations

import os
from typing import Final

from openphone_client import AuthenticatedClient

BASE: Final[str] = os.getenv("OPENPHONE_BASE_URL", "https://api.openphone.com")

_sync: AuthenticatedClient | None = None
_async: AuthenticatedClient | None = None


def _get_key() -> str:
    key = os.getenv("OPENPHONE_API_KEY", "").strip()
    if not key:
        raise RuntimeError(
            "OPENPHONE_API_KEY environment variable is required before making requests."
        )
    return key


def _sync_client() -> AuthenticatedClient:
    global _sync
    if _sync is None:
        _sync = AuthenticatedClient(
            base_url=BASE, headers={"X-API-KEY": _get_key()}, token=""
        )
    return _sync


def _async_client() -> AuthenticatedClient:
    global _async
    if _async is None:
        _async = AuthenticatedClient(
            base_url=BASE, headers={"X-API-KEY": _get_key()}, token=""
        )
    return _async


# Public helpers -------------------------------------------------------------


def client() -> AuthenticatedClient:
    """Shared synchronous client."""
    return _sync_client()


def aclient() -> AuthenticatedClient:
    """Shared asynchronous client (for upcoming async wrappers)."""
    return _async_client()
