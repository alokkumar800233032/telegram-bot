import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.environ["TOKEN"]

WELCOME_TEXT = """
🎉 <b>WELCOME</b> 🎉

👋 Hello {name}

❤️ Welcome to AK GAMER CHAT ❤️

📜 <b>GROUP RULES</b>

1️⃣ Respect Everyone 🤝
2️⃣ 🚫 No Spam / No Abuse
3️⃣ 🚫 No Links Without Permission
4️⃣ 💚 Stay Active
"""

buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("📢 Channel", url="https://t.me/joing_ak_gamer_channel"),
        InlineKeyboardButton("👥 Group", url="https://t.me/Ak_gamer_chat"),
    ],
    [
        InlineKeyboardButton("💬 WhatsApp", url="https://whatsapp.com/channel/0029VbCO0u0G8l5AKfymSx00"),
        InlineKeyboardButton("▶️ YouTube", url="https://www.youtube.com/@AK_GAMER_900K"),
    ],
    [
        InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/ak_gamer_60k"),
        InlineKeyboardButton("👑 Owner", url="https://t.me/ak_gamers"),
    ],
])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Welcome Bot is Running!")


async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.new_chat_members:
        return

    for member in update.message.new_chat_members:
        name = member.mention_html()

        try:
            await context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=PHOTO_ID,
                caption=WELCOME_TEXT.format(name=name),
                parse_mode="HTML",
                reply_markup=buttons,
            )
        except Exception as e:
            print("Photo Error:", e)

            await update.effective_chat.send_message(
                text=WELCOME_TEXT.format(name=name),
                parse_mode="HTML",
                reply_markup=buttons,
            )


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome)
    )

    print("✅ Bot Started...")
    application.run_polling()


if __name__ == "__main__":
    main()