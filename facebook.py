import os, random, json
from pymessenger.bot import Bot
from flask import Flask, request
from nlp import TextInput as TI
from testClass import TestT as Terminal
import manageIntent as MI
import managephones as MP
import base64 as b6

app = Flask(__name__)
ACCESS_TOKEN = "EAAE9kzEJZXXXXXXXmZBlV838bIhHUs3ZC1WGtna9xDLDL1XzCE6TSs0BQZA2JzRupeEhV31GIqwLhp8rK6cNZBdAGusBYZBRoLXS6FWtHWh7hCXE2gnAkFbJp9X0gWggbhV6kb01ReL4DrwNYosTJOXft0XXXX"
VERIFY_TOKEN = "youssef"
bot = Bot(ACCESS_TOKEN)

chat = Terminal()


@app.route("/webhook", methods=["GET", "POST"])
def receive_message():
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
                        # Facebook Messenger ID for user so we know where to send response back to
                        recipient_id = message["sender"]["id"]
                        if message["message"].get("text"):
                            userMessage = message["message"].get("text")
                            rep = TI(userMessage)
                            rep.text_initiation()
                            rep = list(set(rep.text))
                            detect_purpose = MI.ManageIntent()
                            # detect_purpose.get_response(rep)
                            # response = detect_purpose.get_response(
                            #     rep, client="messenger", recipient_id=recipient_id
                            # )
                            print("NLP: ", rep)
                            print(
                                "extracted intents: ",
                                detect_purpose.extractIntents(rep),
                            )
                            intent1, intent2 = detect_purpose.extractIntents(rep)
                            msg, flag, i1, i2 = chat.getInfo()
                            if intent1 and intent2 == None:
                                chat.setFlag(1)
                            if intent1 == "":
                                send_message(
                                    recipient_id,
                                    "I didn't quit get that. Please try again.",
                                )
                                return "success"
                            elif intent1 == "sort" or i1 == "sort":
                                manage = MP.ManagePhones()
                                res = []
                                if intent2 == "price" or i2 == "price":
                                    res = manage.sort(
                                        "price", recipient_id=recipient_id
                                    )
                                elif intent2 == None:
                                    send_message(
                                        recipient_id,
                                        "How would you like to sort the phones?",
                                    )
                                    return "success"
                                if len(res) > 0:
                                    for index, item in enumerate(res):
                                        if index <= 9:
                                            text = b6.b64decode(item)
                                            send_message(
                                                recipient_id,
                                                f"i: {index}\n{text.decode('utf-8')}",
                                            )
                                    return "success"

                            # send_message(recipient_id, "Finished =====")
                            # return "success"

                            # send_message(
                            #     recipient_id,
                            #     f"i1: sort, i2: {intent2}",
                            # )
                            # send_message(
                            #     recipient_id, f"{detect_purpose.extractIntents(rep)}"
                            # )

                            chat.setI1(intent1)
                            chat.setI2(intent2)
                            return "success"

                        # if user sends us a GIF, photo,video, or any other non-text item
                        if message["message"].get("attachments"):
                            response_sent_nontext = get_message()
                            for attach in message["message"].get("attachments"):
                                if attach["type"] == "image":
                                    bot.send_image_url(
                                        recipient_id, attach["payload"]["url"]
                                    )
                                print(attach["type"])

        print("terminal tuple: ", chat.getInfo())
    except Exception as e:
        print("Exception: ", e)
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


if __name__ == "__main__":
    app.run(debug=True)
