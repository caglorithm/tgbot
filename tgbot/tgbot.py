import requests
import io
import json


class TelegramBot(object):
    def __init__(self, bot_token=None, to_id=None):

        if bot_token is None and to_id is None:
            # load credentials from json
            with open("credentials.json", "r") as f:
                credentials_dict = json.load(f)

        # create a new bot by writing "/newbot" to @BotFather
        self.bot_token = bot_token or credentials_dict["bot_token"]

        self.request_url = f"https://api.telegram.org/bot{self.bot_token}"

        # to get your Telegram id:
        # 1) serach for the bot name you've created
        # 2) send the bot a message
        # 3) go to https://api.telegram.org/bot<bot_token>/getUpdates
        # 4) get the field result.message.from.id
        self.to_id = to_id or credentials_dict["to_id"]

    def sendMsg(self, message, to=None):
        to = to or self.to_id
        send_text = self.request_url + "/sendMessage?chat_id=" + \
            to + "&parse_mode=Markdown&text=" + message
        response = requests.get(send_text)
        return response.json()

    def sendImage(self, filename, to=None):
        # https://stackoverflow.com/questions/31860628/how-to-send-an-image-from-a-telegram-bot
        to = to or self.to_id
        url = self.request_url + "/sendPhoto"
        files = {"photo": open(filename, "rb")}
        data = {"chat_id": self.to_id}
        r = requests.post(url, files=files, data=data)
        return (r.status_code, r.reason, r.content)

    def sendRemoteImage(self, img_url, to=None):
        to = to or self.to_id
        url = self.request_url + "/sendPhoto"
        remote_image = requests.get(img_url)
        photo = io.BytesIO(remote_image.content)
        photo.name = "img.png"
        files = {"photo": photo}
        data = {"chat_id": self.to_id}
        r = requests.post(url, files=files, data=data)
        return (r.status_code, r.reason, r.content)

    def sendFile(self, filename, to=None):
        to = to or self.to_id
        url = self.request_url + "/sendDocument"
        files = {"document": open(filename, "rb")}
        data = {"chat_id": self.to_id}
        r = requests.post(url, files=files, data=data)
        return (r.status_code, r.reason, r.content)

    def sendRemoteFile(self, img_url, to=None):
        to = to or self.to_id
        url = self.request_url + "/sendDocument"
        remote_image = requests.get(img_url)
        photo = io.BytesIO(remote_image.content)
        photo.name = "img.png"
        files = {"document": photo}
        data = {"chat_id": self.to_id}
        r = requests.post(url, files=files, data=data)
        return (r.status_code, r.reason, r.content)


if __name__ == "__main__":
    bot = TelegramBot()
    bot.sendMsg("Hello world.")
