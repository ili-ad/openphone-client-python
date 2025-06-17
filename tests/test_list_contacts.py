import os


def test_list_contacts(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"
    httpx_mock.add_response(
        method="GET",
        url="https://api.openphone.com/v1/contacts?externalIds=123&maxResults=10",
        json={"data": [], "totalItems": 0, "nextPageToken": None},
        status_code=200,
    )

    from openphone_sdk.list_contacts import list_contacts

    out = list_contacts(external_ids=["123"])

    req = httpx_mock.get_request()
    assert req.method == "GET"
    assert str(req.url) == "https://api.openphone.com/v1/contacts?externalIds=123&maxResults=10"
    assert req.headers.get("X-API-KEY") == "k"
    assert out.data == []
