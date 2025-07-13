# agents.py
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
subscription_key = os.getenv("AZURE_OPENAI_KEY")
api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview")

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

def summarize(input_dict):
    text = input_dict['text']
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Summarize this text."},
            {"role": "user", "content": text}
        ],
        max_tokens=800,
        temperature=0.7,
        model=deployment
    )
    return {"text": "Summary: " + response.choices[0].message.content}

def translate(input_dict):
    text = input_dict['text']
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Translate this text to English."},
            {"role": "user", "content": text}
        ],
        max_tokens=800,
        temperature=0.7,
        model=deployment
    )
    return {"text": "English: " + response.choices[0].message.content}

def get_summary_agent():
    return summarize

def get_translation_agent():
    return translate
