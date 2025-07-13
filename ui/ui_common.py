import streamlit as st

EXAMPLES = {
    "English Text": "This is a simple test in English.",
    "French Text": "Ceci est une phrase en français.",
    "Mixed Language": "Here is a sentence with français included.",
    "Non-ASCII Characters": "こんにちは、元気ですか？",
    "Special Characters": "@#$%^&*!()_+",
    "Empty Input": ""
}

def render_examples():
    st.header("👩🏻‍🔬 Prebuilt Examples")
    cols = st.columns(3)
    for idx, (label, example_text) in enumerate(EXAMPLES.items()):
        col = cols[idx % 3]
        with col:
            st.markdown(f"**{label}**")
            st.code(example_text, language="text")
            if st.button(f"Use Example", key=f"btn_{label}"):
                st.session_state["input_text"] = example_text
                st.session_state["run_inference"] = True

def render_input_area():
    st.markdown("---")
    st.header("✍️ Or enter your own input")
    if "input_text" not in st.session_state:
        st.session_state["input_text"] = ""
    input_text = st.text_area("Custom Input", value=st.session_state["input_text"], height=70)
    st.session_state["input_text"] = input_text
    return input_text

def render_output(output, result=None):
    st.write("### Output:")
    st.code(output, language="text")
    # Custom CSS for consistent button styling
    st.markdown("""
        <style>
        .stDownloadButton button {
            background-color: #f0f2f6;
            color: #2C6BED;
            border: 1px solid #2C6BED;
            margin-bottom: 0.5rem;
        }
        </style>
    """, unsafe_allow_html=True)
    st.download_button("📄 Copy Output", output, file_name="output.txt", key="copy_output_btn")
    if result:
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