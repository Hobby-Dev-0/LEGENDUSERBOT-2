import asyncio
from . import *
@bot.on(admin_cmd(pattern="gn"))
async def _(event):
	await asyncio.sleep(1)
	await event.edit("""
  ┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█
┌▀█╔══╗╔══╗╔══╗╔══╗▀█
┌▀█║╔═╣║╔╗║║╔╗║╚╗╗║▀█
┌▀█║╚╗║║╚╝║║╚╝║╔╩╝║▀█
┌▀█╚══╝╚══╝╚══╝╚══╝▀█
┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█
┌▀█░░░░░░░░░░░░░░░░▀█
┌▀█░░█▌▌█▐▀▐░▌▀█▀░░▀█
┌▀█░░█▐▌█▐▐▐▀▌░█░░░▀█
┌▀█░░█░▌█▐█▐░▌░█░░░▀█
┌▀█░░░░░░░░░░░░░░░░▀█
┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█ 
🌙.     *       ☄️      
🌟   .  *       .         
                       *   .      🛰     .        ✨      *
  .     *   SLEEP WELL        🚀     
      .              . . SWEET DREAMS 🌙
. *       🌏 GOOD NIGHT         *
                     🌙.     *       ☄️      
🌟   .  *       .         
                       *   .      🛰     .        ✨      *
"""
CmdHelp("botstatus").add_command( 
	'bot', None, 'Use and See'
).add()


