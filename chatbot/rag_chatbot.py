import faiss
import pickle
import numpy as np
import google.generativeai as genai

from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv
load_dotenv()

print("Current File:", __file__)
print("Current Folder:", os.path.dirname(__file__))
print("Files:", os.listdir(os.path.dirname(__file__)))

# Gemini API
genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)



llm = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# Load Embedding Model
embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS
import os

BASE_DIR = os.path.dirname(__file__)

index_path = os.path.join(
    BASE_DIR,
    "telecom_index.faiss"
)

print(index_path)

index = faiss.read_index(index_path)
print("FAISS Loaded Successfully")



# Load texts
import os

BASE_DIR = os.path.dirname(__file__)

with open(
    os.path.join(BASE_DIR, "telecom_texts.pkl"),
    "rb"
) as f:
    texts = pickle.load(f)




def retrieve_context(question, k=3):

    query_embedding = embedding_model.encode(
        [question]
    )

    distances, indices = index.search(
        np.array(query_embedding),
        k
    )
    context = []
    for idx in indices[0]:
        context.append(texts[idx])

    return "\n".join(context)

def ask_chatbot(question):

    context = retrieve_context(question)

    prompt = f"""
You are a Telecom Customer Retention Expert.

Use ONLY the provided context.

Context:
{context}

Question:
{question}

Provide:
1. Explanation
2. Risk Factors
3.Suggestions

"""

    response = llm.generate_content(
        prompt
    )

    return response.text