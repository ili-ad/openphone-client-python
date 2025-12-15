import os
from httpx import Response


def test_list_conversations(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"
    httpx_mock.add_response(
        method="GET",
        url="https://api.openphone.com/v1/conversations?maxResults=10",
        json={"data": [], "totalItems": 0, "nextPageToken": None},
        status_code=200,
    )

    from openphone_sdk.experimental import list_conversations

    out = list_conversations()

    req = httpx_mock.get_request()
    assert req.method == "GET"
    assert str(req.url) == "https://api.openphone.com/v1/conversations?maxResults=10"
    assert req.headers.get("Authorization") == "k"
    assert out.data == []
