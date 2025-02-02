import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
    BotCommand,
)
from utils import is_check_admin
from Script import script
from info import ADMINS


@Client.on_message(filters.command("grp_cmds"))
async def grp_cmds(client, message):
    user_id = message.from_user.id if message.from_user else None
    if not user_id:
        return await message.reply(
            "<b>💔 ʏᴏᴜ ᴀʀᴇ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ...</b>"
        )
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("<code>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ.</code>")
    grp_id = message.chat.id
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text("<b>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ</b>")
    # title = message.chat.title
    buttons = [[InlineKeyboardButton("❌ ᴄʟᴏsᴇ ❌", callback_data="close_data")]]
    await message.reply_text(
        text=script.GROUP_C_TEXT,
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode=enums.ParseMode.HTML,
    )


@Client.on_message(filters.command("admin_cmds") & filters.user(ADMINS))
async def admin_cmds(client, message):
    buttons = [
        [KeyboardButton("/add_premium"), KeyboardButton("/premium_users")],
        [KeyboardButton("/remove_premium"), KeyboardButton("/add_redeem")],
        [KeyboardButton("/refresh"), KeyboardButton("/set_muc")],
        [KeyboardButton("/pm_search_on"), KeyboardButton("/pm_search_off")],
        [KeyboardButton("/set_ads"), KeyboardButton("/del_ads")],
        [KeyboardButton("/setlist"), KeyboardButton("/clearlist")],
        [KeyboardButton("/verify_id"), KeyboardButton("/index")],
        [KeyboardButton("/send"), KeyboardButton("/leave")],
        [KeyboardButton("/ban"), KeyboardButton("/unban")],
        [KeyboardButton("/broadcast"), KeyboardButton("/grp_broadcast")],
        [KeyboardButton("/delreq"), KeyboardButton("/channel")],
        [KeyboardButton("/del_file"), KeyboardButton("/delete")],
        [KeyboardButton("/deletefiles"), KeyboardButton("/deleteall")],
        [KeyboardButton("All These Commands Can Be Used Only By Admins.")],
        [KeyboardButton("⚡")],
    ]
    reply_markup = ReplyKeyboardMarkup(
        buttons, resize_keyboard=True, one_time_keyboard=True
    )

    sent_message = await message.reply(
        "<b>Admin All Commands [auto delete 2 min] 👇</b>",
        reply_markup=reply_markup,
    )
    #  2 minutes (120 seconds)
    await asyncio.sleep(120)
    await sent_message.delete()
    await message.delete()


@Client.on_message(filters.command("commands") & filters.user(ADMINS))
async def set_commands(client, message):
    commands = [
        BotCommand("start", "🚀 𝗦𝘁𝗮𝗿𝘁 𝗧𝗵𝗲 𝗕𝗼𝘁"),
        BotCommand("most", "🔥 𝗠𝗼𝘀𝘁 𝗦𝗲𝗮𝗿𝗰𝗵𝗲𝗱 𝗕𝘂𝘁𝘁𝗼𝗻 𝗟𝗶𝘀𝘁"),
        BotCommand("trend", "📈 𝗧𝗼𝗽 𝗧𝗿𝗲𝗻𝗱𝗶𝗻𝗴 𝗕𝘂𝘁𝘁𝗼𝗻 𝗟𝗶𝘀𝘁"),
        BotCommand("mostlist", "📊 𝗦𝗵𝗼𝘄 𝗠𝗼𝘀𝘁 𝗦𝗲𝗮𝗿𝗰𝗵𝗲𝗱 𝗟𝗶𝘀𝘁"),
        BotCommand("trendlist", "📉 𝖳𝗈𝗉 𝖳𝗋𝖾𝗇𝖽𝗂𝗇𝗀 𝖫𝗂𝗌𝗍"),
        BotCommand("plan", "💎 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗠𝗲𝗺𝗯𝗲𝗿𝘀𝗵𝗶𝗽 𝗣𝗹𝗮𝗻𝘀"),
        BotCommand("myplan", "📜 𝗬𝗼𝘂𝗿 𝗖𝘂𝗿𝗿𝗲𝗻𝘁 𝗣𝗹𝗮𝗻"),
        BotCommand("refer", "🎁 𝗥𝗲𝗳𝗲𝗿 𝗮 𝗙𝗿𝗶𝗲𝗻𝗱 & 𝗘𝗮𝗿𝗻 𝗣𝗿𝗲𝗺𝗶𝘂𝗺"),
        BotCommand("stats", "📂 𝗖𝗵𝗲𝗰𝗸 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝗦𝘁𝗮𝘁𝘀"),
        BotCommand("id", "🆔 𝗚𝗲𝘁 𝗬𝗼𝘂𝗿 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗜𝗗"),
        BotCommand("font", "🔠 𝗖𝗼𝗼𝗹 𝗙𝗼𝗻𝘁 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗼𝗿"),
        BotCommand("details", "📌 𝗖𝗵𝗲𝗰𝗸 𝗚𝗿𝗼𝘂𝗽 𝗗𝗲𝘁𝗮𝗶𝗹𝘀"),
        BotCommand("settings", "⚙️ 𝗕𝗼𝘁 𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀"),
        BotCommand("grp_cmds", "📢 𝗚𝗿𝗼𝘂𝗽 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀"),
        BotCommand("admin_cmds", "🛠️ 𝗕𝗼𝘁 𝗔𝗱𝗺𝗶𝗻 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀"),
    ]
    await client.set_bot_commands(commands)
    await message.reply("Set command successfully✅ ")
