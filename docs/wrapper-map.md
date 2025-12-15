# Wrapper → endpoint map

## Stable exports (pinned spec)
| Wrapper | Method | Path |
| --- | --- | --- |
| `get_call_recordings` | GET | `/v1/call-recordings/{callId}` |
| `get_call_summary` | GET | `/v1/call-summaries/{callId}` |
| `get_call_transcript` | GET | `/v1/call-transcripts/{id}` |
| `list_calls` | GET | `/v1/calls` |
| `get_contact_custom_fields` | GET | `/v1/contact-custom-fields` |
| `create_contact` | POST | `/v1/contacts` |
| `delete_contact` | DELETE | `/v1/contacts/{id}` |
| `get_contact_by_id` | GET | `/v1/contacts/{id}` |
| `update_contact_by_id` | PATCH | `/v1/contacts/{id}` |
| `list_messages` | GET | `/v1/messages` |
| `send_message` | POST | `/v1/messages` |
| `get_message_by_id` | GET | `/v1/messages/{id}` |
| `list_phone_numbers` | GET | `/v1/phone-numbers` |
| `list_webhooks` | GET | `/v1/webhooks` |
| `create_call_summary_webhook` | POST | `/v1/webhooks/call-summaries` |
| `create_call_transcript_webhook` | POST | `/v1/webhooks/call-transcripts` |
| `create_call_webhook` | POST | `/v1/webhooks/calls` |
| `create_message_webhook` | POST | `/v1/webhooks/messages` |
| `delete_webhook_by_id` | DELETE | `/v1/webhooks/{id}` |
| `get_webhook_by_id` | GET | `/v1/webhooks/{id}` |

## Experimental exports (not in pinned spec)
| Wrapper | Method | Path |
| --- | --- | --- |
| `list_conversations` | GET | `/v1/conversations` |
| `list_contacts` | GET | `/v1/contacts` |
