import os
from httpx import Response


def test_get_contact_custom_fields(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"
    httpx_mock.add_response(
        method="GET",
        url="https://api.openphone.com/v1/contact-custom-fields",
        json={"data": []},
        status_code=200,
    )

    from openphone_sdk.get_contact_custom_fields import get_contact_custom_fields

    out = get_contact_custom_fields()

    req = httpx_mock.get_request()
    assert req.method == "GET"
    assert str(req.url) == "https://api.openphone.com/v1/contact-custom-fields"
    assert req.headers.get("X-API-KEY") == "k"
    assert out.data == []
