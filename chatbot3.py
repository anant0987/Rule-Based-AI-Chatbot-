import json
import os

# File used as chatbot database
memory_file = "chatbot_memory.json"

# Load old memory
if os.path.exists(memory_file):
    with open(memory_file, "r") as file:
        responses = json.load(file)
else:
    responses = {
        "hello": "Hello! How can I help you?",
        "hi": "Hi there!",
        "how are you": "I am good!",
        "what is your name": "I am Memory Bot."
    }


history = []

print("Chatbot: Hello! I have permanent memory.")
print("Type 'bye' to exit")
print("Type 'history' to view chat")


while True:

    user_input = input("You: ").lower()


    # Exit chatbot
    if user_input == "bye" or user_input == "exit":
        print("Chatbot: Saving my memory...")

        with open(memory_file, "w") as file:
            json.dump(responses, file)

        print("Chatbot: Goodbye!")
        break


    # Show history
    elif user_input == "history":
        print("\n--- Chat History ---")

        for message in history:
            print(message)

        print("-------------------")


    # Known question
    elif user_input in responses:

        bot_reply = responses[user_input]

        print("Chatbot:", bot_reply)

        history.append("You: " + user_input)
        history.append("Bot: " + bot_reply)


    # Learn new question
    else:

        print("Chatbot: I don't know this.")

        new_response = input(
            "Teach me the answer: "
        )

        responses[user_input] = new_response

        print("Chatbot: I learned it!")

        history.append("You: " + user_input)
        history.append(
            "Bot learned: " + new_response
        )