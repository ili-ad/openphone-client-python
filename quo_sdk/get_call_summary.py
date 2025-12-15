from quo_sdk.request import client
from quo_client.api.calls.get_call_summary_v_1 import sync
from quo_client.models.get_call_summary_v1_response_200 import GetCallSummaryV1Response200


def get_call_summary(call_id: str) -> GetCallSummaryV1Response200:
    """Return the call summary for the given call ID or raise RuntimeError on non-200."""
    res = sync(call_id=call_id, client=client())
    if isinstance(res, GetCallSummaryV1Response200):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
