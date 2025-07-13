
def get_summary_agent():
    from langgraph.graph import ToolNode
    import openai

    def summarize(input_dict):
        text = input_dict['text']
        response = openai.ChatCompletion.create(
            model="gpt-35-turbo",
            messages=[
                {"role": "system", "content": "Summarize this text."},
                {"role": "user", "content": text}
            ]
        )
        return {"text": response.choices[0].message['content']}

    return ToolNode(summarize)

def get_translation_agent():
    from langgraph.graph import ToolNode
    import openai

    def translate(input_dict):
        text = input_dict['text']
        response = openai.ChatCompletion.create(
            model="gpt-35-turbo",
            messages=[
                {"role": "system", "content": "Translate this text to English."},
                {"role": "user", "content": text}
            ]
        )
        return {"text": response.choices[0].message['content']}

    return ToolNode(translate)
