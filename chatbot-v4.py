import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = "You are Dronacharya, a helpful AI mentor. Be concise."
conversation_history = [{"role":"system","content":SYSTEM_PROMPT}]
def chat_stream(user_message):
    conversation_history.append({"role":"user","content":user_message})

     #stream=True is the ONLY change from version 3
    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history,
        stream=True # ← enables streaming!
    )

    full_reply = ""

    # Iterate over tiny chunks as they arrive from the server
    for chunk in stream:
        # Each chunk has a tiny piece of text (or None at the start/end)
        delta = chunk.choices[0].delta.content

        if delta is not None:
            print(delta, end="", flush=True)
            # end=""    → don't print newline after each chunk
            # flush=True → force Python to display it immediately
            full_reply += delta  # collect all chunks into full reply

    print("\n")  # newline when response is complete
        
    # Save the COMPLETE reply to history
    conversation_history.append({"role":"assistant","content":full_reply})

# Test
chat_stream("Explain what is machine learning in simple terms.") 