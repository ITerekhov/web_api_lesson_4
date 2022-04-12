import os
import telegram
from dotenv import load_dotenv

load_dotenv()
tg_bot_token = os.getenv('TG_BOT_TOKEN')
tg_chat_id = os.getenv('TG_CHAT_ID')

bot = telegram.Bot(token=tg_bot_token)
bot.send_message(chat_id=tg_chat_id, text='какой-нибудь текст')