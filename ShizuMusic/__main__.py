import requests

from pyrogram import Client as Bot

from ShizuMusic.config import API_HASH

from ShizuMusic.config import API_ID

from ShizuMusic.config import BG_IMAGE

from ShizuMusic.config import BOT_TOKEN

from ShizuMusic.services.callsmusic import run

response = requests.get(BG_IMAGE)

file = open("./etc/foreground.png", "wb")

file.write(response.content)

file.close()

bot = Bot(

    ":memory:",

    API_ID,

    API_HASH,

    bot_token=BOT_TOKEN,

    plugins=dict(root="ShizuMusic.modules"),

)

bot.start()

run()

