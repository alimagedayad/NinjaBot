import json
import os

class dbHandler:
    def __init__(self):
        self.memory = None
    def read(self, json_file):
        with open(json_file) as jF:
            self.memory = json.load(jF)
        return self.memory


"""
Tests:
"""
# demo = dbHandler()
# print(demo.read("db.json"))
