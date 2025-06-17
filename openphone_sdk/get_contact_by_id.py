from openphone_sdk.request import client
from openphone_client.api.contacts.get_contact_by_id_v_1 import sync
from openphone_client.models.get_contact_by_id_v1_response_200 import GetContactByIdV1Response200


def get_contact_by_id(contact_id: str) -> GetContactByIdV1Response200:
    """Return contact details for the given contact ID or raise RuntimeError on non-200."""
    res = sync(id=contact_id, client=client())
    if isinstance(res, GetContactByIdV1Response200):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
