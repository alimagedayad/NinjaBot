import json
import os


class dbHandler:
    def __init__(self):
        self.memory = None

    def read(self, json_file):
        with open(json_file) as jF:
            self.memory = json.load(jF)
        return self.memory

    def write_order(self, text):
        order = open("order.txt", "a")
        order.write(text)
        order.close()

    def write_json(self, json_file, new_list):
        data = json.dumps(new_list, indent=4, separators=(",", ": "))
        with open(json_file, "w") as outfile:
            outfile.write(data)


"""
Tests:
"""
# demo = dbHandler()
# print(demo.read("db.json"))
