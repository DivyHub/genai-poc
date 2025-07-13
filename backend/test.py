from langgraph_orchestration import get_graph

graph = get_graph()

def run_test(input_text, expected_output_substring=None):
    print("\n🧪 Test Input:", input_text)
    result = graph.invoke({"text": input_text})
    output_text = result["text"]
    trace = result.get("trace", [])

    print("✅ Output:", output_text)
    print("🧵 Trace:")
    for step in trace:
        print(f"  - [{step['name']}] {step['content']}")

    if expected_output_substring:
        assert expected_output_substring.lower() in output_text.lower(), (
            f"❌ Test failed: Expected '{expected_output_substring}' in output"
        )
    assert isinstance(trace, list) and len(trace) >= 2, "❌ Trace should include router and tool steps"
    print("✅ Trace contains expected steps.\n")


def test_english_input():
    run_test("This is a test message in English.", expected_output_substring="summary")

def test_non_english_input():
    run_test("Ceci est un message en français.", expected_output_substring="english")

def test_mixed_input():
    run_test("Here is a sentence avec des mots en français.", expected_output_substring="english")

if __name__ == "__main__":
    test_english_input()
    test_non_english_input()
    test_mixed_input()
