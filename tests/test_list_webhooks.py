import os
from httpx import Response


def test_list_webhooks(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"
    httpx_mock.add_response(
        method="GET",
        url="https://api.openphone.com/v1/webhooks",
        json={"data": []},
        status_code=200,
    )

    from openphone_sdk.list_webhooks import list_webhooks

    out = list_webhooks()

    req = httpx_mock.get_request()
    assert req.method == "GET"
    assert str(req.url) == "https://api.openphone.com/v1/webhooks"
    assert req.headers.get("X-API-KEY") == "k"
    assert out.data == []
