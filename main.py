# from intents import intents
# from text_processing import normalize, remove_punc, tokenize, removeStopWord
from nlp import TextInput as TI
import random

import manageIntent as MI
# from time import sleep
# from responses import response
# from random import choice as rChoice

"""
List:
- manage intents DONE
-intent       DONE
-db-handler  DONE
-phones     DONE
-ManagePhones DONE
-Boundary (UI) DONE
"""


class ChatBot:
    def __init__(self):
        pass
    def init_bot(self):

        print("Hello, I'm Ninja!")
        name = input("May I need know your name? \n")
        print(f"Hi {name}, How may I help you? \n (You can always exit by typing 'quit')")

    def start_bot(self):
        prom = ""
        rep = TI(prom)
        while True:
            prom = input("-> ")
            if prom == 'quit':
                break
            rep = TI(prom)
            rep.text_initiation()
            rep = rep.text
            detect_purpose = MI.ManageIntent()
            detect_purpose.get_response(rep)

    def bot_end(self):
        print("Goodbye!!!")



"""
CHATBOT NINJA
"""


chat = ChatBot()
chat.init_bot()
chat.start_bot()
chat.bot_end()


