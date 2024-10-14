# app.py
import streamlit as st
from sos_alert import send_sms

st.title("Women's Safety Alert System")

location = st.text_input("Enter your location:")

if st.button("Send SMS Alert"):
    if location:
        result = send_sms(location)
        st.success(result)
    else:
        st.error("Please enter a location.")
