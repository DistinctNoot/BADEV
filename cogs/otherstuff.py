import discord
from replit import db
import discord.utils
from discord.ext import commands

class otherstuff(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['afk'])
  async def AFK(self,ctx, *, reason="`AFK`"):
    var = discord.utils.get(ctx.guild.roles, name = "AFK")
    var2 = discord.utils.get(ctx.guild.roles, name = "Flight Notifications")
    try:
      del db[ctx.author.id]
      nick1 = f"[AFK] {ctx.author.display_name}"
      nick2 = nick1.replace('[AFK]','')
      await ctx.send(f"Welcome back {ctx.author.mention}, i removed your AFK")
      try:
        await ctx.author.remove_roles(var)
        await ctx.author.add_roles(var2)
      except:
        print("cant update role")
      finally:
        try:
          await ctx.author.edit(nick=nick2)
        except:
          print("Cant rename")
    except:      
      db[ctx.author.id] = reason
      await ctx.send(f"I set you AFK: {reason}" .format(reason))
      try:
        await ctx.author.remove_roles(var2)
        await ctx.author.add_roles(var)
      except:
        print("cant change role")
      finally:
        try:
          await ctx.author.edit(nick=f"[AFK] {ctx.author.display_name}")
        except:
          print("Cant rename")
        
  @commands.command()
  async def count(self, ctx, mode, num1:int, num2:int):
    if mode == '+':
      total = num1 + num2
    elif mode == '-':
      total = num1 - num2
    elif mode == '*':
      total = num1 * num2
    elif mode == '/':
      total = num1 // num2
    else:
      total = "invalid operation"
    await ctx.send(str(total))
  
  @commands.command()
  async def check(self, ctx, user: discord.User, role):
    channel = await user.create_dm()
    fltime = "3 pm BST" #replace with DB later
    flnumber = "example" #replace with DB later
    if role.lower() == "pilot":
      check = discord.Embed(title=f"Flight at {fltime}", description=f"You've been selected to be todays pilot on flight {flnumber}. \n\nIf you are available at {fltime} please use the tick reaction below in the next **20 minutes**, if not please choose the cross!", color=0xff0000)
      check.set_author(name="BA Staff Team", icon_url="http://logok.org/wp-content/uploads/2014/04/British-Airways-logo-ribbon-logo.png")
    elif role.lower() == "f/o":
      check = discord.Embed(title=f"Flight at {fltime}", description=f"You've been selected to be todays first officer on flight {flnumber}. \n\nIf you are available at {fltime} please use the tick reaction below in the next **20 minutes**, if not please choose the cross!", color=0xff0000)
      check.set_author(name="BA Staff Team", icon_url="http://logok.org/wp-content/uploads/2014/04/British-Airways-logo-ribbon-logo.png")
    elif role.lower() == "f/a":
      check = discord.Embed(title=f"Flight at {fltime}", description=f"You've been selected to be todays flight attendant on flight {flnumber}. \n\nIf you are available at {fltime} please use the tick reaction below in the next **20 minutes**, if not please choose the cross!", color=0xff0000)
      check.set_author(name="BA Staff Team", icon_url="http://logok.org/wp-content/uploads/2014/04/British-Airways-logo-ribbon-logo.png")
    
    msg = await channel.send(embed=check)
    await ctx.send(f"Waiting for {role} to confirm")
    await msg.add_reaction(str('✅'))
    await msg.add_reaction(str('❌'))

def setup(client):
    client.add_cog(otherstuff(client))
    return