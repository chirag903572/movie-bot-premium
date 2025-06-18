import os
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get your bot token from environment
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update, context):
    update.message.reply_text("Welcome to the Movie Bot!")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
