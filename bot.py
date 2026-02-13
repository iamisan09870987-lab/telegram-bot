import telebot
import openai

# ====== CONFIG ======
BOT_TOKEN = "8211814119:AAGpBAATk2GPbJFm4z07J2OJCpNUPFay6W0"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

OWNER_NAME = "@Hᴀʀᴜ!! "

# ====== START COMMAND ======
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f"hey !! 👋 Kaise ho {user_name} 😊\nMain {OWNER_NAME} ka friendly bot hoon 🤖✨\nKuch bhi pucho Hindi ya English me!")

# ====== AUTO REPLY ======
@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    try:
        user_text = message.text
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a friendly, happy Telegram bot. Reply in Hindi or English depending on user message. Keep tone cute, fun and positive."},
                {"role": "user", "content": user_text}
            ]
        )

        reply = response.choices[0].message.content
        bot.reply_to(message, reply)

    except Exception as e:
        bot.reply_to(message, "Oops 😅 Thoda technical problem ho gaya! Dobara try karo.")

# ====== RUN BOT ======
print("Bot is running...")
bot.infinity_polling()
