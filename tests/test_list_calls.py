import os


def test_list_calls(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"
    httpx_mock.add_response(
        method="GET",
        url="https://api.openphone.com/v1/calls?phoneNumberId=PN123&participants=%2B1555&maxResults=10",
        json={"data": [], "totalItems": 0, "nextPageToken": None},
        status_code=200,
    )

    from openphone_sdk.list_calls import list_calls

    out = list_calls("PN123", ["+1555"])

    req = httpx_mock.get_request()
    assert req.method == "GET"
    assert (
        str(req.url)
        == "https://api.openphone.com/v1/calls?phoneNumberId=PN123&participants=%2B1555&maxResults=10"
    )
    assert req.headers.get("X-API-KEY") == "k"
    assert out.data == []

