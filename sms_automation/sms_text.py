from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_FROM_NUMBER")
to_number = os.getenv("MY_PHONE_NUMBER")

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_=from_number,
    body="Hello! This is an automated message using the Twilio API and Python.",
    to=to_number
)

print("Message SID:", message.sid)
print("Message sent successfully!")
