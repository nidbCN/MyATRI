# coding=utf-8

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot('ATRI')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.atri"
)

# Get a response to an input statement
while True:
    msg = input()
    r = chatbot.get_response(msg)

    print("RESPONSE:" + str(r))
