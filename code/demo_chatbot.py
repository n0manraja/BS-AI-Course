# Simple Chatbot Demo (Lecture 1)
print("Simple AI Chatbot (type 'bye' to exit)")

while True:
    user = input("You: ")
    if "hello" in user.lower():
        print("AI: Hello! I am your AI assistant.")
    elif "how are you" in user.lower():
        print("AI: I am good, thank you! How can I help you?")
    elif "bye" in user.lower():
        print("AI: Goodbye! See you again.")
        break
    else:
        print("AI: I am still learning...")
