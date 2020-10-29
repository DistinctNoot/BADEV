from replit import db
from discord.ext import commands

class tags(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def tag(self, ctx, name):
    try:
      val = db[f"tag: {name}"]
      await ctx.send(val)
    except:
      await ctx.send(f"Tag {name} not found")

  @commands.command()
  async def addtag(self, ctx, name, *, desc):
    try:
      val = db[f"tag: {name}"]
      await ctx.send(f"{name} tag is already exist!")
    except:
      db[f"tag: {name}"] = desc
      await ctx.send(f"Added tag named {name}")

  @commands.command()
  async def removetag(self, ctx, name):
    try:
      del db[f"tag: {name}"]
      await ctx.send(f"Deleted tag named {name}")
    except:
      await ctx.send(f"Tag does not exist")

  @commands.command()
  async def alltag(self, ctx, page=1):        
    matches = db.prefix("tag: ")
    s = ', '.join(matches)
    await ctx.send(s)

def setup(client):
    client.add_cog(tags(client))