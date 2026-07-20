from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8764326925:AAGf5SIHFfi9w4-OqMGEpcd6BPdYjMhIVPo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎵 Assalomu alaykum!\n\nBot muvaffaqiyatli ishga tushdi!")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot ishga tushdi...")
app.run_polling()
