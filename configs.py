# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 2885017))
    API_HASH = os.environ.get("API_HASH", "fddc3353cf2cca30aa178fa4725378ed")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1903329893:AAGh4ZtHllGdFmj1Xnsm3xQoyR45V2d_ThQ")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Rename-Bot-0")
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 5))
    BOT_OWNER = os.environ.get("BOT_OWNER", 1506444772)
    CAPTION = "Rename Bot by @{}\n\nMade by @Percy_Jackson_4"
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001531387788))
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://song:song@cluster0.6joos.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    DOWNLOAD_PATH = os.environ.get("DOWNLOAD_PATH", "./downloads")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    ONE_PROCESS_ONLY = bool(os.environ.get("ONE_PROCESS_ONLY", False))
    START_TEXT = """
Hi Dear 👋 I am Cortana. A Telegram Files Rename Bot.

Send me a File to Rename.

Made by [Master Chief](t.me/percy_jackson_4)
    """
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
    """
