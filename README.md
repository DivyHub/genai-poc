
# GenAI Proof of Concept (PoC)

This project is a simple FastAPI-based backend orchestrating translation and summarization using LangGraph and Azure OpenAI. It supports API-key based multi-tenant access.

## Setup Instructions

1. Create a new GitHub repo and push this code.
2. Add your Azure Web App publish profile as a secret:
   - `AZURE_WEBAPP_NAME`
   - `AZURE_WEBAPP_PUBLISH_PROFILE`
3. Push to `main` and GitHub Actions will deploy your app to Azure.

### API Endpoint

POST `/process`

```json
{
  "text": "Bonjour, ceci est un exemple."
}
```

Headers:

```
x-api-key: <your-api-key>
```
