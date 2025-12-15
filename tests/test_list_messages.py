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


def test_list_messages_rejects_reversed_created_range():
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"

    from datetime import datetime

    from openphone_sdk.list_messages import list_messages

    with pytest.raises(ValueError, match="created_after must be <= created_before"):
        list_messages(
            "PN1",
            participants=["+1555"],
            created_after=datetime(2024, 1, 2),
            created_before=datetime(2024, 1, 1),
        )


def test_list_messages_rejects_mixed_timezone_datetimes():
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"

    from datetime import datetime, timezone

    from openphone_sdk.list_messages import list_messages

    with pytest.raises(
        ValueError,
        match="created_after and created_before must be comparable datetimes",
    ):
        list_messages(
            "PN1",
            participants=["+1555"],
            created_after=datetime(2024, 1, 1),
            created_before=datetime(2024, 1, 2, tzinfo=timezone.utc),
        )
