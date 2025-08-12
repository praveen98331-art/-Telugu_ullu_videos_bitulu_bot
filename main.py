from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7912733347:AAFeuZDn544pkmd7bUwcRLSBfqjqxYkCnkU"
CHANNEL_LINK = "https://t.me/+dt6vu048PjFjMjU1"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"💥 Welcome! Join our channel here:\n{CHANNEL_LINK}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
