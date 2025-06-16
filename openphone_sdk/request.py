# openphone_sdk/request.py
from openphone_client import Client, AsyncClient
import os

BASE = os.getenv("OPENPHONE_BASE_URL", "https://api.openphone.com/v1")
KEY  = os.environ["OPENPHONE_API_KEY"]

_sync = Client(base_url=BASE, headers={"X-API-KEY": KEY})
_async = AsyncClient(base_url=BASE, headers={"X-API-KEY": KEY})

def client() -> Client:
    return _sync

def aclient() -> AsyncClient:
    return _async
