# alert.py
import json
from twilio.rest import Client

def load_config():
    with open('config/config.json') as f:
        return json.load(f)

def send_sms(location):
    config = load_config()
    
    account_sid = config['twilio_sid']
    auth_token = config['twilio_token']
    client = Client(account_sid, auth_token)
    
    message_body = f"\n Emergency Alert! The user is in distress at {location}. Please take immediate action."

    try:
        message = client.messages.create(
            body=message_body,
            from_=config['twilio_phone'],
            to=config['recipient_phone']
        )
        return f"Message SID: {message.sid}"
    except Exception as e:
        return f"Error: {e}"