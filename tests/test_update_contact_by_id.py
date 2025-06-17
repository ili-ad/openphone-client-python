import os
import json
from httpx import Response


def test_update_contact_by_id(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"

    from openphone_client.models.update_contact_by_id_v1_body import UpdateContactByIdV1Body
    from openphone_client.models.update_contact_by_id_v1_body_default_fields import UpdateContactByIdV1BodyDefaultFields

    body = UpdateContactByIdV1Body(
        default_fields=UpdateContactByIdV1BodyDefaultFields(first_name="Alice")
    )

    httpx_mock.add_response(
        method="PATCH",
        url="https://api.openphone.com/v1/contacts/123",
        json={
            "data": {
                "id": "123",
                "externalId": None,
                "source": None,
                "sourceUrl": None,
                "defaultFields": {
                    "company": None,
                    "emails": [],
                    "firstName": "Alice",
                    "lastName": "Smith",
                    "phoneNumbers": [],
                    "role": None,
                },
                "customFields": [],
                "createdAt": "2023-01-01T00:00:00Z",
                "updatedAt": "2023-01-01T00:00:00Z",
                "createdByUserId": "u1",
            }
        },
        status_code=200,
    )

    from openphone_sdk.update_contact_by_id import update_contact_by_id

    out = update_contact_by_id("123", body)

    req = httpx_mock.get_request()
    assert req.method == "PATCH"
    assert str(req.url) == "https://api.openphone.com/v1/contacts/123"
    assert req.headers.get("X-API-KEY") == "k"
    assert json.loads(req.content) == body.to_dict()
    assert out.data.id == "123"
