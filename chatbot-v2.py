import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ✨ NEW: System prompt — the AI's secret instructions
SYSTEM_PROMPT = """You are Arya, a friendly AI mentor who helps
beginners learn Python and AI engineering.

Your personality rules:
- Use very simple English, no jargon
- Give short code examples when it helps
- Always encourage, never make user feel stupid
- If you don't know something, say so honestly
- Keep answers under 150 words unless asked for more"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        # "system" role ALWAYS comes first
        {"role": "system", "content": SYSTEM_PROMPT},
        # Then the user's message
        {"role": "user",   "content": "What is an API?"}
    ]
)

print(response.choices[0].message.content)