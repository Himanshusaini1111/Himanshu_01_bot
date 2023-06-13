from telethon import TelegramClient
import logging
import time


api_id="1125689"
api_hash="4772d1792ed194020a8fb06a91ffb8fa"
bot_token="5846650068:AAHdEsl_uG-OB_Gh2hS5Tcjgo7OnfQkRooQ"

bot = TelegramClient("Himanshu", api_id, api_hash).start(bot_token = bot_token)