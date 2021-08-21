from superos import bot, CMD_HELP, ALIVE_NAME
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from LEGENDBOT.utils import admin_cmd, sudo_cmd, edit_or_reply
from superos.supercmds.cmdhelp import CmdHelp
import html
from telethon import events
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from telethon.events import ChatAction
from . import *

Legend_Mr_Hacker = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND User"
papa = borg.uid


async def get_full_user(event):  
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await edit_or_reply(event, "**Som3thing W3nt Wr0ng**\n`Can you please provide me a user id`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await edit_or_reply(event, "**Som3thing W3nt Wr0ng**\n", str(err))           
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await edit_or_reply(event, str(err))
        return None
    return user_obj

@bot.on(admin_cmd(pattern="gban ?(.*)"))
@bot.on(sudo_cmd(pattern="gban ?(.*)", allow_sudo=True))
async def gban(superos):
    if superos.fwd_from:
        return
    ids = superos
    sender = await ids.get_sender()
    hum = await ids.client.get_me()
    if not sender.id == hum.id:
        LEGENDBOT = await edit_or_reply(ids, "Trying to gban this retard!")
    else:
        LEGENDBOT = await edit_or_reply(ids, "`Ok! Gban ho rha h intzarrr karo....`")
    hum = await superos.client.get_me()
    await LEGENDBOT.edit(f"`🔥Global Ban ho rha h ruko'💦....dekhte jaao bus kya hota h 😎 `")
    my_mention = "[{}](tg://user?id={})".format(hum.first_name, hum.id)
    f"@{hum.username}" if hum.username else my_mention
    await superos.get_chat()
    a = b = 0
    if superos.is_private:
        user = superos.chat
        reason = superos.pattern_match.group(1)
    else:
        superos.chat.title
    try:
        user, reason = await get_full_user(superos)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await LEGENDBOT.edit(f"**Something W3NT Wrong 🤔**")
    if user:
        if user.id == 1856561912:
            return await LEGENDBOT.edit(
                f"`First Grow Some Balls To Gban My Creater🤫🚶`"
            )
        try:
            from superos.modules.sql_helper.gmute_sql import gmute
        except:
            pass
        try:
            await superos.client(BlockRequest(user))
        except:
            pass
        testsuperos = [
            d.entity.id
            for d in await superos.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testsuperos:
            try:
                await superos.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await LEGENDBOT.edit(f"Gbaning ho rha h 😂\n\nTotal Chats :- `{a}`")
            except:
                b += 1
    else:
        await LEGENDBOT.edit(f"`Either reply to a user or gib me user id/name`")
    try:
        if gmute(user.id) is False:
            return await LEGENDBOT.edit(f"**Error! User phle se chuda(Gbanned) pda h 😂 .**")
    except:
        pass
    return await LEGENDBOT.edit(
        f"[{user.first_name}](tg://user?id={user.id}) \n\n**Gban Successful This Nube 🔥\nAffected Chats😏 : {a} **"
    )

@bot.on(admin_cmd(pattern="ungban ?(.*)"))
@bot.on(sudo_cmd(pattern="ungban ?(.*)", allow_sudo=True))
async def gunban(superos):
    if superos.fwd_from:
        return
    ids = superos
    sender = await ids.get_sender()
    hum = await ids.client.get_me()
    if not sender.id == hum.id:
        LEGENDBOT = await edit_or_reply(ids, "`Trying to ungban this kid...`")
    else:
        LEGENDBOT = await edit_or_reply(ids, "`Ungban in progress...`")
    hum = await superos.client.get_me()
    await LEGENDBOT.edit(f"`Trying to ungban this kiddo...`")
    my_mention = "[{}](tg://user?id={})".format(hum.first_name, hum.id)
    f"@{hum.username}" if hum.username else my_mention
    await superos.get_chat()
    a = b = 0
    if superos.is_private:
        user = superos.chat
        reason = superos.pattern_match.group(1)
    else:
        superos.chat.title
    try:
        user, reason = await get_full_user(superos)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await LEGENDBOT.edit("**Som3ting W3nt Wr0ng**")
    if user:
        if user.id == 1856561912:
            return await LEGENDBOT.edit("**You need to grow some balls to gban / ungban my creator**")
        try:
            from superos.modules.sql_helper.gmute_sql import ungmute
        except:
            pass
        try:
            await superos.client(UnblockRequest(user))
        except:
            pass
        testsuperos = [
            d.entity.id
            for d in await superos.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testsuperos:
            try:
                await superos.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await LEGENDBOT.edit(f"Ok! Now Ungbaning ho rha h nhi to yhi patak kr chod dete.\nChats:- `{a}`")
            except:
                b += 1
    else:
        await LEGENDBOT.edit("**Reply to a user**")
    try:
        if ungmute(user.id) is False:
            return await LEGENDBOT.edit("**Error! User already ungbanned.**")
    except:
        pass
    return await LEGENDBOT.edit(
        f"**[{user.first_name}](tg://user?id={user.id}) Purani Baate bhul jaa... ab Friend ban ja 😂.**\n\nUngban Successful 🔥\nChats :- `{a}`"
    )




@borg.on(ChatAction)
async def handler(legend): 
   if legend.user_joined or legend.user_added:      
       try:       	
         from superos.plugins.sql_helper.gmute_sql import is_gmuted
         guser = await legend.get_user()      
         gmuted = is_gmuted(guser.id)             
       except:      
          return
       if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):                                                                         
                chat = await legend.get_chat()
                admin = chat.admin_rights
                creator = chat.creator   
                if admin or creator:
                 try:
                    await client.edit_permissions(legend.chat_id, guser.id, view_messages=False)                              
                    await legend.reply(
                     f"⚠️⚠️**Warning**⚠️⚠️\n\n`Gbanned User Joined the chat!!`\n"                      
                     f"**⚜️ Victim Id ⚜️**:\n[{guser.id}](tg://user?id={guser.id})\n"                   
                     f"**🔥 Action 🔥**  :\n`Banned this piece of shit....` **AGAIN!**")                                                
                 except:       
                    legend.reply("`Sheit!! No permission to ban users.\n@admins ban this retard.\nGlobally Banned User And A Potential Spammer`\n**Make your group a safe place by cleaning this shit**")                   
                    return
                  
                  
CmdHelp("gban_gmute").add_command(
  'gban', '<reply> / <userid> / <username>', 'Gbans the targeted user and adds to gban watch list'
).add_command(
  'ungban', '<reply> / <userid> / <username>', 'Unbans the targeted user and removes them from gban watch list. Grants another Chance'
).add_command(
  'gmute', '<reply>/ <userid>/ <username>', 'Gmutes the targeted user. Works only if you have delete msg permission. (Works on admins too)'
).add_command(
  'ungmute', '<reply>/ <userid>/ <username>', 'Ungmutes the user. Now targeted user is free'
).add()
