from quo_sdk.request import client
from quo_client.api.contacts.create_contact_v_1 import sync
from quo_client.models.create_contact_v1_body import CreateContactV1Body
from quo_client.models.create_contact_v1_response_201 import CreateContactV1Response201


def create_contact(body: CreateContactV1Body) -> CreateContactV1Response201:
    """Create a contact and return the created contact or raise RuntimeError on non-201."""
    res = sync(client=client(), body=body)
    if isinstance(res, CreateContactV1Response201):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
