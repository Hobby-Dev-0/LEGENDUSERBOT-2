#originally created by @Legend_Mr_Hacker

#team LEGEND
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import bot
from userbot import CmdHelp

@bot.on(admin_cmd(pattern=r"allban", outgoing=True))
async def testing(event):
    nikal = await event.get_chat()
    chutiya = await event.client.get_me()
    admin = nikal.admin_rights
    creator = nikal.creator
    if not admin and not creator:
        await event.edit(" U Don't have sufficient permission 🧐 u noob 😑😑")
        return
    await event.edit("Doing Nothing 🙃🙂")#Kang with Credits
# for LEGENDBOT
    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == chutiya.id:
            pass
        try:
            await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
        except Exception as e:
            await event.edit(str(e))
        await sleep(.5)
    await event.edit("Nothing Happend here🙃🙂")
CmdHelp("allban").add_command(
    'allban', 'None', 'U can Ban Member In Group'
)
