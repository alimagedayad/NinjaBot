from dbHandler import dbHandler


class Intent:

    db = dbHandler()

    def __init__(self):
        current_intent = None

    def set_intent(self, int_type):
        self.current_intent = int_type

    def get_all(self, filename="intents.json"):
        Intent.db.read(filename)
        return Intent.db.memory


"""
TESTING
"""
# iT = Intent()
# print(iT.get_all())