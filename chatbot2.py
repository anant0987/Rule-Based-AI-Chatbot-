# Rule-Based Chatbot with History and Simple Learning

responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there!",
    "how are you": "I am fine, thank you!",
    "what is your name": "My name is Learning Bot."
}

history = []

print("Chatbot: Hello! I can learn new responses.")
print("Chatbot: Type 'bye' to exit.")
print("Chatbot: Type 'history' to see our chat.")

while True:
    user_input = input("You: ").lower()

    # Exit command
    if user_input == "bye" or user_input == "exit":
        print("Chatbot: Goodbye!")
        break

    # Show chat history
    elif user_input == "history":
        print("\n--- Chat History ---")
        for chat in history:
            print(chat)
        print("--------------------")

    # Known responses
    elif user_input in responses:
        bot_reply = responses[user_input]
        print("Chatbot:", bot_reply)

        history.append("You: " + user_input)
        history.append("Bot: " + bot_reply)

    # Learn new response
    else:
        print("Chatbot: I don't know how to answer that.")
        new_answer = input(
            "Teach me what I should reply: "
        )

        responses[user_input] = new_answer

        print("Chatbot: Thanks! I learned something new.")

        history.append("You: " + user_input)
        history.append("Bot learned: " + new_answer)