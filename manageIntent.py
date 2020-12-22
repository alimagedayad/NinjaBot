from intent import Intent
import managephones as MP
import random


class ManageIntent:

    intentObj = Intent()

    def __init__(self):
        pass


    def extractIntent(self, cleanList):
        intentFound = False
        ManageIntent.intentObj.current_intent=None
        intent = ""
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


    def check_second_intent(self, cleanList):
        intent = None
        intentFound = False
        first_intent = ManageIntent.intentObj.current_intent
        if first_intent == 'sort' or first_intent == 'filter':
            for item in ManageIntent.intentObj.get_all():
                if item['entryPoint'] == first_intent:
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

    def get_response(self, cleanList):
        intent1 = self.extractIntent(cleanList)
        intent2 = self.check_second_intent(cleanList)
        for item in ManageIntent.intentObj.get_all():
            if item['entryPoint'] == intent1 and len(item['responses']) != 0:
                print(random.choice(item['responses']))
                break
        if intent1 == '':
            print("I didn't quit get that. Please try again.")
        if intent1 == 'sort':
            manage = MP.ManagePhones()
            manage.sort(intent2)
        elif intent1 == 'filter':
            manage = MP.ManagePhones()
            manage.filter(intent2)
        elif intent1 == 'recommendation':
            manage = MP.ManagePhones()
            manage.recommend_phone()
        elif intent1 == 'browse':
            manage = MP.ManagePhones()
            manage.print_name()
        elif intent1 == 'restart':
            manage = MP.ManagePhones()
            manage.reinit()
        elif intent1 == 'reserve':
            manage = MP.ManagePhones()
            id = self.check_number(cleanList)
            if id < 0:
                id = None
            manage.reserve_phone(id)


'''
TESTING
'''
# print(">>start")
# demo = ManageIntent()
# print(demo.check_number(["me","hello","055"]))
# print(">>start")
# inp = ["filter","os"]
# print(">>start")
# # # print(demo.extractIntent(inp))
# # # print(demo.check_second_intent(inp))
# demo.get_response(inp)
# inp = ["clear"]
# demo.get_response(inp)
# inp = ["display"]
# demo.get_response(inp)


