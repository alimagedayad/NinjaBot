from intent import Intent
import managephones as MP
import random


class ManageIntent:

    intentObj = Intent()

    def __init__(self):
        pass

    def extractIntent(self, cleanList):
        intentFound = False
        ManageIntent.intentObj.current_intent = None
        intent = None
        for item in ManageIntent.intentObj.get_all():
            for word in cleanList:
                if word in item["entryPoint"] or word in item["patterns"]:
                    intent = item["entryPoint"]
                    intentFound = True
                    break
                if intentFound:
                    break
            if intentFound:
                break

        ManageIntent.intentObj.set_intent(intent)
        return intent

    def greeting(self, word):
        for item in ManageIntent.intentObj.get_all():
            if item["entryPoint"] == word and len(item["responses"]) != 0:
                return random.choice(item["responses"])
                # return choice
                # break

    def check_second_intent(self, cleanList):
        intent = None
        intentFound = False
        first_intent = ManageIntent.intentObj.current_intent
        if first_intent == "sort" or first_intent == "filter":
            for item in ManageIntent.intentObj.get_all():
                if item["entryPoint"] == first_intent:
                    for word in cleanList:
                        for i in item["entities"]:
                            if word in i:
                                intentFound = True
                                intent = i
                                break
                        if intentFound:
                            break
                if intentFound:
                    break
        return intent

    def check_number(self, cleanlist):
        for word in cleanlist:
            if word.isnumeric():
                return int(word)
        return -1

    def extractIntents(self, cleanList):
        return [self.extractIntent(cleanList), self.check_second_intent(cleanList)]

    def checkEntities(self, cleanList):
        priority = 1
        checkedEntities = {}
        intentObj = ManageIntent.intentObj.get_all()
        for item in cleanList:
            for item2 in intentObj:
                for entity in set(item2["entities"]):
                    if item == entity:
                        if item in checkedEntities.keys():
                            pass
                        else:
                            checkedEntities[str.lower(item)] = [True, priority]
                            priority += 1

        if checkedEntities == {}:
            try:
                print("cleanList =", cleanList)
                ints = [int(i) for i in cleanList]
                ints.sort()
                strInts = [str(i) for i in ints]
                return ",".join(strInts)
            except ValueError:
                return {}
        else:
            return checkedEntities

    def get_response(self, cleanList, client="user", recipient_id="123"):
        if client == "messenger":
            print("called from messenger")
            print("cleanList: ", cleanList)
        intent1 = self.extractIntent(cleanList)
        intent2 = self.check_second_intent(cleanList)

        for item in ManageIntent.intentObj.get_all():
            if item["entryPoint"] == intent1 and len(item["responses"]) != 0:
                choice = random.choice(item["responses"])
                print(choice)
                break
        if intent1 == "":
            return "I didn't quit get that. Please try again."
        if intent1 == "sort":
            manage = MP.ManagePhones()
            manage.sort(intent2, recipient_id=recipient_id)
        elif intent1 == "filter":
            manage = MP.ManagePhones()
            manage.filter(intent2)
        elif intent1 == "recommendation":
            manage = MP.ManagePhones()
            manage.recommend_phone()
        elif intent1 == "browse":
            manage = MP.ManagePhones()
            manage.print_name()
        elif intent1 == "restart":
            manage = MP.ManagePhones()
            manage.reinit()


"""
TESTING
"""
# demo = ManageIntent()
# inp = ["200", "0"]
# print(demo.checkEntities(inp))
