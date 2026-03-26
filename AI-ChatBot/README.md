# AI Chatbot (Azure OpenAI + Gradio)

A simple chatbot built using **Gradio** and **Azure OpenAI**.  
It loads credentials from a `.env` file and opens a chat interface in your browser.

---

## Setup

### 1. Install dependencies
```bash
pip install gradio python-dotenv openai
```

### 2. Create a .env file
AZURE_OPENAI_API_KEY=your_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource.cognitiveservices.azure.com/

### 3. Update your deployment name 
DEPLOYMENT = "mydeployment"

### 4. Run the app
python app.py

Gradio will open the chatbot in your browser.

## What it does?
- Loads Azure OpenAI credentials from .env
- Sends user messages to Azure OpenAI
- Displays responses in a simple Gradio chat UI
