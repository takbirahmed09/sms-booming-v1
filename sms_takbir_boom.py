import os
import time
from getpass import getpass
from twilio.rest import Client

# Banner
banner = """
__________  ______   ______   ______   ______   _________  ______   ______
\      \ /\  __ \ /\  __ \ /\  __ \ /\  __ \ /\___   /\ /\  __ \ /\  ___ \
 \      \ \  __ \ \  __ \ \  __ \ \  __ \ \  __ \ \  __ \ \ \  __ \ \  __ \
 /   __  \ \_\ \_\ \_\ \_\ \_\ \_\ \_\ \_\ \_\  \ \_\  \ \ \_\ \_\ \_\  \_
/   __  \ \_____\ \_____\ \_____\ \_____\ \_____\ \_____\ \_____\ \_____\
\____  \ \/_____/ \/_____/ \/_____/ \/_____/ \/_____/ \/_____/ \/_____/

                                Takbir
"""

print(banner)

# Password protection
password = getpass("Enter the password: ")
if password != 'takbir0099':
    print("Incorrect password. Exiting...")
    exit(1)

# Load credentials from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')

client = Client(account_sid, auth_token)

def send_sms(to_number, message_body):
    try:
        message = client.messages.create(
            body=message_body,
            from_=twilio_phone_number,
            to=to_number
        )
        print(f"Sent message to {to_number}: {message.sid}")
    except Exception as e:
        print(f"Failed to send message to {to_number}: {e}")

# Read phone numbers from a file
with open('numbers.txt', 'r') as file:
    to_numbers = [line.strip() for line in file]

message_body = "Your message here"

for number in to_numbers:
    send_sms(number, message_body)
    time.sleep(1)  # Add a 1-second delay between messages to avoid rate limiting

# Optional: Log successful sends to a file
with open('successful_sends.txt', 'w') as log_file:
    for number in to_numbers:
        log_file.write(f"Sent to: {number}\n")
