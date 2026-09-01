from pyrogram.enums import ParseMode, ButtonStyle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import LOGGER_ID
from Oneforall import app
from Oneforall.utils.database import is_on_off


def btn(text, emoji_id, style=ButtonStyle.DEFAULT, **kwargs):
    try:
        return InlineKeyboardButton(
            text=text,
            icon_custom_emoji_id=emoji_id,
            style=style,
            **kwargs
        )
    except TypeError:
        return InlineKeyboardButton(text=text, **kwargs)


async def play_logs(message, streamtype, link=None):
    if not await is_on_off(2):
        return

    if message.chat.id == LOGGER_ID:
        return

    chat_username = (
        f"@{message.chat.username}"
        if message.chat.username
        else "Private Group"
    )

    user_username = (
        f"@{message.from_user.username}"
        if message.from_user.username
        else "No Username"
    )

    query = (
        message.text.split(None, 1)[1]
        if len(message.text.split()) > 1
        else "Unknown"
    )

    logger_text = f"""
<b>🎵 {app.mention} Play Log</b>

<b>🏠 Chat ID :</b> <code>{message.chat.id}</code>
<b>📛 Chat Name :</b> {message.chat.title}
<b>🔗 Username :</b> {chat_username}

<b>👤 User ID :</b> <code>{message.from_user.id}</code>
<b>🙋 Name :</b> {message.from_user.mention}
<b>📎 Username :</b> {user_username}

<b>🔍 Query :</b> {query}
<b>📡 Stream Type :</b> {streamtype}
"""

    buttons = []
    row = []

    # Public / Private Group Link
    try:
        if message.chat.username:
            group_link = f"https://t.me/{message.chat.username}"
        else:
            group_link = await app.export_chat_invite_link(
                message.chat.id
            )

        row.append(
            btn(
                "Open Group",
                5438224604499819092,
                url=group_link,
                style=ButtonStyle.SUCCESS
            )
        )
    except Exception:
        pass

    # User Button
    row.append(
        btn(
            "Open User",
            6026236216079290036,
            url=f"tg://openmessage?user_id={message.from_user.id}",
            style=ButtonStyle.PRIMARY
        )
    )

    if row:
        buttons.append(row)

    # YouTube Button
    if link and (
        "youtube.com" in link
        or "youtu.be" in link
    ):
        buttons.append(
            [
                btn(
                    "YouTube",
                    6001604106190330097,
                    url=link,
                    style=ButtonStyle.DANGER
                )
            ]
        )

    try:
        await app.send_message(
            chat_id=LOGGER_ID,
            text=logger_text,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except Exception as e:
        print(f"Play Log Error: {e}")