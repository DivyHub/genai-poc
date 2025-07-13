# ui/demo.py
import streamlit as st
import sys, os
from ui_common import render_examples, render_input_area, render_output

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend")))
from langgraph_orchestration import get_graph

st.set_page_config(page_title="GenAI Multi-Agent Orchestration PoC", layout="wide")

# Apply light theme and minimal padding
st.markdown("""
    <style>
        .stApp {
            background-color: #ffffff;
            color: #000000;
            padding-top: 0.5rem;
        }
        .stButton > button {
            background-color: #f0f2f6;
            color: #2C6BED;
            border: 1px solid #2C6BED;
            margin-bottom: 0.5rem;
        }
        textarea, .stTextArea textarea, .stCodeBlock pre {
            background-color: #f8f9fa !important;
            color: #000000 !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 GenAI Multi-Agent PoC Demo")

render_examples()
input_text = render_input_area()

if st.button("🚀 Call Multi-Agent Routing System") or st.session_state.get("run_inference", False):
    st.session_state["run_inference"] = False
    if not input_text.strip():
        st.warning("Please enter or select an input.")
    else:
        st.write("### Input:")
        st.code(input_text, language="text")
        try:
            with st.spinner("Processing..."):
                graph = get_graph()
                result = graph.invoke({"text": input_text})
                if not isinstance(result, dict):
                    raise ValueError("Unexpected result format. Expected a dictionary.")
                output = result.get("text", "⚠️ No text field returned in result.")
            st.toast("✔️ Inference complete", icon="✨")
            render_output(output, result)
        except Exception as e:
            st.error(f"❌ An error occurred during inference: {e}")
