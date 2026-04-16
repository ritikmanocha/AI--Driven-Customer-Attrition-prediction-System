# 📊 AI-Driven Customer Attrition Prediction System

A machine learning-powered web application that predicts customer churn using telecom data. Built with a clean, professional UI and deployed using Streamlit.

---

## 🚀 Project Overview

Customer churn is a major challenge for telecom companies. This project uses machine learning to identify customers who are likely to leave, helping businesses take proactive retention actions.

---

## 🎯 Key Features

* 🔐 User Authentication (Login & Register)
* 💳 Payment Gateway Integration (Stripe - optional premium access)
* 📊 Interactive Dashboard (Clean Tech Dark UI)
* 🤖 Real-time Churn Prediction
* 📈 Probability & Risk Analysis (High / Medium / Low)
* 💡 Smart Recommendations for retention
* 📉 Data Visualization (Charts & Metrics)

---

## 🧠 Machine Learning Model

* Algorithm: Random Forest Classifier
* Dataset: Telco Customer Churn Dataset
* Techniques Used:

  * Data Cleaning & Preprocessing
  * Feature Encoding
  * Handling Missing Values
  * SMOTE (for class imbalance)
  * Train-Test Split
  * Model Evaluation (Accuracy, Precision, Recall)

---

## 🛠️ Tech Stack

* Frontend: Streamlit
* Backend: Python
* Libraries:

  * Pandas
  * NumPy
  * Scikit-learn
  * Pickle
* UI Styling: Custom CSS (Clean Tech Dark Mode)
* Version Control: Git & GitHub

---

## 📂 Project Structure

```
CUSTOMER_ATTRITION/
│
├── assets/
│ └── style.css # UI Styling (Dark Theme)
│
├── backend/
│ ├── utils.py # Helper functions
│ └── pycache/
│
├── config/
│ └── settings.py # Configuration settings
│
├── data/
│ ├── users.csv # User login data
│ └── Telco Dataset.csv # Customer churn dataset
│
├── model/
│ ├── customer_churn_model.pkl # Trained ML model
│ ├── features.json # Feature list
│ └── notebook.ipynb # Model training
│
├── pages/
│ ├── Login.py
│ ├── Register.py
│ ├── Payment.py
│ └── Overview.py
│
├── app.py # Main Streamlit App
├── encoders.pkl # Encoding objects
├── requirements.txt # Dependencies
├── .env # Secret keys (NOT shared)
└── README.md
```

---

## ▶️ How to Run the Project

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo-name.git
```

2. Navigate to the folder:

```
cd your-repo-name
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the app:

```
streamlit run app.py
```

---

## 📊 Dataset

* Source: Telco Customer Churn Dataset (Kaggle)
* Contains customer details like:

  * Demographics
  * Account information
  * Services used
  * Billing data

---

## 🔮 Future Improvements

* Deployment on Streamlit Cloud / AWS
* Advanced ML models (XGBoost, Random Forest)
* Real-time database integration
* Customer segmentation dashboard
* Email/SMS alert system

---

## 👨‍💻 Author

Ritik Manocha
B.Tech (AI & Data Science)

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
