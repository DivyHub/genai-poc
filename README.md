# GenAI Multi-Agent Orchestration PoC

This project consists of two main components: a backend FastAPI application and a Streamlit demo UI. Below is an overview of the project structure and instructions for setting up each component.

## Project Structure

```
genai-poc
├── backend
│   ├── main.py
│   ├── requirements.txt
│   ├── utils.py
│   ├── langgraph_orchestration.py
│   ├── agents.py
│   ├── .env
│   └── README.md
├── ui
│   ├── app.py
│   ├── demo.py
│   ├── ui_common.py
│   ├── requirements.txt
│   └── README.md
└── README.md
```

## Backend FastAPI Application

### Setup Instructions

1. Navigate to the `backend` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create and configure your `.env` file (see `backend/.env` for example).
4. Run the FastAPI application:
   ```
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

### Usage

- The backend exposes a POST endpoint at `/process` that accepts JSON input:
  - **Body:** `{"text": "Your text here"}`
  - **Header:** `tenant-key: <your-tenant-key>` (must match one of the keys in `.env`'s `VALID_TENANT_KEYS`)
- The response includes the processed output, trace, and debug information.

## Streamlit Demo UI

### Setup Instructions

1. Navigate to the `ui` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```
   streamlit run app.py
   ```

### Usage

- Enter your text and a valid tenant key (from the backend `.env` file).
- Click "Process" to send the text to the FastAPI backend for processing.
- Optionally, enable "Show agent trace/debug info" to view detailed trace and debug information from the backend.
- You can also use `demo.py` to test the orchestration graph directly without the backend.

## Conclusion

This project provides a complete setup for a FastAPI backend and a Streamlit frontend, enabling users to process text and visualize the results easily.