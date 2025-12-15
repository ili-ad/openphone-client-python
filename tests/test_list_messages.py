import os
import re

import pytest


def test_list_messages(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"
    httpx_mock.add_response(
        method="GET",
        url=re.compile(r"https://api\.openphone\.com/v1/messages.*"),
        json={"data": [], "totalItems": 0, "nextPageToken": None},
        status_code=200,
    )

    from openphone_sdk.list_messages import list_messages

    out = list_messages("PN1", participants=["+1555"], max_results=5)

    req = httpx_mock.get_request()
    assert req.method == "GET"
    assert str(req.url).startswith("https://api.openphone.com/v1/messages")
    assert req.headers.get("Authorization") == "k"
    params = req.url.params
    assert params["phoneNumberId"] == "PN1"
    assert params.get_list("participants") == ["+1555"]
    assert params["maxResults"] == "5"
    assert out.data == []


def test_list_messages_rejects_empty_participants():
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"

    from openphone_sdk.list_messages import list_messages

    with pytest.raises(ValueError):
        list_messages("PN1", participants=[])


def test_list_messages_validates_max_results():
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"

    from openphone_sdk.list_messages import list_messages

    with pytest.raises(ValueError):
        list_messages("PN1", participants=["+1"], max_results=0)
