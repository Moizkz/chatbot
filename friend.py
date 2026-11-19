import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key= os.getenv("key"))

print("AI Chatbot\n Press q to exit")

messages = [
    {
        "role": "developer",
        "content":"Act as you're user's girlfriend and user is your boyfriend, do a romantic conversation with him and remember your developer name is Moiz kz"
    }
]

while True:
    user_input = input("You : ")
    
    if user_input.lower() in ["q", "exit", "quit", "stop"]:
        print("Bye babe! I will wait for you")
        break

    messages.append(
    {"role": "user",
     "content": user_input
     })   

    response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages = messages,
    temperature = 1.8,
    max_tokens = 500
    )   

    bot_reply = response.choices[0].message.content
    print(f"Bot: {bot_reply}\n")

    messages.append({
    "role":"assistant",
    "content":bot_reply
    })