# ============================================
# Step 1: Make your first Groq API call
# ============================================

import os
from dotenv import load_dotenv
from groq import Groq

# load_dotenv() reads your .env file and puts
# GROQ_API_KEY into the environment so os.getenv() can find it
load_dotenv()

# Create a Groq "client" — this object handles all
# the communication with Groq's servers for you
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Send a message and get a response
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",   # which AI model to use
    messages=[               # conversation — list of message dicts
        {
            "role": "user",  # "user" = the human speaking
            "content": "What is Python? Explain in 2 sentences."
        }
    ]
)

# Dig into the response object to get the text
# response → choices → first choice → message → content
answer = response.choices[0].message.content
print(answer)