
def get_response(message):
    message = message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hi! How can I help you today?"

    elif "how are you" in message:
        return "I'm fine, thanks! How about you?"

    elif "your name" in message:
        return "I'm a simple chatbot made for a CodeAlpha task."

    elif "help" in message:
        return "You can say hello, ask how I am, ask my name, or say bye."

    elif message in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand that. Try saying 'help'."


def main():
    print("Chatbot: Hello! Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit"]:
            break


if __name__ == "__main__":
    main()