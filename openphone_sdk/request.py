from __future__ import annotations

import os
import httpx
from openphone_client import Client

BASE_URL = os.getenv("OPENPHONE_BASE_URL", "https://api.openphone.com")
API_KEY  = os.getenv("OPENPHONE_API_KEY")
if not API_KEY:
    raise RuntimeError("Set OPENPHONE_API_KEY")

_sdk = Client(                     # the generated wrapper
    base_url=BASE_URL,
    headers={"Authorization": API_KEY},
)

def client() -> Client:            # keep for future wrappers
    return _sdk


_httpx = httpx.Client(
    base_url=BASE_URL,
    headers={"Authorization": API_KEY},
)

def httpx_client() -> httpx.Client:   # ← add
    return _httpx