import discord
import logging
import datetime
import os
import sys
import subprocess
import time
import json
from discord.ext import commands
from keep_alive import keep_alive

sys.dont_write_bytecode = True

intents = discord.Intents.default()

with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []


client = commands.Bot(command_prefix="bd!", help_command=None, intents=intents.all())

subprocess.Popen(['java', '-jar', 'Lavalink.jar'])
time.sleep(40)


@client.event
async def on_ready():
    logging.basicConfig(filename="log.txt", filemode="a", format="%(asctime)s %(msecs)d- %(process)d -%(levelname)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S %p", level=logging.INFO)

    channel = client.get_channel(769374818298495076)
    tn = datetime.datetime.utcnow()
    await channel.send(f'{tn.strftime("%c")} log, timezone: UTC', file=discord.File('log.txt'))
    #await channel.send(file=discord.File("spring.log"))
    with open("log.txt", "r+") as f:
        f.truncate()
    #with open("./logs/spring.log", "r") as r:
        #r.truncate()
    await client.change_presence(
	    activity=discord.Activity(
	        type=discord.ActivityType.watching,
	        name=f'over British Airways Coding!'))
    print('Bot Started')

    for filename in os.listdir('./cogs'):
	    if filename.endswith('.py'):
		    client.load_extension(f'cogs.{filename[:-3]}')
		    print(f'loading {filename}')
    #print all command
    testlist = []
    for i in client.commands:
      print(i)
      testlist.append(i.name)
    print(testlist)

keep_alive()
client.run(os.getenv("DISCORD_TOKEN"))