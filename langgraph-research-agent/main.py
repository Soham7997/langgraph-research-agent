from fastapi import FastAPI
from pydantic import BaseModel
from agent import build_agent

app = FastAPI(title="LangGraph Research Agent")
agent = build_agent()

class QueryRequest(BaseModel):
    query: str

@app.post("/research")
def run_research(request: QueryRequest):
    result = agent.invoke({
        "query": request.query,
        "sub_questions": [],
        "answers": [],
        "final_report": ""
    })
    return {
        "query": request.query,
        "sub_questions": result["sub_questions"],
        "answers": result["answers"],
        "final_report": result["final_report"]
    }

@app.get("/")
def health():
    return {"status": "Agent is running!"}