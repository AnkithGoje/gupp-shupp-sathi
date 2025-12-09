from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from memex.extractor import extract_memory
from personality.engine import rewrite
from memex.models import ExtractionResult

app = FastAPI(title="Companion AI")

class IngestRequest(BaseModel):
    messages: List[str]

class RewriteRequest(BaseModel):
    messages: List[str]
    tone: str
    original_answer: str

@app.post("/ingest", response_model=ExtractionResult)
def ingest(req: IngestRequest):
    return extract_memory(req.messages)

@app.post("/rewrite")
def rewrite_ep(req: RewriteRequest):
    mem = extract_memory(req.messages)
    new = rewrite(req.original_answer, mem, req.tone)
    return {"before": req.original_answer, "after": new}