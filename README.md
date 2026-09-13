# OlaSupportAgen – FastAPI Capstone Project

## 🚀 Overview
OlaSupportAgen is a FastAPI-based support agent project.  
It provides endpoints to handle user queries (`/ask`) and manage documents (`/add-document`).  
The project also generates logs for every request, useful for grading and proof.

---

## 📦 Requirements
- Python 3.13+ (Anaconda recommended)
- FastAPI
- Uvicorn
- Pydantic
- Anyio, Starlette, Typing-extensions

Install dependencies:
```bash
pip install -r requirements.txt



▶️ Run the Server

uvicorn api.main:app --reload


INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.


🌐 API Endpoints


Handles user queries.

{
  "query": "What is Ola refund policy?"
}

Response:


{
  "answer": "You asked: What is Ola refund policy?"
}


Adds a document to the knowledge base.


Request:


{
  "title": "Refund Policy",
  "content": "Ola refunds are processed within 7 days."
}


Response:



{
  "title": "Refund Policy",
  "content": "Ola refunds are processed within 7 days."
}


{
  "status": "Document added successfully"
}


📑 Proof & Logs

Interactive API docs: http://127.0.0.1:8000/docs

Alternative docs: http://127.0.0.1:8000/redoc (127.0.0.1 in Bing)

=============================================================================================

OlaSupportAgen/
│
├── api/
│   ├── __init__.py
│   └── main.py          # FastAPI app with /ask and /add-document endpoints
│
├── logs/
│   └── requests.log     # Auto-generated request traces
│
├── requirements.txt     # All dependencies (fastapi, uvicorn, pydantic, etc.)
│
├── README.md            # Project overview, run guide, endpoints, proof checklist
│
├── run_demo.py          # (Optional) Script to send sample queries and auto-generate logs
│
└── .gitignore           # Ignore logs, __pycache__, etc.





============================================================================================

requirement.txt

fastapi==0.115.6
uvicorn==0.30.1
pydantic==2.13.5
anyio==4.15.1
starlette==1.6.0
click
h11
