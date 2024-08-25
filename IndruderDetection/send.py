# from twilio.rest import Client
# account_sid = 'US9fb1cc0c445252fd07e07bcf5e8c7fa6'
# auth_token = 'auth_token'
# client = Client(account_sid, auth_token)
# def sendSms():
#     message = client.messages.create(
#     from_='+16203038645',
#     body='Alert ',
#     to='+919945261886'
#     )

#     print(message.sid)
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+16502854879',
  body='hello',
  to='+919945261886'
)

print(message.sid)
