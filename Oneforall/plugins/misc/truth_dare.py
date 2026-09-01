import aiohttp

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from Oneforall import app

TRUTH_API = "https://api.truthordarebot.xyz/v1/truth"
DARE_API = "https://api.truthordarebot.xyz/v1/dare"


async def fetch_question(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data.get("question")
    except Exception:
        return None


@app.on_message(filters.command("truth"))
async def truth_cmd(_, message):

    question = await fetch_question(TRUTH_API)

    if not question:
        return await message.reply_text(
            "❌ Failed to fetch truth question."
        )

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🎭 New Truth",
                    callback_data="truth_refresh"
                )
            ]
        ]
    )

    await message.reply_text(
        f"""
✨ **TRUTH QUESTION**

💭 {question}
""",
        reply_markup=keyboard
    )


@app.on_message(filters.command("dare"))
async def dare_cmd(_, message):

    question = await fetch_question(DARE_API)

    if not question:
        return await message.reply_text(
            "❌ Failed to fetch dare challenge."
        )

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔥 New Dare",
                    callback_data="dare_refresh"
                )
            ]
        ]
    )

    await message.reply_text(
        f"""
🔥 **DARE CHALLENGE**

🎯 {question}
""",
        reply_markup=keyboard
    )


@app.on_callback_query(filters.regex("^truth_refresh$"))
async def refresh_truth(_, query: CallbackQuery):

    question = await fetch_question(TRUTH_API)

    if not question:
        return await query.answer(
            "Failed to fetch question",
            show_alert=True
        )

    await query.message.edit_text(
        f"""
✨ **TRUTH QUESTION**

💭 {question}
""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🎭 New Truth",
                    callback_data="truth_refresh"
                )
            ]]
        )
    )


@app.on_callback_query(filters.regex("^dare_refresh$"))
async def refresh_dare(_, query: CallbackQuery):

    question = await fetch_question(DARE_API)

    if not question:
        return await query.answer(
            "Failed to fetch challenge",
            show_alert=True
        )

    await query.message.edit_text(
        f"""
🔥 **DARE CHALLENGE**

🎯 {question}
""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🔥 New Dare",
                    callback_data="dare_refresh"
                )
            ]]
        )
    )