import streamlit as st

st.set_page_config(layout="wide")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "paid" not in st.session_state:
    st.session_state["paid"] = False

if not st.session_state["logged_in"]:
    # Professional Header
    st.title("Welcome to the AI-Driven Customer Attrition Prediction System")
    st.markdown("---")
    
    # Split layout into interactive information and actions
    col = st.columns([1.2, 1], gap="large")
    
    # FIX: Used col[0] index to target the first column correctly
    with col[0]:
        # Structured Warning / Welcome Card
        with st.container(border=True):
            st.markdown("### 🔐 System Access Notice")
            st.write("Please login to continue.")
            
            st.info("""
            * **New user?** Register first and then login.
            * **Existing user?** Login with your credentials.
            """)
            
    st.stop()
