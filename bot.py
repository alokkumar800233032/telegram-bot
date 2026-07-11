from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = "8870938287:AAHXMEPO2qf432pPfSpIZuzW2cWgus6AD5k"

WELCOME_PHOTO = "AgACAgUAAxkBAAEgUBpqUcUbVBabPK_S147HlOiTtKU40AACdhBrG_xMkFZ9ceP8_CUJyQEAAwIAA3kAAzwE"

WELCOME_TEXT = """
🌟 WELCOME 🌟

💗 Hello..

👤 Name : {first_name}
🆔 Username : @{username}

📎 Welcome to ❣️ AK GAMER CHAT ❣️

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📜 GROUP RULES 📌

1️⃣ Respect Everyone 🤝
2️⃣ 🚫 No Spam / No Abuse
3️⃣ 🚫 No Links Without Permission
4️⃣ 💚 Stay Active

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

buttons = InlineKeyboardMarkup([
    keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("📢 Channel", url="https://t.me/joing_ak_gamer_channel"),
        InlineKeyboardButton("👥 Group", url="https://t.me/Ak_gamer_chat")
    ],
    [
        InlineKeyboardButton("💬 WhatsApp", url="https://whatsapp.com/channel/0029VbCO0u0G8l5AKfymSx00"),
        InlineKeyboardButton("▶️ YouTube", url="https://www.youtube.com/@AK_GAMER_900K")
    ],
    [
        InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/ak_gamer_60k?igsh=MWtsbG85cHdrbGoydw=="),
        InlineKeyboardButton("👑 Owner", url="https://t.me/ak_gamers")
    ]
])
    if not update.message or not update.message.new_chat_members:
        return

    for member in update.message.new_chat_members:

        username = (
            f"@{member.username}"
            if member.username
            else "No Username"
        )

        caption = WELCOME_TEXT.format(
            first_name=member.first_name,
            username=username.replace("@", "")
        )

        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=WELCOME_PHOTO,
            caption=caption,
            reply_markup=buttons,
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(
        filters.StatusUpdate.NEW_CHAT_MEMBERS,
        welcome
    )
)# ==========================
# START BOT
# ==========================

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")

app.add_error_handler(error_handler)

print("✅ AK GAMER Welcome Bot Started...")
print("🚀 Waiting for new members...")

app.run_polling(
    allowed_updates=Update.ALL_TYPES,
    drop_pending_updates=True
)