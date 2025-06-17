# openphone_sdk/request.py
from __future__ import annotations

import os
from typing import Final

try:  # openphone_client may not expose AsyncClient
    from openphone_client import Client, AsyncClient  # type: ignore
except ImportError:  # pragma: no cover - fallback for older versions
    from openphone_client import Client

    AsyncClient = Client  # type: ignore[misc,assignment]


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


# Public helpers -------------------------------------------------------------


def client() -> AuthenticatedClient:
    """Shared synchronous client."""
    return _sync_client()
