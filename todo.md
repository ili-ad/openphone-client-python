# Wrapper backlog
- [x] 1. wrap `/calls/get-call-recordings` → `quo_sdk/get_call_recordings.py`
- [x] 2. wrap `/calls/get-call-summary` → `quo_sdk/get_call_summary.py`
- [x] 3. wrap `/calls/get-call-transcript` → `quo_sdk/get_call_transcript.py`
- [x] 4. wrap `/calls/list-calls` → `quo_sdk/list_calls.py`
- [x] 5. wrap `/contact-custom-fields/get-contact-custom-fields` → `quo_sdk/get_contact_custom_fields.py`
- [x] 6. wrap `/contacts/create-contact` → `quo_sdk/create_contact.py`
- [x] 7. wrap `/contacts/delete-contact` → `quo_sdk/delete_contact.py`
- [x] 8. wrap `/contacts/get-contact-by-id` → `quo_sdk/get_contact_by_id.py`
- [x] 9. wrap `/contacts/list-contacts` → `quo_sdk/list_contacts.py`
- [x] 10. wrap `/contacts/update-contact-by-id` → `quo_sdk/update_contact_by_id.py`
- [x] 11. wrap `/conversations/list-conversations` → `quo_sdk/list_conversations.py`
- [x] 12. wrap `/messages/get-message-by-id` → `quo_sdk/get_message_by_id.py`
- [x] 13. wrap `/messages/list-messages` → `quo_sdk/list_messages.py`
- [x] 14. wrap `/messages/send-message` → `quo_sdk/send_message.py`
- [x] 15. wrap `/phone-numbers/list-phone-numbers` → `quo_sdk/list_phone_numbers.py`
- [x] 16. wrap `/webhooks/create-call-summary-webhook` → `quo_sdk/create_call_summary_webhook.py`
- [x] 17. wrap `/webhooks/create-call-transcript-webhook` → `quo_sdk/create_call_transcript_webhook.py`
- [x] 18. wrap `/webhooks/create-call-webhook` → `quo_sdk/create_call_webhook.py`
- [x] 19. wrap `/webhooks/create-message-webhook` → `quo_sdk/create_message_webhook.py`
- [x] 20. wrap `/webhooks/delete-webhook-by-id` → `quo_sdk/delete_webhook_by_id.py`
- [x] 21. wrap `/webhooks/get-webhook-by-id` → `quo_sdk/get_webhook_by_id.py`
- [x] 22. wrap `/webhooks/list-webhooks` → `quo_sdk/list_webhooks.py`
- [x] Ticket 5B: validate created_after/created_before ordering in list_calls and list_messages


## Backlog – polish after first integration

| area | task | payoff |
|------|------|--------|
| Wrappers not yet exercised | E2E create/update/delete contact & webhooks | prove write flows |
| Automated tests | turn smoke_everything into pytest marked @live | confidence w/out spamming API |
| CI / CD | GitHub Actions: ruff + pytest | green badge |
| Packaging | fill poetry metadata, README quick-start | PyPI-ready |
| Docs | mention “participants required” nuance | save future you headaches |
| Typing | mypy + pre-commit | catch bugs early |



Wrappers you haven’t exercised	Create / Update / Delete flows:
• create_contact, update_contact_by_id, delete_contact
• All four create_*_webhook helpers
• delete_webhook_by_id	Confirms that all 21 helpers succeed against the real service (not just the 6 read-only ones). You can run them against a throw-away contact/webhook and immediately delete it so your workspace stays tidy.
Automated tests	• Convert examples/smoke_everything.py into an end-to-end pytest marked @pytest.mark.live (skipped on CI unless an env-flag is set).
• Keep the existing offline tests for fast local iterations.	Lets CI keep you honest, but avoids hitting the OpenPhone quota on every PR.
CI / CD	• Add a minimal GitHub Actions matrix: poetry install, ruff, pytest (offline suite).
• Optionally add a job that runs the live test only when OPENPHONE_API_KEY is present in repo secrets.	Green badge = instant credibility for anyone landing on your repo.
Packaging polish	• Fill in tool.poetry.authors, repository, homepage, keywords.
• Add a short-but-clear README “Quick-start” that shows:
pip install openphone-client … from quo_sdk import list_phone_numbers.
• Cut a CHANGELOG 1.0.0 entry and tag a release on GitHub.	Makes the library discoverable & attractive for PyPI / Git users.
Docs	• Keep the examples/ folder: smoke_everything.py, smoke_wrapper.py, and a “send a text” sample (guarded by a SEND_DEMO=False flag).
• Mention the “participants required” nuance in the README so future users don’t stumble.	Reduces support questions down the road (even if “support” is just future-you).
Type safety niceties	• poetry add --dev mypy types-pytz and run mypy quo_sdk examples. Fix any red flags.
• Configure pre-commit: ruff, mypy, and pytest -q.	Catches foot-guns before they reach Git.
PyPI publish (optional)	poetry config pypi-token.pypi <token> → poetry publish --build.


#Full write sanity run:

from quo_sdk import (
    create_contact, update_contact_by_id, delete_contact,
    create_message_webhook, delete_webhook_by_id,
)

# 1. create a contact
new_contact = create_contact(body={
    "defaultFields": {"firstName": "SDK-Test", "lastName": "Temp"},
    "phoneNumbers":  ["+15555550123"],
})
cid = new_contact.data.id
print("✓ created contact", cid)

# 2. patch it
update_contact_by_id(cid, body={"defaultFields": {"firstName": "SDK-Test-Renamed"}})
print("✓ patched name")

# 3. create then delete a webhook
wb = create_message_webhook(body={
    "url": "https://example.com/hook",
    "events": ["message.created"],
})
wid = wb.data.id
print("✓ webhook id", wid)
delete_webhook_by_id(wid)
print("✓ deleted webhook")

# 4. finally delete contact
delete_contact(cid)
print("✓ cleanup done")


-----

3. First thoughts on wiring into ERPNext
decision	minimal, practical approach
Where to run the OpenPhone code?	A small Frappe App inside your ERPNext bench. Keeps everything in-process; you can still break it out later.
Inbound flow (calls / SMS)	1. In OpenPhone dashboard create Webhooks → point to /api/method/openphone_inbox.webhook.
2. In the Frappe app define that whitelisted method: deserialize payload, look up / create a Communication doc (or a custom DocType “OpenPhone Message”), link it to Customer / Lead by phone number.
Outbound flow (send SMS)	Add a Server Script or ERPNext “SMS Center” integration that calls quo_sdk.send_message when users hit “Send SMS” on Contact / Communication.
Config	Store OPENPHONE_API_KEY with bench set-config openphone_api_key <key>; fetch via frappe.conf.openphone_api_key.
Background jobs	Long-running things (e.g., downloading call transcripts) → enqueue via frappe.enqueue.