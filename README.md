<br>

<p align="center"><img src="https://img.shields.io/badge/BlazerRAT-2CA5E0?logo=telegram&logoColor=white" width="500px"></p>
<h3 align="center">🔥 Control your machine with Telegram bot or from remote machine.</h3> <p
align="center">🔥 Cross platform Telegram based RAT that communicates via telegram to evade network restrictions and cross platform remote access RAT written on Python.</p>

---

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/kraloveckey)

---

# TelegramRAT
    
## Installation

1. `git clone https://github.com/kralovecket/blazer-rat.git`
2. Now follow the instructions in [How to use TelegramRAT](#how-to-use-telegramrat) section.

## How to use TelegramRAT

1. Go to Telegram and search for `https://t.me/BotFather`.
2. Create Bot and get the `API_TOKEN`.
3. Now search for `https://t.me/my_id_bot` and get the `chat_id`.
4. Now go to [blazer-tg.py](./blazer-tg.py) and go to line 17 and 18 and place `API_TOKEN` and `CHAT_ID` there.
5. Now run `python blazer-tg.py` for Windows and `python3 blazer-tg.py` for Linux.
6. Now go to the bot which you created and send command in message field.

## Help menu TelegramRAT

    HELP MENU:
    CMD Commands        | Execute cmd commands directly in bot
    cd ..               | Change the current directory
    cd foldername       | Change to current folder
    download filename   | Download File From Target
    screenshot          | Capture Screenshot
    info                | Get System Info
    location            | Get Target Location
    get url             | Download File From URL (Provide Direct URL)
    
## Features TelegramRAT

    1. Execute Shell Commands in bot directly.
    2. Download file from client.
    3. Get Client System Information.
    4. Get Client Location Information.
    5. Capture Screenshot.
    6. Get url (Download file from URL).
    7. More features will be added.
    
# BlazerRAT

> Cross platform multi clients RAT written on Python.

## Installation

1. `git clone https://github.com/kralovecket/blazer-rat.git`
2. `python3 blazer-server.py` (go to line 152 and change `ip,port` and start the server).
3. `blazer-client.py` (go to line 77 and Edit `IP` and `PORT`).
    
## Usage BlazerRAT

1. `python3 blazer-server.py`
2. Now compile `blazer-client.py` to exe for Windows (make sure change ip and port in it) or run `python3 blazer-client.py` on Linux (make sure change ip and port in it).
    
## Features BlazerRAT

    1. Simple and cross platform RAT.
    2. Multi client handling.
    3. Persistent shell.
    4. Auto-reconnect.
    5. Upload file to client.
    6. Download file from client.
    7. You can convert `blazer-client.py` to exe using `pyinstaller` tool in Windows.
