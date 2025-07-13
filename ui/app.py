import streamlit as st
import requests
from ui_common import render_examples, render_input_area, render_output

# Define the FastAPI backend URL
BACKEND_URL = "https://genai-backend.azurewebsites.net/process"
# BACKEND_URL = "http://localhost:8000/process"  # Uncomment for local testing

# Streamlit application
st.title("GenAI Multi-Agent Orchestration PoC")

render_examples()
input_text = render_input_area()

# Use a regular text input for tenant_key to avoid browser password prompts
tenant_key = st.text_input("Tenant Key (for demo, not hidden)", type="default")

# Option to enable tracing/debugging
show_trace = st.checkbox("Show agent trace/debug info", value=True)

if st.button("Process") or st.session_state.get("run_inference", False):
    st.session_state["run_inference"] = False
    if input_text and tenant_key:
        try:
            response = requests.post(
                BACKEND_URL,
                json={"text": input_text},
                headers={"tenant-key": tenant_key}  # <-- corrected header name
            )
            result = response.json()
            if response.status_code == 200 and "error" not in result:
                output = result.get("text", "⚠️ No text field returned in result.")
                st.success("Processing successful!")
                render_output(output, result if show_trace else None)
            else:
                st.error(f"Error: {result.get('error', 'Unknown error')}")
                if show_trace:
                    if "debug" in result:
                        st.markdown("#### Debug Info")
                        st.json(result["debug"])
                    if "trace" in result and result["trace"]:
                        st.markdown("#### Trace Info")
                        st.json(result["trace"])
        except Exception as e:
            st.error(f"Request failed: {e}")
    else:
        st.warning("Please enter both text and tenant key.")