from dbHandler import dbHandler
import os
from pathlib import Path


class Phone:
    "Common base class for all phones"
    db = dbHandler()
    db.read("db.json")

    def __init__(
        self,
        id_num=None,
        name=None,
        brand=None,
        os=None,
        price=None,
        size=None,
        color=None,
        recommend_score=None,
        photo=None,
    ):
        self.id = id_num
        self.name = name
        self.brand = brand
        self.os = os
        self.price = price
        self.size = size
        self.color = color
        self.photo = photo
        self.recommend_score = recommend_score

    def get_phone(self, phone_num):
        self.id = Phone.db.memory[phone_num]["id"]
        self.name = Phone.db.memory[phone_num]["name"]
        self.brand = Phone.db.memory[phone_num]["brand"]
        self.os = Phone.db.memory[phone_num]["os"]
        self.price = Phone.db.memory[phone_num]["price"]
        self.size = Phone.db.memory[phone_num]["size"]
        self.color = Phone.db.memory[phone_num]["color"]
        self.photo = Phone.db.memory[phone_num]["photo"]
        self.recommend_score = Phone.db.memory[phone_num]["recommend"]

        return self

    def get_number_of_phones(self):
        return len(Phone.db.memory)


"""
TESTING
"""
# p = Phone()
# l = [None]*p.get_number_of_phones()
# for i in range(p.get_number_of_phones()):
#     del p
#     p = Phone()
#     p = p.get_phone(i)
#     l[i]= p
