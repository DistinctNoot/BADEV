import discord
from discord.ext import commands

class others(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_member_join(self, member):
    if member.guild.id == 745144764575252520:
        var1 = discord.utils.get(member.guild.roles, id = 771868207408873492)
        channel = self.client.get_channel(745144764575252523)
        channel1 =self.client.get_channel(769367869548003379)
        channel2 = self.client.get_channel(769367361920696340)
        channel3 = self.client.get_channel(771870733235781642)
        await member.add_roles(var1)
        await channel.send(
f"""
**Hey there {member.mention}!**
**Are you a bot?:** {member.bot}
**When did you become alive?: **""" + member.created_at.strftime('%a, %#d %B %Y, %I:%M %p') +
f"""
**Status?:** {member.status}
**ID?:** {member.id}
Hmmm seems like you passed the test
to view and send messages make sure to verify in {channel3.mention} and
Make sure to check out {channel1.mention} to learn
what's good and bad here
And check out {channel2.mention} for 
awesome updates on our bot
"""
      )
    elif member.guild.id == 707183075624353952:
        var1 = discord.utils.get(member.guild.roles, id = 717681307483635722)
        channel = self.client.get_channel(727195026542559247)
        channel1 = self.client.get_channel(712712583718895687)
        channel2 = self.client.get_channel(712955612467691520)
        await channel.send(
f"""
Welcome to {member.guild.name} {member.mention}
Let's run some quick tests first.
**Are you a bot?:** {member.bot}
**When did you become alive?: **""" + member.created_at.strftime('%a, %#d %B %Y, %I:%M %p') +

f"""
**Status?:** {member.status}
**ID?:** {member.id}
Seems like you passed the test.
Make sure to check out {channel1.mention}
to stay up to date with what's happens
and check out {channel2.mention} to learn
what's good and bad here.
**British Airways to fly to serve**

"""
		)

  @commands.Cog.listener()
  async def on_member_remove(self, member):
      if member.guild.id == 745144764575252520:
        channel = self.client.get_channel(745144764575252523)
        await channel.send(
          f"""
          Oh no! seems like **{member.name}** hasn't been happy.
          We hope to see him again!
          """
        )

  @commands.Cog.listener()
  async def on_member_ban(self, member):
	  channel = await self.client.get_channel(745144764575252523)
	  await channel.send(f"{member.name} was banned.")

def setup(client):
    client.add_cog(others(client))
    return