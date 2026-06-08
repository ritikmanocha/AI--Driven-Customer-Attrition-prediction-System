import streamlit as st

st.set_page_config(layout="wide")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "paid" not in st.session_state:
    st.session_state["paid"] = False

if not st.session_state["logged_in"]:
    st.info("""
🔐 Welcome to the AI-Driven Customer Attrition Prediction System

Please login to continue.

New user? Register first and then login.
Existing user? Login with your credentials.
""")
    st.stop()
