print("Chatbot: Hello! I am your chatbot.")
print("Chatbot: Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Chatbot: Hello! How can I help you?")

    elif user_input == "good morning":
        print("Chatbot: Good morning! Have a great day!")

    elif user_input == "how are you":
        print("Chatbot: I am fine, thank you!")

    elif user_input == "what is your name":
        print("Chatbot: My name is Simple Bot.")

    elif user_input == "what can you do":
        print("Chatbot: I can answer some predefined questions.")

    elif user_input == "bye" or user_input == "exit":
        print("Chatbot: Goodbye! See you again.")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")
