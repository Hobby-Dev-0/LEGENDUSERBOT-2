from datetime import datetime
from telethon import events
from telethon.utils import get_display_name

from datetime import datetime
from telethon import events
from telethon.utils import get_display_name
from math import ceil
from re import compile
import asyncio
import html
import os
import re
import sys
from telethon import Buttons
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.channels import JoinChannelRequest

from userbot import *
from userbot.cmdhelp import *
from LEGENDBOT.utils import *
from userbot.Config import Config
from userbot import ALIVE_NAME
LEGEND_row = Config.BUTTONS_IN_HELP
LEGEND_emoji = Config.EMOJI_IN_HELP

from . import *

Owner_info_msg = f"""
**Owner** - {ALIV_NAME}
**OwnerID** - `{OWNER_ID}`
**Message Forwards** - {event.get("PMBOT")}
__Legend {LEGENDversion}, powered by @Legend_Userbot__
"""

_settings = [
    [
        Button.inline("API Kᴇʏs", data="apiset"),
        Button.inline("Pᴍ Bᴏᴛ", data="chatbot"),
    ],
    [
        Button.inline("Aʟɪᴠᴇ", data="alvcstm"),
        Button.inline("PᴍPᴇʀᴍɪᴛ", data="ppmset"),
    ],
    [Button.inline("Fᴇᴀᴛᴜʀᴇs", data="otvars")],
    [Button.inline("VC Sᴏɴɢ Bᴏᴛ", data="vcb")],
    [Button.inline("« Bᴀᴄᴋ", data="mainmenu")],
]

_start = [
    [
        Button.inline("Lᴀɴɢᴜᴀɢᴇ 🌐", data="lang"),
        Button.inline("Sᴇᴛᴛɪɴɢs ⚙️", data="setter"),
    ],
    [
        Button.inline("Sᴛᴀᴛs ✨", data="stat"),
        Button.inline("Bʀᴏᴀᴅᴄᴀsᴛ 📻", data="bcast"),
    ],
]



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ownerinfo")))
async def own(event):
    await event.edit(
        Owner_info_msg,
        buttons=[Button.inline("Close", data=f"closeit")],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"closeit")))
async def closet(event):
    await event.delete()



@tgbot.on(events.NewMessage(pattern="^/start", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    if event.is_group:
        if str(event.sender_id) in owner_and_sudos():
            return await event.reply(
                "`I dont work in groups`",
                buttons=[
                    Button.url(
                        "⚙️Sᴛᴀʀᴛ⚙️", url=f"https://t.me/Legend_Userbot?start=set"
                    )
                ],
            )
    else:
        if (
            not is_added(event.sender_id)
            and str(event.sender_id) not in owner_and_sudos()
        ):
            add_user(event.sender_id)
        if str(event.sender_id) not in owner_and_sudos():
            ok = ""
            u = await event.client.get_entity(event.chat_id)
            if not event.get("STARTMSG"):
                if event.get("PMBOT") == "True":
                    ok = "You can contact my master using this bot!!\n\nSend your Message, I will Deliver it To Master."
                await event.reply(
                    f"Hey Sir / ตíss, his is Legend Assistant of {ALIVE_NAME}!",
                    buttons=[Button.inline("Info.", data="ownerinfo")],
                )
            else:
                me = f"[{ALIVE_NAME}]"
                mention = f"[{DEFAULTUSER}](tg://user?id={bot.uid})"
                await event.reply(
                    Redis("STARTMSG").format(me=me, mention=mention),
                    buttons=[Button.inline("Info.", data="ownerinfo")],
                )
        else:
            name = get_display_name(event.sender_id)
            if event.pattern_match.group(1) == "set":
                await event.reply(
                    "Choose from the below options -",
                    buttons=_settings,
                )
            else:
                await event.reply(
                    get_string("ast_3").format(name),
                    buttons=_start,
                )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"mainmenu")))
async def _(event):
    if event.is_group:
        return
    await event.edit(
        get_string("ast_3").format(ALIVE_NAME),
        buttons=_start,
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stat")))
async def botstat(event):
    ok = len(get_all_users())
    msg = """LEGEND Assistant - Stats
Total Users - {}""".format(
        ok,
    )
    await event.answer(msg, cache_time=0, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"bcast")))
async def bdcast(event):
    ok = get_all_users()
    await event.edit(f"Broadcast to {len(ok)} users.")
    async with event.client.conversation(ALIVE_NAME) as conv:
        await conv.send_message(
            "Enter your broadcast message.\nUse /cancel to stop the broadcast.",
        )
        response = conv.wait_event(events.NewMessage(chats=ALIVE_NAME))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message("Cancelled!!")
        else:
            success = 0
            fail = 0
            await conv.send_message(f"Starting a broadcast to {len(ok)} users...")
            start = datetime.now()
            for i in ok:
                try:
                    await asst.send_message(int(i), f"{themssg}")
                    success += 1
                except BaseException:
                    fail += 1
            end = datetime.now()
            time_taken = (end - start).seconds
            await conv.send_message(
                f"""
Broadcast completed.
Total Users in Bot - {len(ok)}
Sent to all users.
Failed for 0user(s).""",
            )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"setting")))
async def setting(event):
    await event.edit(
        "Choose from the below options -",
        buttons=_settings,
    )
