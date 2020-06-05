from twilio.rest import Client

account_sid = 'AC82d9de3328c59716562458cac19f45b4'
auth_token = 'f7dee413b52465dad417ef4d600fe288'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12058393775',
    body='Hello, I am from Python using Twilio Trial Account.',
    to='+919500188118'
)

print(message.sid)

# Response
# {
#     "sid": "SMd1582a9d4a874b84a8bb41f8322a7093",
#     "date_created": "Wed, 22 Apr 2020 15:01:51 +0000",
#     "date_updated": "Wed, 22 Apr 2020 15:01:51 +0000",
#     "date_sent": null,
#     "account_sid": "AC82d9de3328c59716562458cac19f45b4",
#     "to": "+919500188118",
#     "from": "+12058393775",
#     "messaging_service_sid": null,
#     "body": "Sent from your Twilio trial account - Hello, I am from Twilio.",
#     "status": "queued",
#     "num_segments": "1",
#     "num_media": "0",
#     "direction": "outbound-api",
#     "api_version": "2010-04-01",
#     "price": null,
#     "price_unit": "USD",
#     "error_code": null,
#     "error_message": null,
#     "uri": "/2010-04-01/Accounts/AC82d9de3328c59716562458cac19f45b4/Messages/SMd1582a9d4a874b84a8bb41f8322a7093.json",
#     "subresource_uris": {
#         "media": "/2010-04-01/Accounts/AC82d9de3328c59716562458cac19f45b4/Messages/SMd1582a9d4a874b84a8bb41f8322a7093/Media.json"
#     }
# }
