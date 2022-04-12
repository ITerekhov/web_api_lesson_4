import os

import telegram
from dotenv import load_dotenv

from main import fetch_astronomy_picture_from_nasa, nasa_request_params

load_dotenv()
tg_bot_token = os.getenv('TG_BOT_TOKEN')
tg_chat_id = os.getenv('TG_CHAT_ID')

bot = telegram.Bot(token=tg_bot_token)
path_images = fetch_astronomy_picture_from_nasa(1, nasa_request_params)
bot.send_document(chat_id=tg_chat_id, document=open(path_images[0], 'rb'))