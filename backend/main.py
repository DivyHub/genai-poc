
from fastapi import FastAPI, Request, Header, HTTPException
from agents import get_summary_agent, get_translation_agent
from langgraph_orchestration import build_graph
import os

app = FastAPI()

graph = build_graph()

@app.post("/process")
async def process(request: Request, x_api_key: str = Header(...)):
    payload = await request.json()
    text = payload.get("text")
    if not text:
        raise HTTPException(status_code=400, detail="Missing 'text'")

    result = graph.invoke({"text": text})
    return {"result": result}
