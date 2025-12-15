import os


def test_delete_webhook_by_id(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"

    httpx_mock.add_response(
        method="DELETE",
        url="https://api.openphone.com/v1/webhooks/WH123",
        status_code=204,
    )

    from openphone_sdk.delete_webhook_by_id import delete_webhook_by_id

    out = delete_webhook_by_id("WH123")

    req = httpx_mock.get_request()
    assert req.method == "DELETE"
    assert str(req.url) == "https://api.openphone.com/v1/webhooks/WH123"
    assert req.headers.get("Authorization") == "k"
    assert out is None

