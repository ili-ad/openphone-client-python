import datetime
import os

import pytest


def test_list_calls(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"
    httpx_mock.add_response(
        method="GET",
        url="https://api.openphone.com/v1/calls?phoneNumberId=PN123&participants=%2B1555&maxResults=10",
        json={"data": [], "totalItems": 0, "nextPageToken": None},
        status_code=200,
    )

    from quo_sdk.list_calls import list_calls

    out = list_calls("PN123", ["+1555"])

    req = httpx_mock.get_request()
    assert req.method == "GET"
    assert (
        str(req.url)
        == "https://api.openphone.com/v1/calls?phoneNumberId=PN123&participants=%2B1555&maxResults=10"
    )
    assert req.headers.get("Authorization") == "k"
    assert out.data == []


def test_list_calls_rejects_empty_participants():
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"

    from quo_sdk.list_calls import list_calls

    with pytest.raises(ValueError):
        list_calls("PN123", [])


def test_list_calls_validates_max_results():
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"

    from quo_sdk.list_calls import list_calls

    with pytest.raises(ValueError):
        list_calls("PN123", ["+1555"], max_results=0)


def test_list_calls_rejects_since():
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"

    from quo_sdk.list_calls import list_calls

    with pytest.raises(ValueError, match="since is deprecated"):
        list_calls("PN123", ["+1555"], since=datetime.datetime.now())


def test_list_calls_rejects_reversed_created_range():
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"

    from quo_sdk.list_calls import list_calls

    earlier = datetime.datetime(2024, 1, 1)
    later = datetime.datetime(2024, 2, 1)

    with pytest.raises(ValueError, match="created_after must be <= created_before"):
        list_calls("PN123", ["+1555"], created_after=later, created_before=earlier)

