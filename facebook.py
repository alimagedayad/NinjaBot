import os, random, json, sys
from pymessenger.bot import Bot
from flask import Flask, request
from nlp import TextInput as TI
from testClass import TestT as Terminal
import manageIntent as MI
import managephones as MP
import base64 as b6

chat = Terminal()

# msg = None
# flag = 0
# i1 = None
# i2 = None
p = 0
firstRun = True

app = Flask(__name__)
ACCESS_TOKEN = ""
VERIFY_TOKEN = ""
bot = Bot(ACCESS_TOKEN)

bannedUsers = [""]
insult_count = 0


@app.route("/webhook", methods=["GET", "POST"])
def receive_message():
    global msg, flag, i1, i2, counter, p, firstRun, insult_count
    responseComplete = False
    try:
        if request.method == "GET":
            """Before allowing people to message your bot, Facebook has implemented a verify token
            that confirms all requests that your bot receives came from Facebook."""
            token_sent = request.args.get("hub.verify_token")
            return verify_fb_token(token_sent)
        # if the request was not get, it must be POST and we can just proceed with sending a message back to user
        else:
            # get whatever message a user sent the bot
            output = request.get_json()
            for event in output["entry"]:
                messaging = event["messaging"]
                for message in messaging:
                    if message.get("message"):
                        p = 0
                        # Facebook Messenger ID for user so we know where to send response back to
                        recipient_id = message["sender"]["id"]
                        if recipient_id in bannedUsers:
                            send_message(recipient_id, "You're banned!")
                            break
                        if message["message"].get("text"):
                            userMessage = message["message"].get("text")
                            # send_buttons(recipient_id, "text", ["1", "2"])
                            msg, flag, i1, i2 = chat.getInfo()
                            # send_message(
                            #     recipient_id,
                            #     f"i1: {i1} \ni2: {i2} \nflag: {flag} \nmsg: {msg}",
                            # )
                            rep = TI(userMessage)
                            rep.text_initiation()
                            rep = list(set(rep.text))

                            detect_purpose = MI.ManageIntent()

                            if check_insult(rep, insult_count, recipient_id):
                                insult_count += 1
                                break
                            else:
                                print("rep: ", rep)
                                detect_purpose = MI.ManageIntent()
                                # detect_purpose.get_response(rep)

                            intent1, intent2 = detect_purpose.extractIntents(rep)
                            manage = MP.ManagePhones()

                            print("intents: ", intent1, intent2, i1, i2)

                            if (intent1 == None and i1 == None) or (
                                intent1 == None and firstRun
                            ):
                                send_message(
                                    recipient_id,
                                    "I didn't quit get that. Please try again.",
                                )

                            elif intent1 != None and intent2 == None:
                                if intent1 == "greeting":
                                    res = detect_purpose.greeting(intent1)
                                    send_message(recipient_id, res)
                                elif intent1 == "sort":
                                    res = manage.sort()
                                    send_message(recipient_id, res)
                                elif intent1 == "filter":
                                    res = manage.filter()
                                    send_message(recipient_id, res)
                                elif intent1 == "recommendation":
                                    res = manage.recommend_phone()
                                    sendRecommendation(res[0], res[1], recipient_id)

                            elif intent1 != None and intent2 != None:
                                # print("line: 91 executed")
                                limit = 9
                                if intent1 == "sort":
                                    res = manage.sort(intent2)
                                    # if intent2 == "price":
                                    #     res = manage.sort(intent2)
                                    # elif intent2 == "size":
                                    #     res = manage.sort(intent2)
                                    # elif intent2 == "name":
                                    #     res = manage.sort(intent2)
                                elif intent1 == "filter":
                                    res = manage.filter(specific=intent2)
                                    print("returned filtered: ", res)

                                if len(res) > 0 and type(res) is list:
                                    sendListv2(res, limit, recipient_id)
                                elif type(res) is str:
                                    send_message(recipient_id, res)
                                else:
                                    print("typeof: ", type(res))

                            elif intent1 is None and i1 is not None:
                                print("line: 113 executed i1,i2: ", i1, i2)
                                res = []
                                checkEntities = detect_purpose.checkEntities(rep)
                                print(
                                    "line: 113 executed checkEntities: ", checkEntities
                                )
                                chosenEntity = None
                                try:
                                    for i in checkEntities:
                                        if checkEntities[i][-1] == 1:
                                            chosenEntity = i
                                except:
                                    print("1st expect: ", checkEntities)
                                    try:
                                        ints = [
                                            int(i) for i in checkEntities.split(",")
                                        ]
                                        chosenEntity = checkEntities
                                        print("nested try: check", chosenEntity)
                                    except ValueError:
                                        print("nested except: check", chosenEntity)
                                        res = "Error!"
                                p = 0
                                if i1 == "sort":
                                    if i2 == "name" or i2 == "brand":
                                        res = manage.sort(i2, nameP=chosenEntity)
                                    elif (
                                        chosenEntity == "name"
                                        or chosenEntity == "brand"
                                    ):
                                        res = manage.sort(chosenEntity)
                                        chat.setI1("sort")
                                        chat.setI2(chosenEntity)
                                        p = 1
                                    else:
                                        print("res: ", chosenEntity)
                                        res = manage.sort(chosenEntity)
                                    if len(res) > 0 and type(res) is list:
                                        sendListv2(res, 10, recipient_id)
                                    elif type(res) is str:
                                        send_message(recipient_id, res)
                                    else:
                                        print("typeof: ", type(res))

                                elif i1 == "filter":
                                    if (
                                        i2 == "os"
                                        or i2 == "price"
                                        or i2 == "size"
                                        or i2 == "ram"
                                        or i2 == "brand"
                                    ):
                                        res = manage.filter(
                                            i2, inputSpecific=chosenEntity
                                        )
                                    else:
                                        res = manage.filter(chosenEntity)
                                        chat.setI1("filter")
                                        chat.setI2(chosenEntity)
                                        p = 1

                                    if len(res) > 0 and type(res) is list:
                                        sendListv2(res, 10, recipient_id)
                                    elif type(res) is str:
                                        send_message(recipient_id, res)
                                    else:
                                        print("typeof: ", type(res))

                            # elif i1 == 'sort' and intent1 == None:
                            #     secAttr = ''.join(rep)
                            #     print('setAttr', secAttr)
                            #     manage = MP.ManagePhones()
                            #     res = []
                            #     if secAttr == "price":
                            #         res = manage.sort(
                            #             "price", recipient_id=recipient_id
                            #         )
                            #         responseComplete = True
                            #     elif secAttr == 'size':
                            #         res = manage.sort(
                            #             "size", recipient_id=recipient_id
                            #         )
                            #         responseComplete = True
                            #     else:
                            #         send_message(
                            #             recipient_id,
                            #             "I didn't quit get that. Please try again. Sorry dude!",
                            #         )
                            #     if len(res) > 0:
                            #         for index, item in enumerate(res):
                            #             if index <= 9:
                            #                 text = b6.b64decode(item)
                            #                 send_message(
                            #                     recipient_id,
                            #                     f"i: {index}\n{text.decode('utf-8')}"
                            #                 )
                            #         return "success"

                            # elif intent1 == "sort" or i1 == "sort":
                            #     manage = MP.ManagePhones()
                            #     res = []
                            #     if intent2 == "price" or i2 == "price":
                            #         res = manage.sort(
                            #             "price", recipient_id=recipient_id
                            #         )
                            #         responseComplete = True
                            #     elif intent2 == None:
                            #         send_message(
                            #             recipient_id,
                            #             "How would you like to sort the phones?",
                            #         )
                            #     if len(res) > 0:
                            #         for index, item in enumerate(res):
                            #             if index <= 9:
                            #                 text = b6.b64decode(item)
                            #                 send_message(
                            #                     recipient_id,
                            #                     f"i: {index}\n{text.decode('utf-8')}"
                            #                 )
                            #         return "success"

                            # i1 = intent1
                            # i2 = intent2
                            # flag = 0
                            # msg = userMessage
                            if p == 1:
                                pass
                            else:
                                chat.setI1(intent1)
                                chat.setI2(intent2)

                            if (
                                (intent1 != None and intent1 != "")
                                and (intent2 != None and intent2 != "")
                                and responseComplete
                            ):
                                chat.setFlag(0)
                            # if (intent1 != None or intent1 != '') and intent2 == None:
                            #     chat.setFlag(0)
                            elif intent1 != None and intent2 != None:
                                chat.setFlag(1)
                            else:
                                chat.setFlag(-1)

                            chat.setMessage(userMessage)

                            # send_message(recipient_id, "Finished =====")
                            # return "success"

                            # send_message(
                            #     recipient_id,
                            #     f"i1: sort, i2: {intent2}",
                            # )
                            # send_message(
                            #     recipient_id, f"{detect_purpose.extractIntents(rep)}"
                            # )
                            firstRun = False
                            return "success"

                        # if user sends us a GIF, photo,video, or any other non-text item
                        if message["message"].get("attachments"):
                            for attach in message["message"].get("attachments"):
                                if attach["type"] == "image":
                                    bot.send_image_url(
                                        recipient_id, attach["payload"]["url"]
                                    )
                                print(attach["type"])

        # print("terminal tuple: ", chat.getInfo())
    except Exception as e:
        print("Exception: ", e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
    return "Message Processed"


def verify_fb_token(token_sent):
    # take token sent by facebook and verify it matches the verify token you sent
    # if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Invalid verification token"


# chooses a random message to send to the user
# def get_message():
#     sample_responses = [
#         "You are stunning!",
#         "We're proud of you.",
#         "Keep on being you!",
#         "We're greatful to know you :)",
#     ]
#     # return selected item to the user
#     return random.choice(sample_responses)

# uses PyMessenger to send response to user
def send_message(recipient_id, response):
    # sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"


def send_buttons(recipient_id, elements):
    bot.send_message(
        recipient_id,
        {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": elements,
                },
            }
        },
    )
    return "status"


