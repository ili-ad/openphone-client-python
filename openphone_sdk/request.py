# openphone_sdk/request.py
from openphone_client import Client
import os

BASE = os.getenv("OPENPHONE_BASE_URL", "https://api.openphone.com")
KEY  = os.environ["OPENPHONE_API_KEY"]

_client = Client(base_url=BASE, headers={"X-API-KEY": KEY})

def client() -> Client:
    return _client

def aclient() -> Client:
    return _client
