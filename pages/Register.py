import streamlit as st
from backend.utils import load_css
import pandas as pd
#css


load_css()

st.title(" Register")

new_user = st.text_input("Username")
new_pass = st.text_input("Password", type="password")

if st.button("Register"):
     df=pd.read_csv("data/users.csv")

     #check if user exists
     if new_user in df["username"].values:
         st.error("User already exists")
     else:
          new_data= pd.DataFrame({
               "username":[new_user],
               "password":[new_pass]
          })
          df=pd.concat([df,new_data], ignore_index=True)
          df.to_csv("data/users.csv", index=False)

          st.success("Registration Successful")
