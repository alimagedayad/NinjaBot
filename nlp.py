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
            or word in ["os", "where", "when", "name", "brand", "ios"]
        ]
        temp = []
        dontStem = ["ios"]
        for word in tokens_without_sw:
            if word in dontStem:
                temp.append(word)
            else:
                temp.append(porter.stem(word))
        self.text = temp


"""
==================================TESTING========================================
"""
# message = TextInput("i want to filter the phones by price from 99 to 100")
# message.text_initiation()
# print(message.text)
"""
==========================================================================
"""
