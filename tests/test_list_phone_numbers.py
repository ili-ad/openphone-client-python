import os
from httpx import Response


def test_list_phone_numbers(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"
    httpx_mock.add_response(
        method="GET",
        url="https://api.openphone.com/v1/phone-numbers?userId=USR1",
        json={"data": []},
        status_code=200,
    )

    from openphone_sdk.list_phone_numbers import list_phone_numbers

    out = list_phone_numbers("USR1")

    req = httpx_mock.get_request()
    assert req.method == "GET"
    assert str(req.url) == "https://api.openphone.com/v1/phone-numbers?userId=USR1"
    assert req.headers.get("Authorization") == "k"
    assert out.data == []
