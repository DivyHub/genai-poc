# Backend FastAPI Application

This directory contains the FastAPI backend application for processing text input and interacting with a graph-based system.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd genai-poc/backend
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the FastAPI application**:
   ```
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## API Endpoints

### POST /process

- **Description**: Processes the input text and returns the output based on the detected language and orchestration logic.
- **Request Body**: 
  - `text`: The text to be processed.
- **Headers**:
  - `tenant-key`: Your tenant key for authentication (must match one of the keys in the `.env` file's `VALID_TENANT_KEYS`).
- **Response**: Returns the processed output, trace, and debug information.

## Usage Example

To test the API, you can use tools like `curl` or Postman. Here’s an example using `curl`:

```bash
curl -X POST "http://localhost:8000/process" -H "tenant-key: demo_tenant_1" -H "Content-Type: application/json" -d '{"text": "Your text here"}'
```

## Additional Information

- Ensure that all dependencies are correctly installed as listed in `requirements.txt`.
- The backend code is in the `backend` folder. The Streamlit UI is in the `ui` folder.
- For any issues, please refer to the documentation or raise an issue in the repository.