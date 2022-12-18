import asyncio
from aiogram import Bot
from config import BOT_TOKEN, CHAT_ID

loop = asyncio.new_event_loop()
bot = Bot(BOT_TOKEN, loop=loop)



def main():
    asyncio.run(bot.send_message(
        chat_id=CHAT_ID,
        text="Cron is working for now."
    ))


if __name__ == '__main__':
    main()