from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AskRequest(BaseModel):
    query: str

@app.post("/ask")
def ask(request: AskRequest):
    return {"answer": f"You asked: {request.query}"}
