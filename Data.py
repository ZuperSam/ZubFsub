from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
**ʜᴇʏ {}**

**ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}**

**ɪ ᴄᴀɴ ꜰᴏʀᴄᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ'ꜱ ᴜꜱᴇʀꜱ ᴛᴏ ᴊᴏɪɴ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ.**
**ᴛʜᴇ ᴄʜᴀᴛ ᴄᴀɴ ʙᴇ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ. ɪᴛ ᴄᴀɴ ʙᴇ ᴘʀɪᴠᴀᴛᴇ ᴏʀ ᴘᴜʙʟɪᴄ.** ⚡

**ᴜꜱᴇ ʙᴜᴛᴛᴏɴꜱ ʙᴇʟᴏᴡ ᴛᴏ ᴍᴏʀᴇ. 😍**

**ʙʏ ꜱʟ-ᴀʟᴘʜᴀ-x ᴛᴇᴀᴍ ⚡**
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="↺ ʀᴇᴛᴜʀɴ ᴛᴏ ʜᴏᴍᴇ", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("⚡ ꜰᴏʀ ᴍᴏʀᴇ ʙᴏᴛꜱ", url="https://t.me/Zub0NSFWupdateS")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ❔", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ ℹ️", callback_data="about")
        ],
        [InlineKeyboardButton("ꜰᴏʀ ꜱᴜᴘᴘᴏʀᴛ 👨‍💻", url="https://t.me/+q4h6ckbdeXplOTFl")],
    ]

    # Help Message
    HELP = """
⚡ Add me as **Admin** to a group.

⚡ Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private.

⚡ Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub -100xxxxxxxxxx` or `/forcesubscribe -100xxxxxxxxxx`

⚡ [Coustomize] Use /settings to change settings!

⚡ You are good to go. Leave the rest to me.

✨ **Available Commands** ✨

/fsub - See current force subscribe chat
/fsub chat_id/username - Force users to join the particular chat
/settings - Change Group Settings
/id - Get the chat id of any group or channel
/about - About The Bot
/help - This Message
/start - Start the Bot

**ℹ️ Note** - You can also use `/forcesubscribe` instead of `/fsub` ⚡
    """

    # About Message
    ABOUT = """
**ℹ️ ᴀʙᴏᴜᴛ** 

ᴀ ᴛᴇʟᴇɢʀᴀᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ʙᴏᴛ ʙʏ [ꜱʟ ᴀʟᴘʜᴀ-x ᴛᴇᴀᴍ](SL_AlphaX_Team)

⭐ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/SL-Alpha-X-Team/ForceSubscribeBot)

⭐ ꜰʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏᴏɢʀᴀᴍ](docs.pyrogram.org)

⭐ ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](www.python.org)

⭐ ᴅᴇᴠᴏʟᴏᴘᴇʀ : [ʏᴏᴜ 😍🔥](tg://settings)
    """
