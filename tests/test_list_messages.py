import os
import re


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
    assert req.headers.get("X-API-KEY") == "k"
    params = req.url.params
    assert params["phoneNumberId"] == "PN1"
    assert params.get_list("participants") == ["+1555"]
    assert params["maxResults"] == "5"
    assert out.data == []
