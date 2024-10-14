# Women's Safety Alert System

This project is an SMS-based alert system for women's safety that sends an emergency notification when the user inputs their location. The alert system uses Twilio's messaging service to send an SMS to a pre-configured recipient.

## Features:
- **SMS Alerts:** Sends an emergency message with the user's location to a predefined phone number.
- **Twilio Integration:** Utilizes Twilio's messaging API for sending SMS alerts.
- **Streamlit Interface:** Provides a simple user interface for entering the location and sending alerts.

## Prerequisites:
1. **Twilio Account:** Sign up at [Twilio](https://www.twilio.com/) and get your `Account SID`, `Auth Token`, and `Twilio Phone Number` (https://youtu.be/CK31fOgI18M?si=x8BjnUb9GftVUKDJ).
2. **Python Environment:** Make sure you have Python 3.x installed.
3. **Streamlit:** Install Streamlit for the front-end user interface.
4. **Twilio Python SDK:** Install the Twilio Python library for SMS integration.

## Installation:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/women-safety-alert-system.git
   cd women-safety-alert-system

## Configure Twilio:

1. **Update the config/config.json file with your Twilio account_sid, auth_token, twilio_phone, and recipient_phone.**
   ```bash
   {
    "twilio_sid": "Your_Twilio_SID",
    "twilio_token": "Your_Twilio_Token",
    "twilio_phone": "+Your_Twilio_Phone_Number",
    "recipient_phone": "+Recipient_Phone_Number"
   }

## Running the Application

1. **Start the Streamlit App:**
   ```bash
   streamlit run app.py
2. **Usage:**
     - Enter your location in the text input box.
     - Click on the "Send SMS Alert" button.
     - A success or error message will be displayed based on the SMS delivery.
  
## License:
This project is licensed under the MIT License.