def phoneElementsCreate(
    name,
    body,
    photo="https://incredideals.net/wp-content/uploads/2019/09/iphone11-select-2019-family.jpeg",
):
    return {
        "title": name,
        "image_url": photo,
        "subtitle": body,
    }


def send_type(recipient_id, state=0):
    if state == 0:
        bot.send_action(recipient_id, "typing_on")
    elif state == 1:
        bot.send_action(recipient_id, "typing_off")
    return "success"


def sendList(list, limit, recipient_id):
    elements = []
    for index, item in enumerate(list):
        if index < limit:
            text = b6.b64decode(item)
            send_message(
                recipient_id,
                f"i: {index}\n{text.decode('utf-8')}",
            )
    return "success"


def sendRecommendation(encodedText, pic, recipient_id):
    decodedText = b6.b64decode(encodedText).decode("utf-8")
    send_message(recipient_id, "Here's our recommendation 🥁🥁🥁")
    sendPhoto(recipient_id, pic)
    send_message(recipient_id, decodedText)
    return "success"


def sendPhoto(recipient_id, image_url):
    bot.send_image_url(recipient_id, image_url)
    return "success"


def check_insult(cleanlist, count, recipient_id):
    global bannedUsers
    cuss = [
        "fuck",
        "shit",
        "asshole",
        "cunt",
        "suck",
        "damn",
        "cock",
        "dick",
        "whore",
        "pussy",
    ]
    for word in cleanlist:
        if word in cuss:
            if count == 2:
                bannedUsers.append(recipient_id)
                send_message(recipient_id, "The chatbot will close!!")
            else:
                send_message(
                    recipient_id,
                    f"This type of language is intolerable. Please refrain from using it again. Do so again {3 - count - 1} times and the bot will close",
                )
            return True
    return False


def sendListv2(list, limit, recipient_id):
    elements = []
    print(limit)
    for index, item in enumerate(list):
        if index < limit:
            elements.append(
                phoneElementsCreate(
                    item[0],
                    f"RAM:{item[2]}GB - {item[3]}GB\n{item[1]}$",
                    photo=item[-1],
                )
            )
    if len(elements) > 0:
        print("elements: ", elements)
        send_buttons(recipient_id, elements)
    return "success"


if __name__ == "__main__":
    app.run(debug=True)
