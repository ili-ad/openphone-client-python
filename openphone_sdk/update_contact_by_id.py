from openphone_sdk.request import client
from openphone_client.api.contacts.update_contact_by_id_v_1 import sync
from openphone_client.models.update_contact_by_id_v1_body import UpdateContactByIdV1Body
from openphone_client.models.update_contact_by_id_v1_response_200 import UpdateContactByIdV1Response200


def update_contact_by_id(contact_id: str, body: UpdateContactByIdV1Body) -> UpdateContactByIdV1Response200:
    """Update a contact by ID or raise RuntimeError on non-200."""
    res = sync(id=contact_id, client=client(), body=body)
    if isinstance(res, UpdateContactByIdV1Response200):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
