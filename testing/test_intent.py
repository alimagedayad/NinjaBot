import unittest

from intent import Intent
import mock


class TestIntent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_memory = [
            {
                "entryPoint": "recommendation",
                "patterns": ["recommend", "proposit", "suggest", "ali"],
                "entities": [],
                "responses": ["please wait while we recommend you a phone..."],
            }
        ]

    def test_canCreateObj(self):
        intObj = Intent()
        with self.assertRaises(Exception):
            Intent("EXTRA ARG")

    def test_setIntent(self):
        intObj = Intent()
        intObj.set_intent("recommendation")
        self.assertEqual(intObj.current_intent, "recommendation")

    def test_getAll(self):
        intObj = Intent()
        with mock.patch("intent.Intent.db") as mocked_db:
            mocked_db.memory = self.sample_memory
            data = intObj.get_all()
        self.assertEqual(data, self.sample_memory)
