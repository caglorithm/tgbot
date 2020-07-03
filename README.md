# Tiny Telegram bot in Python 🌈
I am using this tool to monitor my numerical simulations 👩🏿‍🔬🧪💻 and get notifications when a job is finished. 

## Install

```python
git clone https://github.com/caglorithm/tgbot.git
cd tgbot/
pip install .
```

## Setup
Getting the **bot token** is easy:

1. Create a Telegram bot by sending the message `/newbot` to `@BotFather` and voila, you should receive a string like `238972427:ASdjsd82hasD2hsd872ASsdh`. That's your `<bot_token>`. 
2. Copy it into `credentials.json`.

Now you have to find out **your Telegram ID** so the bot can reach you.

1. In Telegram, search for the bot name you've just created.
2. Send the bot any message.
3. Visit `https://api.telegram.org/bot<bot_token>/getUpdates` in your browser.
4. Find the field `result.message.from.id` in the json. This is your `<to_id>` and it looks like `29937732`. 
5. Copy it into `credentials.json`.

## Usage
```python 
from tgbot.tgbot import TelegramBot
bot = TelegramBot()

# send a message
bot.sendMsg("Hey bae, your simulations are done 🖤.")

# send a local image
bot.sendImage("pic.jpg")

# send a local file
bot.sendFile("README.md")

# send a remote image
bot.sendRemoteImage("https://caglorithm.github.io/notebooks/images/covid-dashboard/dashboard.png")

# send a remote file
bot.sendRemoteFile("https://github.com/robots.txt")
```