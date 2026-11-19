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
        "content": "You are an helpful freindly assistant. Answer in simple english and Roman urdu if user speaks urdu. Always start chat with 'bot : '."
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
        max_tokens=1000,
        stream = True
    )
    word = ""
    for chunk in response:
        bot_reply = chunk.choices[0].delta.content
        if bot_reply:
            print(bot_reply, end = "", flush=True)
            word += bot_reply
    print()

    #Save bot reply in memory
    messages.append({"role": "assistant", "content": word })
    