import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

BOT_TOKEN = os.getenv('BOT_TOKEN')
TMDB_KEY = os.getenv('TMDB_API_KEY')
PREMIUM_LINK = os.getenv('PREMIUM_LINK')
UPI_ID = os.getenv('UPI_ID')

def start(u: Update, c: CallbackContext):
    u.message.reply_text("👋 Welcome! Send me a movie name to get details.")

def premium(u: Update, c: CallbackContext):
    u.message.reply_text(f"💰 Join our premium group (₹1/day). Send payment to +91 {UPI_ID} and join: {PREMIUM_LINK}")

def movie(u: Update, c: CallbackContext):
    name = u.message.text
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_KEY}&query={name}"
    r = requests.get(url).json()
    if r.get('results'):
        m = r['results'][0]
        u.message.reply_text(f"🎬 {m['title']} ({m['release_date'][:4]})\n⭐ {m['vote_average']}\n📝 {m['overview']}")
    else:
        u.message.reply_text("❌ Movie not found!")

def main():
    up = Updater(BOT_TOKEN, use_context=True)
    dp = up.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('premium', premium))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, movie))
    up.start_polling()
    up.idle()

if __name__ == '__main__':
    main()
