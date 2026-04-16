from dotenv import load_dotenv
from backend.utils import load_css
import os
import stripe
import streamlit as st
# css


load_css()


load_dotenv()  # Load environment variables from .env file
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")



st.title("Payment Page")
st.write("Pay $50 to access the ML Model")

# check URL after Stripe redirect
query_params = st.query_params

if "success" in query_params:
    st.success("Payment Successful ✅")
    st.session_state["paid"] = True

elif "cancel" in query_params:
    st.error("Payment Cancelled ❌")

# button to start payment
if st.button("Pay Now"):

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": "ML Model Access"},
                    "unit_amount": 5000,
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url="http://localhost:8501/Payment?success=true",
            cancel_url="http://localhost:8501/Payment?cancel=true",
        )

        st.markdown(f"[Click here to Pay]({session.url})")

    except Exception as e:
        st.error(str(e))

