import discord
import datetime
import asyncio
from discord.ext import commands

class moderation(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.guild_only()
  @commands.has_guild_permissions(ban_members=True)
  async def ban(self, ctx, member : discord.Member, *, reason=None):
        await ctx.guild.ban(user=member, reason=reason)
        await ctx.send(f"Banned {member.name}.")

  @commands.command()
  @commands.guild_only()
  @commands.has_guild_permissions(kick_members=True)
  async def kick(self, ctx, member : discord.Member, *, reason=None):
        await ctx.guild.kick(user=member, reason=reason)
        await ctx.send(f"Kicked {member.name}")

  @commands.command()
  @commands.guild_only()
  @commands.has_guild_permissions(ban_members=True)
  async def unban(self, ctx, id):
        member = await self.client.fetch_user(id)
        await ctx.guild.unban(user=member)
        await ctx.send(f"Unbanned {member.name}")


  @commands.command(aliases=['whois', 'userinfo'])
  async def user(self,ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author
        if (member.status == discord.Status.online):
            status = "<:Online:769418800718020619> Online"
            pass
        elif (member.status == discord.Status.offline):
            status = "<:Offline:769418801007427594> Offline"
            pass
        elif (member.status == discord.Status.idle):
            status = "<:Idle:769418800940056596> Idle"
            pass
        elif (member.status == discord.Status.dnd):
            status = "<:DND:769418800843063297> Do Not Disturb"
            pass

        roles = [role for role in member.roles[:1]]
        embed = discord.Embed(color=0x9E0B0B, timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f"{member}", icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p"))
        embed.add_field(name='Registered at:', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p'))
        embed.add_field(name='Bot?', value=f'{member.bot}')
        embed.add_field(name='Status?', value=status)
        embed.add_field(name='Top Role?', value=f'{member.top_role}')
        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles[:1]]))
        embed.set_footer(icon_url=member.avatar_url, text=f'Requested By: {ctx.author.name}')
        await ctx.send(embed=embed)

  @commands.command()
  async def say(self, ctx, *, msg):
      await ctx.message.delete()
      await asyncio.sleep(1)
      await ctx.send("{}" .format(msg))

  @commands.command()
  async def embedsay(self, ctx, *, msg):
      await asyncio.sleep(1)
      await ctx.message.delete()
      em = discord.Embed(description="{}" .format(msg),color=0x9E0B0B)
      em.set_author(name=f"{ctx.author.name}",icon_url=ctx.author.avatar_url)
      await ctx.send(embed=em)

  @commands.command()
  @commands.has_guild_permissions(manage_messages=True)
  async def embedimg(self, ctx, *, msg):
      await asyncio.sleep(1)
      em = discord.Embed(description="{}\n[Join this server for updates](https://discord.gg/v9hgwZV)" .format(msg), color=0x9E0B0B)
      attachments = ctx.message.attachments
      em.set_image(url=attachments[0].url)
      await ctx.send(embed=em)
      await ctx.message.delete()

  @commands.command()
  async def embedsayimg(self, ctx, *, msg, image=None):
      await asyncio.sleep(1)
      await ctx.message.delete()
      em = discord.Embed(description="{}" .format(msg),color=0x9E0B0B)
      image = ctx.message.attachments
      if not image in msg:
      	em.set_image(url=image[0].url)
      else:
          return
      em.set_author(name=f"{ctx.author.name}",icon_url=ctx.author.avatar_url)
      await ctx.send(embed=em)

  @commands.command()
  @commands.has_guild_permissions(manage_messages=True)
  async def embed(self, ctx, *, msg):
      await asyncio.sleep(1)
      em = discord.Embed(description="""
	  {}
	  

	  
	  [Join this server for updates](https://discord.gg/v9hgwZV)""" .format(msg), color=0x9E0B0B)
      await ctx.send(embed=em)
      await ctx.message.delete()

  @commands.command()
  async def embedd(self, ctx, msg):
	  await asyncio.sleep(1)
	  em = discord.Embed(description =msg ,color=0x9E0B0B)
	  await ctx.send(embed=em)

  @commands.command()
  async def answer(self, ctx, user : discord.User):
	  channel = await user.create_dm()
	  em = discord.Embed(title="Your application for BA developer has been accepted.",color=0x9E0B0B)
	  em.add_field(name="Your application for developer has been accepted", value="You will be given access to the [repl](https://repl.it/@BADEVTOOLS/BADEV#cogs/moderation.py) you will be given the trainee role and your code will be monitored")
	  em.set_footer(icon_url=user.avatar_url, text="British Airways Coding")
	  await channel.send(embed=em)

  @commands.command()
  async def verify(self, ctx):
	  role = discord.utils.get(ctx.guild.roles, id=769429653873360930)
	  role2 = discord.utils.get(ctx.guild.roles, id=771868207408873492)

	  if role in ctx.author.roles:
		  await ctx.send("You already verified!")
	  else:
		  await ctx.send("Welcome to the server!")
		  await ctx.author.add_roles(role)
		  await ctx.author.remove_roles(role2)


def setup(client):
    client.add_cog(moderation(client))
    return