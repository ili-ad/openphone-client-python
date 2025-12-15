from quo_sdk.request import client
from quo_client.api.contact_custom_fields.get_contact_custom_fields_v_1 import sync
from quo_client.models.get_contact_custom_fields_v1_response_200 import GetContactCustomFieldsV1Response200


def get_contact_custom_fields() -> GetContactCustomFieldsV1Response200:
    """Return all contact custom fields or raise RuntimeError on non-200."""
    res = sync(client=client())
    if isinstance(res, GetContactCustomFieldsV1Response200):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
