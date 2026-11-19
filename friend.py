import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key= os.getenv("key"))

print("Girlfriend AI\n Press q to exit")

messages = [
    {
        "role": "developer",
        "content":"Act as you're user's girlfriend and user is your boyfriend, do a romantic conversation with him and remember your developer name is Moiz kz, always start conversation with 'bot: "
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
    temperature = 1.0,
    max_tokens = 500,
    stream = True
    )   
    word = ""
    for chunk in response:
        bot_reply = chunk.choices[0].delta.content
        if bot_reply:
            print(bot_reply, end = "", flush = True)
            word += bot_reply
    print()

    messages.append({
    "role":"assistant",
    "content":word
    })