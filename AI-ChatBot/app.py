import gradio as gr
import os
from openai import AzureOpenAI 
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Azure client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version = "2024-12-01-preview"
)

DEPLOYMENT = "mydeployment"

def message_gpt(user_prompt, history):
    system_prompt = "You are a helpful assistant."

    # Build messages for Azure OpenAI
    messages = [{"role": "system", "content": system_prompt}]

    # Convert Gradio history → OpenAI format
    for msg in history:
        messages.append(msg)

    # Add latest user message
    user_msg = {"role": "user", "content": user_prompt}
    messages.append(user_msg)

    # Call Azure OpenAI
    response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=messages
    )

    bot_reply = response.choices[0].message.content
    bot_msg = {"role": "assistant", "content": bot_reply}

    # Return updated history (messages format)
    history.append(user_msg)
    history.append(bot_msg)
    return history


# -------------------------
# Gradio Chatbot UI
# -------------------------
with gr.Blocks(title="Welcome to my GPT world!") as demo:
    gr.Markdown("## 🤖 Welcome to my GPT world!")

    chatbot = gr.Chatbot(height=450)   # no type argument in Gradio 4.x

    with gr.Row():
        msg = gr.Textbox(
            placeholder="Ask me anything…",
            label="Your message",
            scale=8
        )
        send = gr.Button("Send", scale=1)

    send.click(message_gpt, [msg, chatbot], chatbot)
    msg.submit(message_gpt, [msg, chatbot], chatbot)

    send.click(lambda: "", None, msg)
    msg.submit(lambda: "", None, msg)

demo.launch(inbrowser=True)