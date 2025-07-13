from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langchain_core.runnables import Runnable, RunnableMap
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.tools import tool
from langchain_core.language_models import BaseChatModel
from langchain_openai import ChatOpenAI
from typing import TypedDict, List, Annotated
from langdetect import detect
from agents import summarize as summarize_agent, translate as translate_agent  # Avoid name clash

# Define the input/output schema
class GraphState(TypedDict):
    text: str
    trace: List[dict]
    next_step: str

# Tool definitions (wrappers for real agent functions)
def translate(state: dict) -> str:
    """Translate the text to English using the agent."""
    result = translate_agent({"text": state["text"]})
    return result["text"]

def summarize(state: dict) -> str:
    """Summarize the text using the agent."""
    result = summarize_agent({"text": state["text"]})
    return result["text"]

# Router function
class Router(Runnable):
    def invoke(self, state: GraphState, config=None) -> GraphState:
        input_text = state["text"]
        try:
            detected_lang = detect(input_text)
        except Exception as e:
            detected_lang = "unknown"
        route = "summarize" if detected_lang == "en" else "translate"
        trace_entry = {
            "name": "router",
            "content": f"Detected language: {detected_lang}. Routed to: {route} based on input: {input_text}"
        }
        return {
            "text": input_text,
            "trace": state.get("trace", []) + [trace_entry],
            "next_step": route
        }

# Tool Executor
tools = {
    "translate": translate,
    "summarize": summarize
}

def tool_node(state: GraphState, tool_name: str) -> GraphState:
    tool_fn = tools[tool_name]
    output = tool_fn(state)
    trace_entry = {
        "name": tool_name,
        "content": f"Tool '{tool_name}' output: {output}"
    }
    return {
        "text": output,
        "trace": state.get("trace", []) + [trace_entry],
        "next_step": ""
    }

# Build the LangGraph
builder = StateGraph(GraphState)
builder.add_node("router", Router())
builder.add_node("summarize", lambda state: tool_node(state, "summarize"))
builder.add_node("translate", lambda state: tool_node(state, "translate"))

builder.set_entry_point("router")
builder.add_conditional_edges(
    "router",
    lambda state: state["next_step"],
    {"summarize": "summarize", "translate": "translate"}
)

builder.add_edge("summarize", END)
builder.add_edge("translate", END)

graph = builder.compile()

def get_graph():
    return graph
