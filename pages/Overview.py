import streamlit as st
import pandas as pd
import numpy as np
import pickle
from chatbot.rag_chatbot import ask_chatbot

#------------Payment Page procedure-----------------#
if "paid" not in st.session_state:
    st.session_state["paid"] = False



st.set_page_config(layout="wide")
st.markdown("""
<style>

/* 🌑 MAIN BACKGROUND */
.stApp {
    background-color: #000000;
}

/* 📦 CARD STYLE (Clean Tech) */
.card {
    background-color: #161616;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #27272A;
    text-align: center;
    transition: all 0.25s ease;
}

/* ✨ Hover Effect (Subtle, Professional) */
.card:hover {
    border: 1px solid #3f3f46;
    transform: translateY(-5px);
}

/* 🧾 Title inside card */
.card h3 {
    color: #A1A1AA;
    font-size: 20px;
    font-weight: 500;
}

/* 🔢 Value inside card */
.card h1 {
    color: #FFFFFF;
    font-size: 32px;
    margin-top: 5px;
}

/* 🔘 Button Style */
div.stButton > button {
    background-color: #FFFFFF;
    color: black;
    border-radius: 8px;
    border: none;
    font-weight: 600;
}

/* 📊 Section Titles */
h2, h3 {
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #161616;
    border-right: 1px solid #27272A;
}

</style>
""", unsafe_allow_html=True)


#-----------------dataframe loading---------------
df=pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
# Sidebar
st.sidebar.title("Telecom AI")
menu = st.sidebar.radio("Menu", ["Overview", "Customer Risk"])

# Title



# Load model
with open("model/customer_churn_model.pkl", "rb") as f:
  model_data = pickle.load(f)
model= model_data["model"]
feature_names=model_data["features_names"]

#------------Title Setting-----------------#
st.markdown("""
<h1 style='text-align: center; 
            margin-top: -50px;'>
AI-Driven Customer Attrition Prediction System
</h1>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ---------------- #
st.sidebar.header("📥 Enter Customer Details")

# Customer Info
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
senior = st.sidebar.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.sidebar.selectbox("Partner", ["No", "Yes"])
dependents = st.sidebar.selectbox("Dependents", ["No", "Yes"])

# Account Info
tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
payment = st.sidebar.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer", "Credit card"
])

# Services
internet = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
tech_support = st.sidebar.selectbox("Tech Support", ["Yes", "No"])
online_security = st.sidebar.selectbox("Online Security", ["Yes", "No"])
streaming = st.sidebar.selectbox("Streaming TV", ["Yes", "No"])

# Charges
monthly = st.sidebar.number_input("Monthly Charges", 0, 200, 50)
total = st.sidebar.number_input("Total Charges", 0, 10000, 500)

# ---------------- ENCODING ---------------- #
def encode():
    input_dict = {   # dictionery made for features
         "gender": 1 if gender == "Male" else 0,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "Partner": 1 if partner == "Yes" else 0,
        "Dependents": 1 if dependents == "Yes" else 0,
        "tenure": tenure,
        "Contract": 1 if contract == "One year" else (2 if contract == "Two year" else 0),
        "PaperlessBilling": 1 if paperless == "Yes" else 0,
        "PaymentMethod": 0 if payment == "Electronic check" else 1,
        "InternetService": 0 if internet == "DSL" else (1 if internet == "Fiber optic" else 2),
        "TechSupport": 1 if tech_support == "Yes" else 0,
        "OnlineSecurity": 1 if online_security == "Yes" else 0,
        "StreamingTV": 1 if streaming == "Yes" else 0,
        "MonthlyCharges": monthly,
        "TotalCharges": total,

        # Missing features in UI handled here
        "PhoneService": 1,
        "MultipleLines": 0,
        "OnlineBackup": 0,
        "DeviceProtection": 0,
        "StreamingMovies": 0
    }
    data=pd.DataFrame([input_dict])
    
    #reindex used
    data=data.reindex(columns=feature_names, fill_value=0)
    return data



# ---------------- PREDICTION ---------------- #


if st.button("🔍 Predict Churn"):

    # check payment first
    if not st.session_state["paid"]:
        st.error("Please complete payment first to access prediction feature")
        st.stop()

        #if paid then run the model
    data = encode()
    
    prediction = model.predict(data)[0]
    prob = model.predict_proba(data)[0][1]

    st.subheader("📈 Prediction Result")

    

    # ---------------- AI ANALYSIS ---------------- #

    customer_info = f"""
    Contract: {contract}
    Internet Service: {internet}
    Tenure: {tenure}
    Monthly Charges: {monthly}
    Payment Method: {payment}
    Tech Support: {tech_support}
    Online Security: {online_security}

    Churn Probability: {round(prob*100,2)}%
    """

    query = f"""
    Analyze this telecom customer.

    {customer_info}

    Why is this customer at risk?

    Suggest retention actions.
    """

    ai_response = ask_chatbot(query)

    st.subheader("🤖 AI Churn Analysis")

    st.write(ai_response)



    col1, col2, col3 = st.columns(3)

    # Prediction
    with col1:
        st.metric("Prediction", "Churn" if prediction == 1 else "No Churn")

    # Probability
    with col2:
        st.metric("Churn Probability", f"{round(prob*100,2)}%")

    # Risk Level
    with col3:
        if prob > 0.7:
            st.error("🔴 High Risk")
            action = "Offer discount / Call customer"
        elif prob > 0.4:
            st.warning("🟡 Medium Risk")
            action = "Send offers"
        else:
            st.success("🟢 Low Risk")
            action = "No action needed"

    # Progress bar
    st.progress(int(prob * 100))

    # Recommendation
    st.subheader("💡 Recommendation")
    st.write(action)

# Top Metrics
col1, col2, col3, col4 = st.columns(4)
# values shown for dataset
total_customers=len(df)
churned=df[df["Churn"]=="Yes"].shape[0]
active=df[df["Churn"]=="No"].shape[0]
churn_rate=round((churned/total_customers)*100,2)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="card">
        <h3>Total Customers</h3>
        <h1>{total_customers}</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <h3>Active Customers</h3>
        <h1>{active}</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <h3>Churned Customers</h3>
        <h1>{churned}</h1>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="card">
        <h3>Churn Rate</h3>
        <h1>{churn_rate}%</h1>
    </div>
    """, unsafe_allow_html=True)


# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Risk Distribution")
    data = pd.DataFrame({
        'Risk': ['High', 'Medium', 'Low'],
        'Count': [10, 25, 65]
    })
    st.bar_chart(data.set_index('Risk'))

with col2:
    st.subheader("Monthly Churn Trend")
    trend = pd.DataFrame(np.random.randn(12), columns=['Churn'])
    st.line_chart(trend)

# Table
st.subheader("High-Risk Customers")
df = pd.DataFrame({
    "Customer ID": [1,2,3],
    "Churn Probability": ["85%", "78%", "90%"],
    "Action": ["Call", "Discount", "Offer"]
})
st.dataframe(df)
