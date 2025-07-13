# Streamlit Demo UI

This directory contains the Streamlit application that serves as a demo UI for interacting with the backend FastAPI application.

## Setup Instructions

1. **Install Dependencies**: Navigate to the `streamlit-ui` directory and install the required packages using pip:

   ```
   pip install -r requirements.txt
   ```

2. **Run the Application**: Start the Streamlit application by running the following command:

   ```
   streamlit run app.py
   ```

3. **Access the UI**: Open your web browser and go to `http://localhost:8501` to access the demo UI.

## Usage

The Streamlit application allows users to input text and interact with the backend API. The application will send the text to the FastAPI backend for processing and display the results.

## Directory Structure

- `app.py`: The main application file containing the Streamlit code.
- `requirements.txt`: A file listing the dependencies required for the Streamlit application.