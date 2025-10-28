print(" ChatBot: Hello! I'm your simple chatbot.")
print("You can talk to me! (You can Type 'bye' to end Conversation With Me)\n")

users_name = ""
while True:
    users_input = input("You: ").lower()

    if "bye" in users_input:
        print(" ChatBot: Bye! Take care ")
        break

    elif "my name is" in users_input:
        users_name = users_input.split("is")[-1].strip().capitalize()
        print(f" ChatBot: Nice to meet you, {users_name}!")

    elif "How are you" in users_input:
        print(" ChatBot: I'm fine! How about you?")

    elif "fine" in users_input:
        print(" ChatBot: Glad to hear that!")

    elif " what is your name" in users_input:
        print(" ChatBot: I'm a simple chatbot made using Python.")

    elif "yours age" in users_input:
        print(" ChatBot: I don't have an age, I'm just a few lines of code!")

    elif " Tell Me a Joke" in users_input:
        print(" ChatBot: Why did the computer go to therapy? Because it had too many bugs!")

    elif "time" in users_input:
        from datetime import datetime
        now = datetime.now()
        print(" ChatBot: time is", now.strftime("%I:%M %p"))

    elif "Thank You" in users_input:
        print(" ChatBot: My Pleasure!")

    elif "whats the weather?" in users_input:
        print(" ChatBot: I’m not sure, but I hope it’s nice where you are!")

    else:
        print(" ChatBot: Sorry, I didn’t understand that. Can you ask something else?")
