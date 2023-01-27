from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new instance of a chat bot
bot = ChatBot('Cleo')

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
trainer = ListTrainer(bot)
trainer.train(conversation)

print("\n===============================================")
print(f"\nHi, my name is 🤖{bot.name}. How can I help you?\n")

# Define exit conditions
exit_conditions = (":q", "quit", "exit")

# Define conversation structure
while True:
    try:
        query = input("Human: ")
        if query in exit_conditions:
            print("Goodbye!")
            break
        else:
            print(f"🤖{bot.name}: {bot.get_response(query)}")
    except (KeyboardInterrupt, EOFError, SystemError):
        break





