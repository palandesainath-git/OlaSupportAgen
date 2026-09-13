from fastapi import FastAPI
from pydantic import BaseModel
from agent.graph import build_graph
import uuid, time, json

app = FastAPI(title="Ola Support Agent API")
graph = build_graph()

# ---------------- Models ----------------
class AskRequest(BaseModel):
    query: str

class AskResponse(BaseModel):
    query: str
    answer: str
    confidence: float

class AddDocumentRequest(BaseModel):
    doc_text: str

# ---------------- Logging ----------------
def log_request(query, response):
    log_entry = {
        "trace_id": str(uuid.uuid4()),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "query": query,
        "response": response,
    }
    with open("logs/requests.log", "a") as f:
        f.write(json.dumps(log_entry) + "\n")

# ---------------- Endpoints ----------------
@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    result = graph.run(req.query)
    log_request(req.query, result)
    return result

@app.post("/add-document")
def add_document(req: AddDocumentRequest):
    # Placeholder for adding new KB docs dynamically
    with open("knowledge_base/new_doc.md", "w") as f:
        f.write(req.doc_text)
    return {"message": "Document added successfully"}


