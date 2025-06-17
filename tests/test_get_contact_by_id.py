import os
from httpx import Response


def test_get_contact_by_id(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"
    httpx_mock.add_response(
        method="GET",
        url="https://api.openphone.com/v1/contacts/C123",
        json={
            "data": {
                "id": "C123",
                "externalId": None,
                "source": None,
                "sourceUrl": None,
                "defaultFields": {
                    "company": None,
                    "emails": [],
                    "firstName": None,
                    "lastName": None,
                    "phoneNumbers": [],
                    "role": None
                },
                "customFields": [],
                "createdAt": "2020-01-01T00:00:00+00:00",
                "updatedAt": "2020-01-01T00:00:00+00:00",
                "createdByUserId": "U1"
            }
        },
        status_code=200,
    )

    from openphone_sdk.get_contact_by_id import get_contact_by_id

    out = get_contact_by_id("C123")

    req = httpx_mock.get_request()
    assert req.method == "GET"
    assert str(req.url) == "https://api.openphone.com/v1/contacts/C123"
    assert req.headers.get("X-API-KEY") == "k"
    assert out.data.id == "C123"
