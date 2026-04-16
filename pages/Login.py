from backend.utils import load_css
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")


load_css()
#center layout
st.markdown("<br>", unsafe_allow_html=True)

# --- center container ---


st.markdown('<h2 class="center-title"> Login</h2>', unsafe_allow_html=True)

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    df=pd.read_csv("data/users.csv")

    user=df[(df["username"]==username)  & (df["password"]==password)] 

    if not user.empty:
        st.session_state["logged_in"]=True
        st.success("Login Successful")
    else:
        st.error("Invalid Credentials")
