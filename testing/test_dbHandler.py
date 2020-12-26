import unittest
from dbHandler import dbHandler
import mock
import json

"""
Note that dbHandler does not have any external dependenciesl so no integration test for it 
"""


class TestDbHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        pass

    def test_canCreateObj(self):

        fObj = dbHandler()
        self.assertIsNone(fObj.memory)

    def test_readFileThatDoesNotExist(self):
        fObj = dbHandler()
        with self.assertRaises(FileNotFoundError):
            fObj.read("non-existant.json")

    def test_objWithPosParams(self):
        with self.assertRaises(TypeError):
            fObj = dbHandler("DUMMY_ARG")

    def test_readingJSON_v3(self):
        sample_json = [
            {
                "id": 1,
                "name": "iphone 12 pro",
                "brand": "apple",
                "os": "ios 14",
                "price": 999,
                "size": 128,
                "color": "graphite",
                "recommend": 10,
                "stock": 11,
                "ram": 6,
                "photo": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-graphite-hero?wid=940&hei=1112&fmt=png-alpha&qlt=80&.v=1604021660000",
            },
            {
                "id": 2,
                "name": "iphone 12 pro",
                "brand": "apple",
                "os": "ios 14",
                "price": 1099,
                "size": 256,
                "color": "graphite",
                "recommend": 5,
                "stock": 12,
                "ram": 6,
                "photo": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-graphite-hero?wid=940&hei=1112&fmt=png-alpha&qlt=80&.v=1604021660000",
            },
        ]

        fObj = dbHandler()
        with mock.patch(
            "builtins.open", mock.mock_open(read_data=json.dumps(sample_json))
        ) as mockOpenedFileObject:
            result = fObj.read("non-existant.json")
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[1]["size"], 256)
        mockOpenedFileObject.assert_called_with(fObj.filename, "r")

    def test_writeOrder(self):
        fObj = dbHandler()
        with mock.patch("builtins.open", mock.mock_open()) as mockedOpenedFileObj:
            fObj.write_order("FAKE_TEXT")
            mockedOpenedFileObj.return_value.write.assert_called_with("FAKE_TEXT")

    def test_writeJson(self):
        fObj = dbHandler()
        new_list = [{"phone": "apple", "id": 1}]
        data = json.dumps(new_list, indent=4, separators=(",", ": "))
        with mock.patch("builtins.open", mock.mock_open()) as mockedOpenedFileObj:
            fObj.write_json("non-existant.json", new_list)
            mockedOpenedFileObj.return_value.write.assert_called_with(data)
