"""
Quick sanity-check that uses *your* wrappers, not raw httpx.

• Lists the first workspace number
• Pulls calls from the last 30 days that involve one other party
• Prints the timestamp that best represents “when the call started ringing”
• Lists the last 5 messages with that party
"""

import datetime, os, pytz
from   openphone_sdk.list_phone_numbers import list_phone_numbers
from   openphone_sdk.list_calls        import list_calls
from   openphone_sdk.list_messages     import list_messages


# ---------------------------------------------------------------------------
# 0) pick the first number in the workspace
# ---------------------------------------------------------------------------
first_num = list_phone_numbers().data[0]
PHONE_ID  = first_num.id
OTHER     = "+16602301809"          # ← replace with any E.164 the UI shows

# ---------------------------------------------------------------------------
# 1) calls that mention that participant, last 30 days
# ---------------------------------------------------------------------------
now   = datetime.datetime.now(pytz.UTC)
since = now - datetime.timedelta(days=30)

calls = list_calls(
    phone_number_id = PHONE_ID,
    participants    = [OTHER],
    since           = since,
    max_results     = 5,
)

print(f"calls fetched: {len(calls.data)}")
for c in calls.data:
    # answered_at exists only if the call was picked up;
    # otherwise fall back to when it was created/rang
    ts = c.answered_at or c.created_at
    print(f"{c.id} • dir={c.direction} • {ts}")

# ---------------------------------------------------------------------------
# 2) last 5 messages with that participant
# ---------------------------------------------------------------------------
msgs = list_messages(
    phone_number_id = PHONE_ID,
    participants    = [OTHER],
    max_results     = 5,
)

print(f"\nmessages fetched: {len(msgs.data)}")
for m in msgs.data:
    print(f"{m.id} • {m.created_at} • {m.content[:40]!r}")
