import os
import time

import telegram
from dotenv import load_dotenv


def send_photo(interval):
    while True:
        for root, dirs, images in os.walk('images'):
            for image in images:
                path_img = f'{root}/{image}'
                with open(path_img, 'rb') as photo:
                    bot.send_document(chat_id=tg_chat_id, document=photo)
                time.sleep(interval)


if __name__ == '__main__':
    load_dotenv()
    tg_bot_token = os.getenv('TG_BOT_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')
    time_interval = int(os.getenv('INTERVAL', default=86400))
    bot = telegram.Bot(token=tg_bot_token)
    send_photo(interval=time_interval)
