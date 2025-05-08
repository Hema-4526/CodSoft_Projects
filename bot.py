import re
import random
from datetime import datetime

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if re.search(r"\b(hi|hello|hey|hii|hola)\b", user_input):
        return random.choice([
            "Hi there! 😊",
            "Hello! How can I help you today?",
            "Hey! What's up?"
        ])

    # Name or identity
    elif re.search(r"\b(your name|who are you|what are you)\b", user_input):
        return "I'm ChatBuddy, your friendly chatbot! 🤖"

    # How are you
    elif "how are you" in user_input:
        return random.choice([
            "I'm great! Thanks for asking.",
            "Doing well! How about you?",
            "As good as a bot can be!"
        ])

    # Time
    elif "time" in user_input:
        return f"The current time is {datetime.now().strftime('%I:%M %p')}."

    # Date
    elif "date" in user_input:
        return f"Today's date is {datetime.now().strftime('%A, %d %B %Y')}."

    # Weather
    elif re.search(r"\b(weather|hot|cold|rain|sunny)\b", user_input):
        return "I'm not connected to a weather service yet, but it's always sunny in my code world! ☀️"

    # Jokes
    elif "joke" in user_input:
        jokes = [
            "Why did the programmer quit his job? Because he didn’t get arrays (a raise)! 😂",
            "Why do Java developers wear glasses? Because they don’t C#! 🤓",
            "Why was the computer cold? Because it left its Windows open! ❄️"
        ]
        return random.choice(jokes)

    # Math calculations (very basic)
    elif re.search(r"(\d+)\s*([\+\-\*/])\s*(\d+)", user_input):
        match = re.search(r"(\d+)\s*([\+\-\*/])\s*(\d+)", user_input)
        a, op, b = int(match.group(1)), match.group(2), int(match.group(3))
        result = eval(f"{a}{op}{b}")
        return f"The result is: {result}"

    # Thank you
    elif "thank" in user_input:
        return "You're very welcome! 😊"

    # Goodbye
    elif re.search(r"\b(bye|goodbye|see you|exit|quit)\b", user_input):
        return "Goodbye! It was great talking to you. 👋"

    # Help
    elif "help" in user_input:
        return "I can tell jokes, do basic math, tell you the time, and chat casually. Just ask me!"

    # Default response
    else:
        return "Hmm... I'm not sure how to respond to that yet. Can you try rephrasing it?"

# Chat loop
print("🤖 ChatBuddy: Hello! I'm here to chat. Type 'bye' to end.")
while True:
    user_input = input("You: ")
    if user_input.lower().strip() in ["bye", "exit", "quit"]:
        print("ChatBuddy: Goodbye! 👋")
        break
    response = chatbot_response(user_input)
    print("ChatBuddy:", response)
