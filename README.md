# Azure Web Apps Project

This project consists of two main components: a backend FastAPI application and a Streamlit demo UI. Below is an overview of the project structure and instructions for setting up each component.

## Project Structure

```
azure-webapps-project
├── backend
│   ├── main.py                # FastAPI application with text processing endpoint
│   ├── requirements.txt       # Dependencies for the backend application
│   ├── utils.py               # Utility functions, including language detection
│   ├── langgraph_orchestration.py # Logic for interacting with the graph
│   └── README.md              # Documentation for the backend application
├── streamlit-ui
│   ├── app.py                 # Streamlit application code for the demo UI
│   ├── requirements.txt       # Dependencies for the Streamlit application
│   └── README.md              # Documentation for the Streamlit demo UI
└── README.md                  # Main documentation for the entire project
```

## Backend FastAPI Application

### Setup Instructions

1. Navigate to the `backend` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the FastAPI application:
   ```
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

### Usage

- The backend exposes a POST endpoint at `/process` that accepts text input and an API key for processing.

## Streamlit Demo UI

### Setup Instructions

1. Navigate to the `streamlit-ui` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```
   streamlit run app.py
   ```

### Usage

- The Streamlit UI allows users to interact with the backend API and visualize the results.

## Conclusion

This project provides a complete setup for a FastAPI backend and a Streamlit frontend, enabling users to process text and visualize the results easily.