from pyrogram.types import InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton, ChatPrivileges

from Oneforall import app


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


@app.on_chat_member_updated()
async def admin_change_handler(client, message):
    old_status = message.old_chat_member
    new_status = message.new_chat_member

    if not old_status or not new_status:
        return

    chat_id = message.chat.id
    admin_user = message.from_user
    target_user = new_status.user
    new_title = new_status.custom_title or "No Title"

    # Promotion
    if old_status.status != new_status.status or old_status.privileges != new_status.privileges:

        if isinstance(new_status.privileges, ChatPrivileges):

            text = (
                "╭─────────────────\n"
                "├ 🟢 ADMIN PROMOTED\n"
                f"├ 👤 By : {admin_user.mention}\n"
                f"├ 🎯 User : {target_user.mention}\n"
                f"├ 🏷 Title : {new_title}\n"
                "╰─────────────────"
            )

            keyboard = InlineKeyboardMarkup(
                [[
                    btn(
                        "Promoted",
                        6001604106190330097,
                        style=ButtonStyle.SUCCESS,
                        callback_data="ignore"
                    )
                ]]
            )

        else:

            text = (
                "╭─────────────────\n"
                "├ 🔴 ADMIN DEMOTED\n"
                f"├ 👤 By : {admin_user.mention}\n"
                f"├ 🎯 User : {target_user.mention}\n"
                "╰─────────────────"
            )

            keyboard = InlineKeyboardMarkup(
                [[
                    btn(
                        "Demoted",
                        6026236216079290036,
                        style=ButtonStyle.DANGER,
                        callback_data="ignore"
                    )
                ]]
            )

        await client.send_message(
            chat_id,
            text,
            reply_markup=keyboard
        )

    # Title Changed
    elif old_status.custom_title != new_status.custom_title:

        text = (
            "╭─────────────────\n"
            "├ 🏷 TITLE CHANGED\n"
            f"├ 👤 By : {admin_user.mention}\n"
            f"├ 🎯 User : {target_user.mention}\n"
            f"├ ✨ New Title : {new_title}\n"
            "╰─────────────────"
        )

        keyboard = InlineKeyboardMarkup(
            [[
                btn(
                    "Title Updated",
                    5438224604499819092,
                    style=ButtonStyle.PRIMARY,
                    callback_data="ignore"
                )
            ]]
        )

        await client.send_message(
            chat_id,
            text,
            reply_markup=keyboard
        )