import os
import time

import telegram
from dotenv import load_dotenv


def send_photo(interval:int=86400):
    while True:
        for el in os.walk('images'):
            for image in el[2]:
                path_img = el[0] + '/' + image
                bot.send_document(chat_id=tg_chat_id,
                                  document=open(path_img, 'rb'))
                time.sleep(interval)


if __name__ == '__main__':
    load_dotenv()
    tg_bot_token = os.getenv('TG_BOT_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')
    time_interval = int(os.getenv('INTERVAL'))
    bot = telegram.Bot(token=tg_bot_token)
    if time_interval:
        send_photo(interval=time_interval)
    else:
        send_photo()
