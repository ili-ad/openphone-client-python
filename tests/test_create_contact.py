import os
import json
import datetime

from openphone_client.models.create_contact_v1_body import CreateContactV1Body
from openphone_client.models.create_contact_v1_body_default_fields import CreateContactV1BodyDefaultFields
from openphone_client.models.create_contact_v1_response_201 import CreateContactV1Response201
from openphone_client.models.create_contact_v1_response_201_data import CreateContactV1Response201Data
from openphone_client.models.create_contact_v1_response_201_data_default_fields import CreateContactV1Response201DataDefaultFields


def test_create_contact(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"

    body = CreateContactV1Body(
        default_fields=CreateContactV1BodyDefaultFields(first_name="Alice")
    )

    response_json = CreateContactV1Response201(
        data=CreateContactV1Response201Data(
            id="C123",
            external_id=None,
            source="public-api",
            source_url=None,
            default_fields=CreateContactV1Response201DataDefaultFields(
                company=None,
                emails=[],
                first_name="Alice",
                last_name=None,
                phone_numbers=[],
                role=None,
            ),
            custom_fields=[],
            created_at=datetime.datetime(2023, 1, 1, tzinfo=datetime.timezone.utc),
            updated_at=datetime.datetime(2023, 1, 1, tzinfo=datetime.timezone.utc),
            created_by_user_id="U1",
        )
    ).to_dict()

    httpx_mock.add_response(
        method="POST",
        url="https://api.openphone.com/v1/contacts",
        json=response_json,
        status_code=201,
    )

    from openphone_sdk.create_contact import create_contact

    out = create_contact(body)

    req = httpx_mock.get_request()
    assert req.method == "POST"
    assert str(req.url) == "https://api.openphone.com/v1/contacts"
    assert req.headers.get("X-API-KEY") == "k"
    assert json.loads(req.content.decode()) == body.to_dict()
    assert out.data.id == "C123"
