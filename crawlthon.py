from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm crawlthon bot! this is the dungeon crowl game bot")

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("PONG")

def main():
    load_dotenv()
    BOT_TOKEN = os.environ.get("TelegramBotAPI")
    
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    ping_handler = CommandHandler('PING', ping)
    application.add_handler(ping_handler)
    

    
    application.run_polling()

if __name__ == "__main__" :
    main()