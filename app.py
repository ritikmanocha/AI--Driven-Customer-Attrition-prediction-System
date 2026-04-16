import streamlit as st

st.set_page_config(layout="wide")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "paid" not in st.session_state:
    st.session_state["paid"] = False

if not st.session_state["logged_in"]:
    st.warning("🔐 Please login first")
    st.stop()
