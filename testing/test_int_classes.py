import unittest
import json
from classes import Phone
from dbHandler import dbHandler

"""
What should I integration-test?
- is the created Phone object, is it of type/class Phone?
"""


class TestIntegrationPhones(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.phone = Phone(
            id_num=None,
            name=None,
            brand=None,
            os=None,
            price=None,
            size=None,
            color=None,
            recommend_score=None,
            stock=None,
            link=None,
            ram=None,
        )

    def test_ObjectofCorrectType(self):
        self.assertIsInstance(self.phone, Phone)

    def test_hasDbHandlerObject(self):
        self.assertTrue("db" in Phone.__dict__)
        self.assertIsInstance(Phone.db, dbHandler)

    def test_orderText(self):
        """
        asssert that order_text puts the expected text in the file, reaf it back, and then revert
        to original state
        IDEALLY, I would be either:
        1- creating a extra test_file.txt to test on instead of modifying the actual file
        but since it (order.txt) is hard-coded AND the method is not taking any file arguments, I had
        to do it this way.
        """
        self.phone.order_phone("Test line")
        with open("order.txt", "r") as file:
            data = file.readlines()
            self.assertEqual("Test line", data[-1])
            del data[-1]
        with open("order.txt", "w") as file:
            for line in data:
                file.write(line)

    def test_updateDb(self):
        """
        Same Problem; the method should offer the dev an option to set the filename as an argument.
        otherwise, by hard-coding the actual data file used, we will need to update, check then revert
        and there will be no availibility to create a test temp data file instead of using the original one.
        """
        new_list = [{"phone": "apple", "id": 1}]
        original_content = self.phone.db.memory
        self.phone.update_db(new_list)
        with open("db.json", "r") as file:
            data = json.load(file)
        self.assertEqual(data, new_list)
        self.phone.update_db(original_content)
