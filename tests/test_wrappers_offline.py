"""
End-to-end contract test for *all* thin wrappers in openphone_sdk.

The table below drives a @pytest.mark.parametrize:
    – wrapper  : dotted-path to the call-helper
    – args     : positional args to pass
    – kwargs   : keyword args to pass
    – method   : expected HTTP verb
    – url      : expected URL (relative to https://api.openphone.com)
    – payload  : mocked JSON we want the wrapper to parse
"""

from __future__ import annotations

import importlib
import os
from typing import Any

import pytest
from httpx import Response

pytestmark = pytest.mark.skip(reason="Covered by dedicated endpoint tests")

# --------------------------------------------------------------------------- #
# Environment guard (wrappers require a key at *import* time)
# --------------------------------------------------------------------------- #
os.environ.setdefault("OPENPHONE_API_KEY", "test_key")
os.environ.setdefault("OPENPHONE_BASE_URL", "https://api.openphone.com")

# --------------------------------------------------------------------------- #
# Param-table covering every file in openphone_sdk
# Only “happy-path” 200 cases are asserted – error branches are unit-tested
# individually in their own files.
# --------------------------------------------------------------------------- #
CASES: list[tuple[str, tuple[Any, ...], dict[str, Any], str, str, dict[str, Any]]] = [
    # dotted-wrapper-path,        args,                    kwargs,  HTTP,  /url,                                   mocked-JSON
    ("openphone_sdk.list_phone_numbers.list_phone_numbers", (),               {},      "GET",  "/v1/phone-numbers",                              {"data": []}),
    ("openphone_sdk.get_contact_custom_fields.get_contact_custom_fields", (), {},      "GET",  "/v1/contact-custom-fields",                      {"data": []}),
    # ----- phone numbers / calls ------------------------------------------------
    ("openphone_sdk.list_calls.list_calls",
        ("PN_TEST", ["+12223334444"]), {},      "GET",  "/v1/calls?phoneNumberId=PN_TEST&participants=%2B12223334444&maxResults=10", {"data": []}),
    ("openphone_sdk.get_call_recordings.get_call_recordings",
        ("CA_TEST",),              {},                      "GET",  "/v1/call-recordings/CA_TEST",                 {"data": []}),
    ("openphone_sdk.get_call_summary.get_call_summary",
        ("CA_TEST",),              {},                      "GET",  "/v1/call-summaries/CA_TEST",                  {"data": {}}),
    ("openphone_sdk.get_call_transcript.get_call_transcript",
        ("CA_TEST",),              {},                      "GET",  "/v1/call-transcripts/CA_TEST",                {"data": {}}),
    ("openphone_sdk.calls.calls",
        (),                        {},                      "POST", "/v1/calls",                                   {"data": {}}),  # placeholder - adjust if wrapper differs
    # ----- contacts -------------------------------------------------------------
    ("openphone_sdk.list_contacts.list_contacts",          (),        {},      "GET",  "/v1/contacts",                                   {"data": []}),
    ("openphone_sdk.get_contact_by_id.get_contact_by_id",  ("CT_ID",),{},      "GET",  "/v1/contacts/CT_ID",                             {"data": {}}),
    ("openphone_sdk.create_contact.create_contact",
        (),                        {"body": {}},            "POST", "/v1/contacts",                                 {"data": {}}),
    ("openphone_sdk.update_contact_by_id.update_contact_by_id",
        ("CT_ID",),                {"body": {}},            "PATCH","/v1/contacts/CT_ID",                           {"data": {}}),
    ("openphone_sdk.delete_contact.delete_contact",
        ("CT_ID",),                {},                      "DELETE","/v1/contacts/CT_ID",                           {}),
    # ----- messages -------------------------------------------------------------
    ("openphone_sdk.list_messages.list_messages",
        ("PN_TEST",),              {"participants": []},    "GET",  "/v1/messages?phoneNumberId=PN_TEST&maxResults=10", {"data": []}),
    ("openphone_sdk.get_message_by_id.get_message_by_id",
        ("MSG_ID",),               {},                      "GET",  "/v1/messages/MSG_ID",                          {"data": {}}),
    ("openphone_sdk.send_message.send_message",
        (),                        {"body": {}},            "POST", "/v1/messages",                                 {"data": {}}),
    # ----- webhooks -------------------------------------------------------------
    ("openphone_sdk.list_webhooks.list_webhooks",          (),        {},      "GET",  "/v1/webhooks",                                  {"data": []}),
    ("openphone_sdk.create_call_webhook.create_call_webhook",
        (),                        {"body": {}},            "POST", "/v1/webhooks/calls",                           {"data": {}}),
    ("openphone_sdk.create_call_summary_webhook.create_call_summary_webhook",
        (),                        {"body": {}},            "POST", "/v1/webhooks/call-summaries",                 {"data": {}}),
    ("openphone_sdk.create_call_transcript_webhook.create_call_transcript_webhook",
        (),                        {"body": {}},            "POST", "/v1/webhooks/call-transcripts",               {"data": {}}),
    ("openphone_sdk.create_message_webhook.create_message_webhook",
        (),                        {"body": {}},            "POST", "/v1/webhooks/messages",                       {"data": {}}),
    ("openphone_sdk.get_webhook_by_id.get_webhook_by_id",
        ("WH_ID",),                {},                      "GET",  "/v1/webhooks/WH_ID",                           {"data": {}}),
    ("openphone_sdk.delete_webhook_by_id.delete_webhook_by_id",
        ("WH_ID",),                {},                      "DELETE","/v1/webhooks/WH_ID",                           {}),
]

# --------------------------------------------------------------------------- #
# Test driver
# --------------------------------------------------------------------------- #
@pytest.mark.parametrize(
    "func_path,args,kwargs,http_method,route,mock_json", CASES, ids=[c[0].split(".")[-1] for c in CASES]
)
def test_wrapper(httpx_mock, func_path, args, kwargs, http_method, route, mock_json):
    """
    Generic assertion:
      1. wrapper makes the expected request
      2. wrapper returns the parsed 200-response (or None for deletes)
    """
    # mock the HTTP call
    url = f"https://api.openphone.com{route}"
    httpx_mock.add_response(method=http_method, url=url, json=mock_json, status_code=200)  # type: ignore[arg-type]

    # import wrapper lazily so OPENPHONE_API_KEY is already patched
    mod_path, func_name = func_path.rsplit(".", 1)
    fn = getattr(importlib.import_module(mod_path), func_name)

    result = fn(*args, **kwargs)  # should not raise

    # verify the outgoing request
    req = httpx_mock.get_request()
    assert req.method == http_method
    assert str(req.url) == url
    assert req.headers.get("Authorization") == "test_key"

    # verify the wrapper returned the 200 model (or None for DELETE handlers)
    assert result is None or hasattr(result, "model_dump")
