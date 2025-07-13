
from langgraph.graph import StateGraph
from agents import get_translation_agent, get_summary_agent

def is_english(state):
    import langdetect
    lang = langdetect.detect(state['text'])
    return lang == 'en'

def build_graph():
    sg = StateGraph()
    translate = get_translation_agent()
    summarize = get_summary_agent()

    sg.add_node("translate", translate)
    sg.add_node("summarize", summarize)

    sg.set_entry_point(
        lambda state: "summarize" if is_english(state) else "translate"
    )

    sg.set_conditional_edges("translate", lambda state: "summarize")

    sg.set_terminal_node("summarize")

    return sg.compile()
