# Azure Deployment Guide for GenAI Multi-Agent Orchestration PoC

This guide provides step-by-step instructions to deploy both the backend (FastAPI) and frontend (Streamlit) components of your project as Azure Web Apps for Containers, using Azure Container Registry (ACR) and CI/CD with GitHub Actions.

---

## 1. Prerequisites

- Azure CLI installed ([Install Guide](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli))
- An active Azure subscription
- Your code pushed to a GitHub repository
- Dockerfiles already created in both `backend/` and `ui/` directories

---

## 2. Azure Resource Setup

### 2.1. Set Variables

```sh
# Example values used in this guide:
# Resource group and region
# RESOURCE_GROUP=genai-poc-rg
# LOCATION=canadacentral

# App Service Plan (shared by both apps)
# PLAN_NAME=genai-poc-plan

# Web App names (must be globally unique)
# BACKEND_APP=genai-backend
# UI_APP=genai-ui-2025

# Azure Container Registry (must be globally unique)
# ACR_NAME=genaiacr2025
```

### 2.2. Create Resource Group

```sh
az group create --name genai-poc-rg --location canadacentral
```

### 2.3. Create Azure Container Registry

```sh
az acr create --resource-group genai-poc-rg --name genaiacr2025 --sku Basic
```

### 2.4. Create App Service Plan

```sh
az appservice plan create \
  --name genai-poc-plan \
  --resource-group genai-poc-rg \
  --is-linux \
  --sku B1
```

### 2.5. Create Backend Web App for Containers

> **Important:** For container-based web apps, **do not use** the `--runtime` parameter.  
> You **must** specify the Docker image to use with `--deployment-container-image-name`.  
> If you are using GitHub Actions to deploy, you can use a placeholder image here (it will be replaced by your workflow).

```sh
az webapp create \
  --resource-group genai-poc-rg \
  --plan genai-poc-plan \
  --name genai-backend \
  --deployment-container-image-name mcr.microsoft.com/azure-app-service/python:3.11
```

### 2.6. Create UI Web App for Containers

```sh
az webapp create \
  --resource-group genai-poc-rg \
  --plan genai-poc-plan \
  --name genai-ui-2025 \
  --deployment-container-image-name mcr.microsoft.com/azure-app-service/python:3.11
```

---

## 3. Configure Environment Variables

Set all required environment variables (like `VALID_TENANT_KEYS`, `AZURE_OPENAI_KEY`, etc.) in Azure Portal for each Web App under **Configuration**.

Example (for backend):

```sh
az webapp config appsettings set \
  --resource-group genai-poc-rg \
  --name genai-backend \
  --settings VALID_TENANT_KEYS="demo_tenant_1,demo_tenant_2" \
             AZURE_OPENAI_KEY="your-azure-openai-key" \
             AZURE_OPENAI_ENDPOINT="https://your-endpoint.openai.azure.com" \
             AZURE_OPENAI_DEPLOYMENT="your-deployment-name" \
             AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

---

## 4. Link Web Apps to Azure Container Registry

This step allows your web apps to pull images from your ACR.

### 4.1. Get ACR Credentials

```sh
az acr credential show --name genaiacr2025
```
Note the `username` and `passwords[0].value`.

### 4.2. Link Backend Web App to ACR

```sh
az webapp config container set \
  --name genai-backend \
  --resource-group genai-poc-rg \
  --docker-custom-image-name genaiacr2025.azurecr.io/genai-backend:latest \
  --docker-registry-server-url https://genaiacr2025.azurecr.io \
  --docker-registry-server-user <ACR_USERNAME> \
  --docker-registry-server-password <ACR_PASSWORD>
```

### 4.3. Link UI Web App to ACR

```sh
az webapp config container set \
  --name genai-ui-2025 \
  --resource-group genai-poc-rg \
  --docker-custom-image-name genaiacr2025.azurecr.io/genai-ui:latest \
  --docker-registry-server-url https://genaiacr2025.azurecr.io \
  --docker-registry-server-user <ACR_USERNAME> \
  --docker-registry-server-password <ACR_PASSWORD>
```

---

## 5. Set Up CI/CD with GitHub Actions

### 5.1. Prepare Azure Publish Profiles and ACR Secrets

- In Azure Portal, go to each Web App (`genai-backend` and `genai-ui-2025`)
- Click **Get publish profile** and download the file for each app
- In your GitHub repo, go to **Settings > Secrets and variables > Actions**
- Add secrets:
  - `AZURE_BACKEND_PUBLISH_PROFILE` (contents of backend publish profile)
  - `AZURE_UI_PUBLISH_PROFILE` (contents of UI publish profile)
  - `ACR_LOGIN_SERVER` (e.g., `genaiacr2025.azurecr.io`)
  - `ACR_USERNAME` (from ACR credentials)
  - `ACR_PASSWORD` (from ACR credentials)

### 5.2. Create GitHub Actions Workflows

#### Backend Deployment Workflow

Save as `.github/workflows/deploy-backend.yml`:

#### UI Deployment Workflow

Save as `.github/workflows/deploy-ui.yml`:

---

## 6. Testing & Validation

- After a push to `main`, GitHub Actions will build and deploy both backend and UI images to ACR and update the Azure Web Apps.
- Access the deployed URLs from the Azure Portal.
- Test the UI by entering text and a valid tenant key.

---

## 7. Notes & Best Practices

- Never commit your `.env` file or secrets to source control.
- Use Azure App Service Configuration for all secrets and environment variables.
- Monitor deployments and logs in the Azure Portal for troubleshooting.

---

**You are now ready to deploy and manage your GenAI PoC on Azure with full confidence!**