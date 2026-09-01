import os
import asyncio
import yt_dlp

from pyrogram import filters
from pyrogram.types import Message

from Oneforall import app   # apne main bot instance ka import

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


# ---------- YT-DLP DOWNLOAD FUNCTION ----------
def download_youtube(url: str) -> str:
    """Download youtube short/video and return file path"""

    ydl_opts = {
        "format": "mp4/best",
        "outtmpl": f"{DOWNLOAD_DIR}/%(title).80s.%(ext)s",
        "noplaylist": True,
        "quiet": True,
        "merge_output_format": "mp4",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

        # ensure mp4 extension
        if not filename.endswith(".mp4"):
            filename = os.path.splitext(filename)[0] + ".mp4"

        return filename


# ---------- COMMAND HANDLER ----------
@app.on_message(filters.command("ytshort") & filters.private)
async def ytshort_handler(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text(
            "❌ Usage:\n/ytshort <youtube shorts link>"
        )

    url = message.text.split(None, 1)[1]

    status = await message.reply_text("⏳ Downloading YouTube Short...")

    try:
        file_path = await asyncio.to_thread(download_youtube, url)

        await status.edit("📤 Uploading video...")

        await message.reply_video(
            video=file_path,
            caption="✅ Here is your downloaded YouTube Short"
        )

        await status.delete()

        # cleanup file
        try:
            os.remove(file_path)
        except:
            pass

    except Exception as e:
        await status.edit(f"❌ Error:\n{str(e)}")