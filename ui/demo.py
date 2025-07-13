# ui/demo.py
import streamlit as st
import sys, os
from streamlit_extras.stylable_container import stylable_container

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
st.markdown("""
Welcome to the Cloud-based GenAI Multi-Agent Orchestration Proof-of-Concept application. Select a prebuilt example below or enter your own text to see how the model responds.
""")

# Prebuilt examples
examples = {
    "English Text": "This is a simple test in English.",
    "French Text": "Ceci est une phrase en français.",
    "Mixed Language": "Here is a sentence with français included.",
    "Non-ASCII Characters": "こんにちは、元気ですか？",
    "Special Characters": "@#$%^&*!()_+",
    "Empty Input": ""
}

st.header("👩🏻‍🔬 Prebuilt Examples")
cols = st.columns(3)
for idx, (label, example_text) in enumerate(examples.items()):
    col = cols[idx % 3]
    with col:
        with stylable_container(
            "container_" + label,
            css_styles="""
                margin-bottom: 1rem;
                border: 1px solid #eee;
                padding: 0.5rem;
                border-radius: 6px;
                background-color: #f9f9f9;
            """
        ):
            st.markdown(f"**{label}**")
            st.code(example_text, language="text")
            if st.button(f"Use Example", key=f"btn_{label}"):
                st.session_state["input_text"] = example_text
                st.session_state["run_inference"] = True

st.markdown("---")

st.header("✍️ Or enter your own input")

# Input area with session state
if "input_text" not in st.session_state:
    st.session_state["input_text"] = ""

input_text = st.text_area("Custom Input", value=st.session_state["input_text"], height=70)
st.session_state["input_text"] = input_text

if st.button("🚀 Call Multi-Agent Routing System"):
    st.session_state["run_inference"] = True

# Execute inference
if st.session_state.get("run_inference", False):
    if not st.session_state["input_text"].strip():
        st.warning("Please enter or select an input.")
        st.session_state["run_inference"] = False
    else:
        st.write("### Input:")
        st.code(st.session_state["input_text"], language="text")

        try:
            with st.spinner("Processing..."):
                graph = get_graph()
                result = graph.invoke({"text": st.session_state["input_text"]})

                if not isinstance(result, dict):
                    raise ValueError("Unexpected result format. Expected a dictionary.")

                output = result.get("text", "⚠️ No text field returned in result.")

            st.toast("✔️ Inference complete", icon="✨")

            st.write("### Output:")
            st.code(output, language="text")

            st.download_button("📄 Copy Output", output, file_name="output.txt")

            st.markdown("#### 📋 Full Result Dictionary")
            with st.expander("Expand for details"):
                st.json(result)

            if "trace" in result:
                st.markdown("#### 🧵 Trace of Agent Decisions")
                for step in result["trace"]:
                    name = step.get("name", "Unnamed")
                    content = step.get("content", "No content available")
                    with st.container():
                        st.markdown(f"**{name}**")
                        st.code(content, language="text")

        except Exception as e:
            st.error(f"❌ An error occurred during inference: {e}")

        st.session_state["run_inference"] = False
