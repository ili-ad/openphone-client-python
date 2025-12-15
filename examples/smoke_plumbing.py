"""
Read-only sanity checks against the live OpenPhone API.
Requires QUO_API_KEY (or OPENPHONE_API_KEY) to be set.
Nothing here sends a message or generates carrier fees.
"""

from __future__ import annotations

import os
import pprint
from datetime import datetime, timedelta, timezone

import httpx
from quo_sdk.request import httpx_client

# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #


def _hr(label: str) -> None:
    print(f"\n{'=' * 8} {label} {'=' * 8}")


def _when(iso: str | None) -> str:
    if not iso:
        return "-"
    dt = datetime.fromisoformat(iso.rstrip("Z")).replace(tzinfo=timezone.utc)
    return dt.astimezone().strftime("%Y-%m-%d %H:%M")


# --------------------------------------------------------------------------- #
# 0) show the key prefix so we’re certain the env is picked up
# --------------------------------------------------------------------------- #

key = os.getenv("QUO_API_KEY") or os.getenv("OPENPHONE_API_KEY")
print("⟹ using key :", (key[:8] + "…") if key else None)

# --------------------------------------------------------------------------- #
# 1) list phone numbers
# --------------------------------------------------------------------------- #

http = httpx_client()  # thin wrapper around httpx.Client with auth header
_hr("phone numbers")
resp = http.get("/v1/phone-numbers")
resp.raise_for_status()

first_num = resp.json()["data"][0]
PHONE_ID   = first_num["id"]
E164       = first_num["number"]          #  ←  "+17183601600"

print(f"{PHONE_ID} • {first_num['formattedNumber']} • {_when(first_num['createdAt'])}")
# --------------------------------------------------------------------------- #
# 2) recent calls (last 30 days) – need BOTH start *and* end
# --------------------------------------------------------------------------- #

_hr("recent calls (last 30 days)")
now   = datetime.now(timezone.utc)
since = (now - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
until =  now.strftime("%Y-%m-%dT%H:%M:%SZ")

resp = http.get(
    "/v1/calls",
    params={
        "phoneNumberId": PHONE_ID,
        "participants":  [E164],   # 👈 required
        "timeRangeStart": since,
        "timeRangeEnd":   until,
        "maxResults":     5,
    },
)

if resp.is_error:
    print("⇡ 400-payload →", resp.status_code, resp.text)  # keep for any future tweaks
resp.raise_for_status()
for c in resp.json()["data"]:
    print(f"{c['id']} • dir={c['direction']} • {_when(c['startTime'])}")
CALL_ID = resp.json()["data"][0]["id"] if resp.json()["data"] else None


# --------------------------------------------------------------------------- #
# 3) recordings for the newest call (if any)
# --------------------------------------------------------------------------- #

if CALL_ID:
    _hr(f"recordings for {CALL_ID}")
    r = http.get(f"/v1/call-recordings/{CALL_ID}")
    r.raise_for_status()
    pprint.pp(r.json())
else:
    _hr("no calls found → skip recordings")

# --------------------------------------------------------------------------- #
# 4) last 5 messages for that number
# --------------------------------------------------------------------------- #

_hr("recent messages")

resp = http.get(
    "/v1/messages",
    params={
        "phoneNumberId": PHONE_ID,
        "participants": [E164],   # ← required just like /v1/calls
        "maxResults":    5,
    },
)
if resp.is_error:
    print("⇡ 400-payload →", resp.status_code, resp.text)   # keep for debugging
resp.raise_for_status()

for m in resp.json()["data"]:
    print(f"{m['id']} • {_when(m['createdAt'])} • {m['content'][:40]!r}")
