import os
from httpx import Response


def test_delete_contact(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"
    httpx_mock.add_response(
        method="DELETE",
        url="https://api.openphone.com/v1/contacts/AB123",
        status_code=204,
    )

    from openphone_sdk.delete_contact import delete_contact

    out = delete_contact("AB123")

    req = httpx_mock.get_request()
    assert req.method == "DELETE"
    assert str(req.url) == "https://api.openphone.com/v1/contacts/AB123"
    assert req.headers.get("Authorization") == "k"
    assert out is None
