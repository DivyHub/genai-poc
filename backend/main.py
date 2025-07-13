from fastapi import FastAPI, Header
from langgraph_orchestration import get_graph
import uvicorn
from utils import detect_language

app = FastAPI()
graph = get_graph()

@app.post("/process")
def process_text(text: str, x_api_key: str = Header(...)):
    # Simple tenant routing using API key
    if not x_api_key:
        return {"error": "Missing API key"}
    lang = detect_language(text)
    if lang == "en":
        output = graph.invoke({"text": text}, start_at="summarize")
    else:
        output = graph.invoke({"text": text})
    return output

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

