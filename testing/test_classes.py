import unittest
from classes import Phone
import mock


class Test_Phones(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p1 = Phone(
            1, "iphone 12 pro", "apple", "ios 14", 999, 128, "graphite", 10, 12, 6, 8
        )
        cls.sample_memory = [
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
            {
                "id": 3,
                "name": "iphone 12 pro",
                "brand": "apple",
                "os": "ios 14",
                "price": 1299,
                "size": 512,
                "color": "graphite",
                "recommend": 7,
                "stock": 12,
                "ram": 6,
                "photo": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-graphite-hero?wid=940&hei=1112&fmt=png-alpha&qlt=80&.v=1604021660000",
            },
        ]

    def test_ValType_int(self):
        self.assertIsInstance(self.p1.id, int)
        self.assertIsInstance(self.p1.price, int)
        self.assertIsInstance(self.p1.size, int)
        self.assertIsInstance(self.p1.stock, int)
        self.assertIsInstance(self.p1.ram, int)

    def test_ValType_str(self):
        self.assertIsInstance(self.p1.name, str)
        self.assertIsInstance(self.p1.brand, str)
        self.assertIsInstance(self.p1.os, str)
        self.assertIsInstance(self.p1.color, str)

    def test_canCreateObj(self):
        with self.assertRaises(TypeError):
            p1 = Phone(
                1,
                "iphone 12 pro",
                "apple",
                "ios 14",
                999,
                128,
                "graphite",
                10,
                12,
                6,
                "EXTRA",
                "EXTRA",
            )

    def test_getPhone(self):

        with mock.patch("classes.Phone.db") as mocked_db:
            mocked_db.memory = self.sample_memory
            self.p1.get_phone(0)
            self.assertEqual(self.p1.id, 1)
            self.assertEqual(self.p1.name, "iphone 12 pro")
            self.assertEqual(self.p1.brand, "apple")
            self.assertEqual(self.p1.os, "ios 14")
            self.assertEqual(self.p1.price, 999)
            self.assertEqual(self.p1.size, 128)
            self.assertEqual(self.p1.color, "graphite")
            self.assertEqual(self.p1.recommend_score, 10)
            self.assertEqual(self.p1.stock, 11)
            self.assertEqual(self.p1.ram, 6)
            self.assertEqual(
                self.p1.link,
                "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-graphite-hero?wid=940&hei=1112&fmt=png-alpha&qlt=80&.v=1604021660000",
            )

    def test_getNumberOfPhones(self):

        with mock.patch("classes.Phone.db") as mocked_db:
            mocked_db.memory = self.sample_memory
            self.assertEqual(self.p1.get_number_of_phones(), 3)
