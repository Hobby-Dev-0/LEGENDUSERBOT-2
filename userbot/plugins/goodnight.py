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
                   
CmdHelp("goodnight").add_command(
  'gn', None, 'use and see'
).add()
