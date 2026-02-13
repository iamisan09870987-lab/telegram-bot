# requirements: pip install python-telegram-bot --upgrade

import logging
import random
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

TOKEN = "8335880993:AAG7muwvIBk6dzOYD9sN_2PvBeqncVXzvBY"

OWNER_NAME = "@Hᴀʀᴜ!!"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name or "dost"
    mention = f"@{user.username}" if user.username else name

    msg = (
        f"Heyy !! 👋 Kaise ho {mention} ❤️\n\n"
        f"Mai {OWNER_NAME} ka full desi + cool bot hu ~\n"
        "Hindi mein, English mein, jo bhi bolega – full masti se jawab dunga 😜🔥\n"
        "Ab bol na, kya scene hai? ✌️"
    )
    await update.message.reply_text(msg)

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower().strip()
    user = update.effective_user
    name = user.first_name or "bhai"

    # Quick matches (Hindi + English mix)
    quick = {
        "hi": f"Arre hi {name}!! 😍 Kya haal-chaal?",
        "hello": f"Hello hello {name} cutu 🫶 Kya scene hai?",
        "kya kar rahe ho": f"Bas tere message ka wait kar raha tha yaar 😜 Tu bata kya chal raha?",
        "kaisa hai": f"Ek number mast hu bhai! 😎 Tu kaise hai meri jaan? 💕",
        "bored hu": f"Arre bore mat ho yaar! Chal koi mast plan banate hain 😈",
        "good morning": f"Good morning {name} ☀️ Subah se hi glow kar raha hai tu!",
        "good night": f"Good night {name} ~ sweet dreams, sapno mein milte hain 😘✨",
        "i love you": f"Awww I love you too {name}!! 😳💖 (par {OWNER_NAME} ko thoda zyada line deti hu hehe)",
        "owner kaun hai": f"Mera pyara owner hai {OWNER_NAME} 💙 Sabse top banda!",
        "sorry": f"Arre sorry kis baat ka bhai? Tu toh already perfect hai 🥰",
        "kya haal hai": f"Halwa puri jaisa haal hai mera 😋 Tu bata?",
    }

    if text in quick:
        await update.message.reply_text(quick[text])
        return

    # Keyword logic (Hindi + English)
    if any(w in text for w in ["love", "pyar", "i love u", "pasand", "dil"]):
        await update.message.reply_text(f"Awww {name} kitna sweet hai tu yaar 🥺💞 Hugsss bhej raha hu!")
    
    elif any(w in text for w in ["sad", "dukhi", "rona", "bore", "depress", "udass"]):
        await update.message.reply_text(f"Arre ro mat bhai 😢 Aa gale lag ja... sab theek ho jayega, pakka! 🤗")
    
    elif any(w in text for w in ["happy", "khush", "mast", "maza", "party"]):
        await update.message.reply_text(f"Yayyyy {name} khush hai toh full party mode ON! 🥳🎉")
    
    elif "?" in text or any(w in text for w in ["kya", "kaise", "kab", "kyun", "kitna", "bata", "bol"]):
        await update.message.reply_text(
            f"Hmmmmm {name} mast sawal poocha 🤔\n"
            f"Soch raha hu... tu pehle bata tujhe kya lag raha hai? 😏🔥"
        )
    
    else:
        # Random desi + friendly replies
        random_replies = [
            f"{name}!! 😍 Aaj tu extra swag mein kyun lag raha hai bhai? ✨",
            f"Waah kya baat boli tune yaar! 🔥 Ab bol agli party kab hai?",
            f"Tere messages padh ke din ban jata hai {name} 🫶",
            f"Ek second... tu itna mast kaise hai bhai? 😳 Secret bata de",
            f"{OWNER_NAME} ne bola tha tu full awesome hai... 100% sach nikla! 😎",
            f"Bas aise hi baatein karte raho na... kabhi bore nahi hota 🥰",
            f"Arre tu toh full form mein hai aaj! 🔥 Kya bol raha scene?",
            f"{name} ke saath baat karne mein full maza aa raha hai 😄✨",
            f"Bhai tu bol, mai sun raha hu full dhyan se 🔥",
        ]
        await update.message.reply_text(random.choice(random_replies))

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            auto_reply
        )
    )

    print("Bot chal pada hai... full desi masti mode ON 🚀🔥")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
