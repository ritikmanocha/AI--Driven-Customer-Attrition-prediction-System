# 📊 AI-Driven Customer Attrition Prediction System 

A comprehensive AI-powered customer retention platform that combines Machine Learning-based churn prediction with a Retrieval-Augmented Generation (RAG) chatbot for intelligent customer support and business insights.

---

## 🚀 Project Overview

Customer attrition (churn) is a critical challenge for telecom companies. This project leverages Machine Learning to predict customer churn risk and integrates a RAG-powered chatbot that can answer customer and business-related queries using a custom telecom knowledge base.

The system helps organizations identify at-risk customers, understand churn patterns, and provide intelligent assistance through conversational AI.

---

## ✨ Key Features

### 🤖 Customer Churn Prediction

* Predicts customer attrition using Machine Learning
* Displays churn probability and risk level
* Supports real-time predictions
* Generates actionable retention recommendations

### 💬 RAG Chatbot Assistant

* Retrieval-Augmented Generation (RAG) architecture
* Semantic search using FAISS vector database
* Context-aware responses
* Telecom knowledge base integration
* Intelligent question answering

### 📊 Interactive Dashboard

* Streamlit-based user interface
* Customer analytics and insights
* Business overview dashboard
* Clean and responsive design

### 🔐 User Management

* Login authentication system
* User registration support
* Session management

### 💳 Payment Module

* Payment integration support
* Premium feature access management

---

## 🧠 Machine Learning Pipeline

### Churn Prediction Model

* Algorithm: Random Forest Classifier
* Data Preprocessing
* Feature Encoding
* Missing Value Handling
* Class Imbalance Handling (SMOTE)
* Model Evaluation & Validation

### RAG Architecture

* Document Processing
* Text Chunking
* Embedding Generation
* FAISS Vector Indexing
* Context Retrieval
* LLM-based Response Generation

---

## 🛠️ Tech Stack

### Frontend

* Streamlit
* HTML/CSS

### Backend

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Generative AI & RAG

* LangChain
* FAISS
* HuggingFace Embeddings

### Data Storage

* Pickle
* CSV Files

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
CUSTOMER_ATTRITION/
│
├── assets/
│   └── style.css
│
├── backend/
│
├── chatbot/
│   ├── rag_chatbot.py
│   ├── rag_chatbot.ipynb
│   ├── telecom_index.faiss
│   ├── telecom_texts.pkl
│   └── vector_db.ipynb
│
├── config/
│   └── settings.py
│
├── data/
│   ├── users.csv
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── model/
│   ├── customer_churn_model.pkl
│   ├── features.json
│   └── Customer churn prediction.ipynb
│
├── pages/
│   ├── Login.py
│   ├── Overview.py
│   └── Payment.py
│
├── app.py
├── encoders.pkl
├── .env
├── .gitignore
└── README.md
```

---

## ▶️ Installation & Setup

### Clone Repository

```bash
git clone <repository-url>
```

### Navigate to Project

```bash
cd CUSTOMER_ATTRITION
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---

## 📊 Dataset

Dataset: Telco Customer Churn Dataset

Includes:

* Customer Demographics
* Service Information
* Account Details
* Billing Information
* Contract Information
* Churn Status

---

## 💬 RAG Chatbot Workflow

1. Telecom documents are processed.
2. Documents are converted into embeddings.
3. Embeddings are stored in a FAISS vector database.
4. User queries are converted into vectors.
5. Relevant context is retrieved.
6. LLM generates context-aware responses.

---

## 🔮 Future Enhancements

* Deployment on AWS / Azure
* Advanced LLM Integration
* Multi-document Knowledge Base
* Customer Segmentation Analytics
* Real-time Database Connectivity
* Email & SMS Retention Campaigns
* Voice-enabled AI Assistant

---

## 👨‍💻 Author

**Ritik Manocha**

B.Tech – Artificial Intelligence & Data Science

Aspiring AI/ML Engineer | Generative AI Enthusiast

---

## ⭐ Support

If you found this project useful, consider giving the repository a star.
