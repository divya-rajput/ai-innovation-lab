import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Azure client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("API_VERSION")
)

request = (
    "Please come up with a challenging, nuanced question that I can ask a number of LLMs "
    "to evaluate their intelligence. Answer only with the question, no explanation."
)

messages = [{"role": "user", "content": request}]

print("Let's start!!!!")
print("Select which model you want to use:")
print("1: Deepseek")
print("2: GPT-4.1")
print("3: Phi-4")
print("4: GPT-5.2-chat")

option = input("Enter your option: ").strip()

if option == "1":
    model_name = "DeepSeek-R1"
elif option == "2":
    model_name = "gpt-4.1-mini"
elif option == "3":
    model_name = "Phi-4"
else:
    model_name = "gpt-5.2"

response = client.chat.completions.create(
    model=model_name,
    messages=messages
)

print(response.choices[0].message.content)