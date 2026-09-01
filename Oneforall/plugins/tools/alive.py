from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import MUSIC_BOT_NAME
from Oneforall import app


@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://files.catbox.moe/l0r3oo.mp4",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention}\n\n🔮 ɪ ᴀᴍ {MUSIC_BOT_NAME}\n\n✨ ɪ ᴀᴍ ғᴀsᴛ ᴀɴᴅ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.\n\n💫 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴊᴏɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ🤍...\n\n━━━━━━━━━━━━━━━━━━❄",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Queen", url=f"tg://openmessage?user_id=8676835917"
                    ),
                    InlineKeyboardButton(
                        text=" ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/Roohi_Soul_Gc"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text=" ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/Roohi_Soul"
                    ),
                ],
                [InlineKeyboardButton("✯ ᴄʟᴏsᴇ ✯", callback_data="close")],
            ]
        ),
    )
