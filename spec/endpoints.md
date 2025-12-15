# Endpoint inventory

Generated from spec/quo-openapi-v1.json. Do not edit by hand.

| Method | Path | Operation ID | Summary |
| --- | --- | --- | --- |
| GET | /v1/call-recordings/{callId} | getCallRecordings_v1 | Get recordings for a call |
| GET | /v1/call-summaries/{callId} | getCallSummary_v1 | Get a summary for a call |
| GET | /v1/call-transcripts/{id} | getCallTranscript_v1 | Get a transcription for a call |
| GET | /v1/calls | listCalls_v1 | List calls |
| GET | /v1/contact-custom-fields | getContactCustomFields_v1 | Get contact custom fields |
| POST | /v1/contacts | createContact_v1 | Create a contact |
| DELETE | /v1/contacts/{id} | deleteContact_v1 | Delete a contact |
| GET | /v1/contacts/{id} | getContactById_v1 | Get a contact by ID |
| PATCH | /v1/contacts/{id} | updateContactById_v1 | Update a contact by ID |
| GET | /v1/messages | listMessages_v1 | List messages |
| POST | /v1/messages | sendMessage_v1 | Send a text message |
| GET | /v1/messages/{id} | getMessageById_v1 | Get a message by ID |
| GET | /v1/phone-numbers | listPhoneNumbers_v1 | List phone numbers |
| GET | /v1/webhooks | listWebhooks_v1 | Lists all webhooks |
| POST | /v1/webhooks/call-summaries | createCallSummaryWebhook_v1 | Create a new webhook for call summaries |
| POST | /v1/webhooks/call-transcripts | createCallTranscriptWebhook_v1 | Create a new webhook for call transcripts |
| POST | /v1/webhooks/calls | createCallWebhook_v1 | Create a new webhook for calls |
| POST | /v1/webhooks/messages | createMessageWebhook_v1 | Create a new webhook for messages |
| DELETE | /v1/webhooks/{id} | deleteWebhookById_v1 | Delete a webhook by ID |
| GET | /v1/webhooks/{id} | getWebhookById_v1 | Get a webhook by ID |
