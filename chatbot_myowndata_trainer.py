from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new instance of chat bot
bot = ChatBot('ChatBot')

# Train ChatBot as per mydata.yml
# Save a custom yml file in the corpus data location specified below
# Yml file location path: .../opt/anaconda3/lib/python3.9/site-packages/chatterbot_corpus/data/custom/mydata.yml
# In yml file: Human questions are after '- -' , ChatBot responses are after '-'
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.custom.mydata')

# Define exit conditions
exit_conditions = ("bye", "goodbye", "bye-bye")

# Define conversation structure
while True:
    try:
        query = input("Human: ")
        if query in exit_conditions:
            print(f"🤖{bot.name}: Goodbye!")
            break
        else:
            print(f"🤖{bot.name}: {bot.get_response(query)}")
    except (KeyboardInterrupt, EOFError, SystemError):
        break

