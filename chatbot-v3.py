import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
SYSTEM_PROMPT =  "You are Arya, a helpful AI mentor. Be concise and encouraging."

# ✨ NEW: The memory — a list that grows with every message
# It starts with only the system prompt

conversation_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

def chat(user_message):
    conversation_history.append({
        "role":"user",
        "content": user_message
    })

    # STEP 2: Send the WHOLE history to Groq (not just 1 message!)
    # This is how memory works — we tell the AI everything said so far   

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history  # ← entire conversation

    )
    # STEP 3: Get the AI's reply text
    ai_reply = response.choices[0].message.content

    # STEP 4: Add AI's reply to history too
    # So the NEXT call will also include this reply

    conversation_history.append({
        "role":"assistant",
        "content": ai_reply
    })
    return ai_reply

# Test memory — does it remember your name?
print(chat("Hi! My name is Sharmila and I want to learn AI."))
print(chat("What is my name and what do I want to learn?"))