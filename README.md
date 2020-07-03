# Tiny Telegram bot in Python 🌈
I am using this tool to monitor my numerical simulations 👩🏿‍🔬🧪💻 and get notifications when a job is finished. 

## Install

```python
git clone https://github.com/caglorithm/tgbot.git
cd tgbot/
pip install .
```


## Usage
```python 
from tgbot.tgbot import TelegramBot
bot = TelegramBot()
bot.sendMsg("Hey bae 🖤")

# send a local image
bot.sendImage("pic.jpg")

# send a local file
bot.sendFile("README.md")

# send a remote image
bot.sendRemoteImage("https://caglorithm.github.io/notebooks/images/covid-dashboard/dashboard.png")

# send a remote file
bot.sendRemoteFile("https://github.com/robots.txt")
```