from quo_sdk.request import client
from quo_client.api.contacts.delete_contact_v_1 import sync


def delete_contact(contact_id: str) -> None:
    """Delete a contact by ID or raise RuntimeError on non-204."""
    res = sync(id=contact_id, client=client())
    if res is None:
        return None
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
