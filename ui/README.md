# Streamlit Demo UI

This directory contains the Streamlit application that serves as a demo UI for interacting with the backend FastAPI application.

## Setup Instructions

1. **Install Dependencies**:  
   Navigate to the `ui` directory and install the required packages using pip:
   ```
   pip install -r requirements.txt
   ```

2. **Run the Application**:  
   Start the Streamlit application by running:
   ```
   streamlit run app.py
   ```

3. **Access the UI**:  
   Open your web browser and go to [http://localhost:8501](http://localhost:8501) to access the demo UI.

## Usage

- Enter your text and a valid tenant key (must match one of the keys in the backend `.env` file's `VALID_TENANT_KEYS`).
- Click "Process" to send the text to the FastAPI backend for processing.
- Optionally, enable "Show agent trace/debug info" to view detailed trace and debug information from the backend.

## Directory Structure

- `app.py`: The main application file for interacting with the backend API.
- `demo.py`: A local demo that calls the orchestration graph directly (for development/testing).
- `ui_common.py`: Shared UI components for both apps.
- `requirements.txt`: Python dependencies for the Streamlit application.

## Notes

- Ensure the backend FastAPI server is running before using the UI.
- For any issues, please refer to the documentation or raise an issue on the GitHub repository.