"""
End-to-end live test that exercises all public wrappers.

• Picks the first workspace number
• Uses /v1/conversations to discover “the other participant”
• Lists recent calls & messages that involve that participant
• (Optionally) downloads call-recording segments

Prereq:  OPENPHONE_API_KEY in your env or .env
"""

from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone
from pprint import pp

from quo_sdk import (
    list_phone_numbers,
    list_calls,
    list_messages,
    get_call_recordings,
)
from quo_sdk.experimental import list_conversations

# ── 0. ENV CHECK ────────────────────────────────────────────────────────────
KEY = os.getenv("OPENPHONE_API_KEY")
if not KEY:
    raise SystemExit("✘  set OPENPHONE_API_KEY first")
print("✔ using key:", KEY[:8] + "…")

# ── 1. FIRST WORKSPACE NUMBER ───────────────────────────────────────────────
num = list_phone_numbers().data[0]
PHONE_ID = num.id
print(f"\n— phone number —\n{PHONE_ID} • {num.formatted_number}")

# ── 2. PICK ONE PARTICIPANT (no phone-number filter – API doesn’t allow it) ─
conv_resp = list_conversations(max_results=1)        #  👈  only arg we send
if not conv_resp.data:
    raise SystemExit("✘  no conversations yet — place a call or send a text first")

OTHER = conv_resp.data[0].participants[0]           #  "+1………"
print("\n— discovered participant —\n", OTHER)

# ── 3. RECENT CALLS WITH THAT PARTICIPANT (last 30 days) ───────────────────
now   = datetime.now(timezone.utc)
since = now - timedelta(days=30)

calls = list_calls(
    phone_number_id = PHONE_ID,
    participants    = [OTHER],          # ←  must specify at least one number
    created_after   = since,
    max_results     = 5,
)

print("\n— recent calls —")
if not calls.data:
    print("  (none)")
else:
    newest = calls.data[0]
    when   = (newest.answered_at or newest.created_at).astimezone()
    print(f"{newest.id} • dir={newest.direction} • {when:%Y-%m-%d %H:%M}")

    # 3b. RECORDINGS FOR THAT CALL (if any)
    rec = get_call_recordings(newest.id)
    print("  ↳ recording segments:", len(rec.data))

# ── 4. RECENT MESSAGES WITH THAT PARTICIPANT ───────────────────────────────
msgs = list_messages(
    phone_number_id = PHONE_ID,
    participants    = [OTHER],
    max_results     = 5,
)

print("\n— recent messages —")
for m in msgs.data:
    ts = m.created_at.astimezone().strftime("%Y-%m-%d %H:%M")
    print(f"{m.id} • {ts} • {m.content[:40]!r}")

print("\n✔ integration-smoke finished OK")
