from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer

porter = PorterStemmer()

"""
==========================================================================
"""
"GOALS"
# normalization
# punctuation
# tokenization
# stop words
# stemming
"""
==========================================================================
"""


class TextInput:
    def __init__(self, text):
        self.text = text

    def change_input(self, text):
        self.text = text

    def remove_punc(self):
        text = self.text
        reduced = []
        for char in text:
            if char not in string.punctuation:
                reduced.append(char)
        self.text = "".join(reduced)

    def text_initiation(self):
        self.remove_punc()
        text = self.text
        text = text.lower()
        text_tokens = text.split()
        tokens_without_sw = [
            word
            for word in text_tokens
            if (not word in stopwords.words())
            or word in ["os", "where", "when", "name"]
        ]
        temp = []
        for word in tokens_without_sw:
            temp.append(porter.stem(word))
        self.text = temp


"""
==================================TESTING========================================
"""
# message = TextInput("i want to sort by name")
# message.text_initiation()
# print(message.text)
"""
==========================================================================
"""
