import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("key"))

print(" Chatbot using Groq  ")
print ("Press q to exit")

# Memory to remember that 
messages = [
    {
        "role" : "system",
        "content": "You are an helpful freindly assistant. Answer in simple english and Roman urdu if user speaks urdu."
    }
]

while True:
    user_input = input("You: ")

    if user_input.lower() in ["q", "exit", "quit", "bye"]:
        print("Bot: Allah Hafiz! See you next time.")
        break
    
    messages.append({
        "role": "user", 
        "content": user_input
    })

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        temperature=0.7,
        max_tokens=1000
    )

    bot_reply = response.choices[0].message.content
    print(f"Bot: {bot_reply}\n")

    #Save bot reply in memory
    messages.append({"role": "assistant", "content": bot_reply })
    