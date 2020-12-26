import unittest

from intent import Intent
from dbHandler import dbHandler


class TestIntegrationIntent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.intObj = Intent()

    def test_objOfSameType(self):
        self.assertIsInstance(self.intObj, Intent)

    def test_hasStoredFilesObject(self):
        self.assertTrue("db" in Intent.__dict__)
        self.assertIsInstance(Intent.db, dbHandler)

    def test_checkVals(self):
        data = self.intObj.get_all()
        # check keys
        for row in data:
            self.assertIn("entryPoint", row.keys())
            self.assertIn("patterns", row.keys())
            self.assertIn("entities", row.keys())
            self.assertIn("responses", row.keys())
        # check some intent vals
        self.assertEqual(data[0]["entryPoint"], "recommendation")
        self.assertEqual(data[2]["entryPoint"], "hours")
