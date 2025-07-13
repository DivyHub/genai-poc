import os
from fastapi import FastAPI, Header
from pydantic import BaseModel
from langgraph_orchestration import get_graph
import uvicorn
import traceback

app = FastAPI()
graph = get_graph()

# For demo: list of valid tenant keys (could also load from env or config)
VALID_TENANT_KEYS = os.getenv("VALID_TENANT_KEYS", "t1,t2").split(",")

# Define a Pydantic model for the request body
class TextRequest(BaseModel):
    text: str

@app.post("/process")
def process_text(request: TextRequest, tenant_key: str = Header(...)):
    # Validate tenant_key
    if not tenant_key or tenant_key not in VALID_TENANT_KEYS:
        return {
            "error": "Invalid or missing tenant_key",
            "trace": [],
            "debug": {"tenant_key_received": tenant_key}
        }
    try:
        output = graph.invoke({"text": request.text})
        # Add debug info to the response
        return {
            "text": output.get("text", ""),
            "trace": output.get("trace", []),
            "debug": {
                "tenant_key_used": tenant_key,
                "input_text": request.text,
                "graph_output_keys": list(output.keys())
            }
        }
    except Exception as e:
        return {
            "error": str(e),
            "trace": [],
            "debug": {
                "exception_type": type(e).__name__,
                "exception_details": str(e),
                "traceback": traceback.format_exc()
            }
        }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

