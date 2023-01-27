# https://chatterbot.readthedocs.io/en/stable/tutorial.html
# After creating a new ChatterBot instance it is also possible to train the bot
# Training is a good way to ensure that the bot starts off with knowledge about specific responses
# pip install chatterbot 
# If the above command doesnt work, try installing the actual version or a version below (aacording to stackoverflow)
# e.g pip install chatterbot==1.0.4
# ChatterBotCorpusTrainer has a number of language options
# The training via ChatterBotCorpusTrainer is based on pre-defined yml files
# Yml files are located here .../opt/anaconda3/lib/python3.9/site-packages/chatterbot_corpus/data/
# Custom files can also be used for training the ChatBot via ChatterBotCorpusTrainer

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new instance of a chat bot
bot = ChatBot('Cleo', storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3')

trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    "chatterbot.corpus.english"
)

# Define entrance text
print("\n===============================================")
print(f"\nHi, my name is 🤖{bot.name}. How can I help you?\n")

# Define exit conditions
exit_conditions = (":q", "quit", "exit")

# Define conversation structure
while True:
    try:
        query = input("Human: ")
        if query in exit_conditions:
            print(f"🤖{bot.name}: Have a nice day!")
            print("\n===============================================\n")
            break
        else:
            print(f"🤖{bot.name}: {bot.get_response(query)}")
    except (SystemError, EOFError, KeyboardInterrupt):
        break
