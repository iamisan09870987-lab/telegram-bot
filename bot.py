import telebot

TOKEN = "8498450887:AAG-TLTZsPQFGzfQPxQaoBMv-r26gQGbfxU"

bot = telebot.TeleBot(TOKEN)

# Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, " hey !!👋 kese ho sab thik !! 😊")

# Text messages
@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text.lower()

    # Owner name question detect
    if "owner" in text or "admin" in text or "malik" in text:
        bot.reply_to(message, "Mere owner hain 👉 @Hᴀʀᴜ!! 😎🔥")

    else:
        bot.reply_to(message, f"Tumne bola: {message.text} 😄")

# Sticker reply
@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    bot.reply_to(message, "Nice sticker 😂🔥")

print("Bot running...")
bot.infinity_polling()
