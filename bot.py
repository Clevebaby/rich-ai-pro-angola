import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

PAIRS = ["EUR/USD", "GBP/USD", "USD/JPY"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"🚀 Bem-vindo ao Rich AI PRO Angola!\n\n"
"Comandos disponíveis:\n"
"/sinais - Consultar os pares Forex\n"
"/pares - Ver os pares disponíveis"
)

async def pares(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"📊 Pares disponíveis:\n" + "\n".join(PAIRS)
)

async def sinais(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"📈 RICH AI PRO ANGOLA\n\n"
"Os pares disponíveis são:\n"
"EUR/USD\nGBP/USD\nUSD/JPY\n\n"
"⚠️ Sistema em fase de configuração.\n"
"Ainda não existem sinais reais confirmados."
)

def main():
if not TOKEN:
raise ValueError("Token do Telegram não configurado.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pares", pares))
app.add_handler(CommandHandler("sinais", sinais))

app.run_polling()

if name == "main":
main()
