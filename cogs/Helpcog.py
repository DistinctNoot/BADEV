  
import discord
from discord.ext import commands

class Helpcog(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.command(aliases=['Help'])
  async def help(self, ctx, category=None):
	  if (category == None):
		  category = await helpreg(ctx)
	  elif(category == "mod"):
		  category = await helpmod(ctx)
	  elif(category == "other"):
		  category = await helpother(ctx)
	  elif(category == "dev"):
		  category = await helpdeveloper(ctx)
	  else:
		  await ctx.send("Help page not found.")
  
async def helpreg(ctx):
      em = discord.Embed(title="BADEV's Developers tools!", description="Our normal commands", url="https://github.com/DistinctNoot/BADEV", color=0x9E0B0B)
      em.add_field(name="Moderation commands", value="Moderation commands")
      em.add_field(name="Developers commands", value="Commands for the Develoeprs")
      em.add_field(name="Fun commands", value="Commands for having fun!")
      em.add_field(name="Others", value="The `other` commands!")
      em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
      await ctx.send(embed=em)

async def helpmod(ctx):
      em = discord.Embed(title="BADEV's moderation commands!", description="Our moderation commands", url="https://github.com/DistinctNoot/BADEV/blob/master/cogs/moderation.py", color=0x9E0B0B)
      em.add_field(name="Ban", value="Example!\n`bd!ban @Tester Annoying me`")
      em.add_field(name="Kick", value="Example!\n`bd!kick @Tester Annoying me a little`")
      em.add_field(name="Unban", value="Example!\n`bd!unban 675689936673`")
      em.add_field(name="Purge", value="Example!\n`bd!purge 23`")
      em.add_field(name="Lockdown", value="lockdown a channel")
      em.add_field(name="embed", value="Make a special announcement")
      em.add_field(name="embedimg", value="Embed an image with words")
      em.add_field(name="embedsay", value="Make a personal announcement")
      em.add_field(name="embedsayimg", value="Make an embed personal announcement with images.")
      em.set_footer(icon_url=ctx.author.avatar_url, text=f" Requested by{ctx.author.name}")
      await ctx.send(embed=em)

async def helpother(ctx):
      em = discord.Embed(title="BADEV's `other` commands!", description="Our `other` commands", url="https://github.com/DistinctNoot/BADEV/blob/master/cogs/otherstuff.py", color=0x9E0B0B)
      em.add_field(name="AFK", value="Stop people from pinging you", inline=False)
      em.add_field(name="Ping", value="Want to game? check your ping!", inline=False)
      em.add_field(name="help", value="I think everyone knows this one", inline=False)
      em.add_field(name="user", value="Check user info!", inline=False)
      em.add_field(name="stats", value="Check how the bot's doing!", inline=False)
      em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
      await ctx.send(embed=em)

async def helpdeveloper(ctx):
	em = discord.Embed(title="Developer commands", description="Here are our developer commands", url = "https://tinyurl.com/y4gja7hv", color=0x9E0B0B)
	em.add_field(name="eval", value="Run code in discord!", inline=False)
	em.add_field(name="echo", value="print code!", inline=False)
	em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
	await ctx.send(embed=em)

def setup(client):
    client.add_cog(Helpcog(client))
    return