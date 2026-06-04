import os, sys, json
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from rich.console import Console
from rich.panel import Panel

# Load config from .env 
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
console = Console()

MODEL = os.getenv("MODEL_NAME","llama-3.3-70b-versatile")
MAX_HISTORY = int(os.getenv("MAX_HISTORY", 20))
HISTORY_FILE = Path("chat_history.json")

MODEL = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
MAX_HISTORY = int(os.getenv("MAX_HISTORY","20"))
HISTORY_FILE = Path("chat_history.json")

#---System Prompt - AI's personality ----
SYSTEM_PROMPT = """ You are Dronacharya, a friendly expert AI engineering mentor.
You help beginners learn Python and AI/ML concepts from scratch.

Ypur rules:
- Use simple English - explain like teaching a 16- year-old
- Give short, working code examples when helpful
- Be warm, patient, and encouraging always
- keep responses under 200 words unless the user asks for detail
- If you don't know something, say "I'm not sure, let me think..."
- Start your first message by asking the user's name
"""

#--- Conversation memory start with System prompt ---
conversation_history = [
    {"role":"system","content":SYSTEM_PROMPT}
]

#--- Helper: save chat to JSON file-------
def save_history():
    with open(HISTORY_FILE, "w") as f:
        json.dump(conversation_history[1:], f, indent=2) # skip system

#--- Helper: Load previous chat from JSON file -------
def load_history():
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE) as f:
            return json.load(f)
    return []

#--- Helper: trim old messages to stay within limits ----
def trim_history():
    # Keep system prompt (index 0) + last MAX_HISTORY messages
    if len(conversation_history)>MAX_HISTORY + 1:
        conversation_history[1:] = conversation_history[-MAX_HISTORY]

#--- Main chat function -----------------
def chat(user_input: str)-> None:
    """Send message to Groq and stream the response."""

    #Add user message to history
    conversation_history.append({"role":"user", "content": user_input})
    trim_history()

    try:
        #Call Groq API with full conversation history + streaming
        stream = client.chat.completions.create(
            model=MODEL,
            messages=conversation_history,
            stream=True,
            temperature=0.7, # 0=focused/precise, 1=creative/random
            max_tokens=1024  # max length of response
        )

        console.print("\n[bold green]Dronacharya:[/bold green] ", end="")
        full_reply = ""

        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                console.print(delta, end="")
                full_reply += delta

        console.print("\n")

        # Save AI reply to history
        conversation_history.append({"role": "assistant", "content": full_reply})

        #Persist to file
        save_history()
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted.[/yellow]\n")
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]\n")

#--- Main program loop -------------------
def main():
    # Load previous conversation if it exists
    conversation_history.extend(load_history())

    # Welcome banner using rich
    console.print(Panel(
        "[bold green]Dronacharya - Your AI mentor[/bold green]\n"
        f"[dim]Model: {MODEL} via Groq (Free Tier)[/dim]\n"
        "[dim]Commands: /help /clear /history quit[/dim]",
        border_style="green", padding=(0, 1)
    ))
    while True:   # infinite loop until user types quit
        try:
            # Get user input — the [bold cyan] adds color via rich
            user_input = console.input("\n[bold cyan]You:[/bold cyan] ").strip()

            # Skip empty messages
            if not user_input:
                continue

            # Handle slash commands
            if user_input.lower() in ("quit", "exit", "q"):
                console.print("[dim]Goodbye! Keep building 🚀.[/dim]")
                sys.exit(0)
            
            elif user_input == "/clear":
                conversation_history[1:] = []   # reset memory (keep system)
                HISTORY_FILE.unlink(missing_ok=True)
                console.print("[dim]Memory cleared.[/dim]")

            elif user_input == "/history":
                count = len(conversation_history)-1
                console.print(f"[dim]{count} messages in memory[/dim]")

            elif user_input == "/model":
                console.print(f"[dim]Using: {MODEL} on Groq (Free)[/dim]")

            elif user_input == "/help":
                console.print("""
[bold]Available commands:[/bold]
 /help  -> show this menu
/clear  -> wipe memory and start fresh
/history -> show how many messages are in memory
/medel  -> show which AI model is being used
quit     -> exit the chatbot                    
                """)
            
            else:
                # Normal message → send to AI
                chat(user_input)

        except KeyboardInterrupt:
            console.print("\n[dim]Use 'quit to exit properly[/dim]")

# This runs main() only when you run the file directly
# (not when it's imported as a module)

if __name__ == "__main__":
    main()     
