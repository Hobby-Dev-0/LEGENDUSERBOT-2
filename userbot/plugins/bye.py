import asyncio
from userbot.utlis import admin_cmd
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd(pattern="byeall"))
async def bye(ult):
	await ult.edit("Guys I Gotta Go!")
	await asyncio.sleep(1)
	await ult.edit("""
	
┏━━┳┓╋╋┏┳━━━┓
┃┏┓┃┗┓┏┛┃┏━━┛
┃┗┛┗┓┗┛┏┫┗━━┓
┃┏━┓┣┓┏┛┃┏━━┛
┃┗━┛┃┃┃╋┃┗━━┓
┗━━━┛┗┛╋┗━━━┛
""")
CmdHelp("bye").add_command(
'byeall', None, 'Say Bye to U all in anmation'
).add()