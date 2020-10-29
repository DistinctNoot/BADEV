import discord
from discord.ext import commands
import platform
import datetime

class Commands(commands.Cog):



    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stats(self, ctx):
        """
        A usefull command that displays bot statistics.
        """
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))
 

        embed = discord.Embed(title=f'{self.bot.user.name} Stats', description='\uFEFF', colour=0x9E0B0B, timestamp=ctx.message.created_at)

        embed.add_field(name='Python Version:', value=pythonVersion)
        embed.add_field(name='Discord.Py Version', value=dpyVersion)
        embed.add_field(name='Total Guilds:', value=serverCount)
        embed.add_field(name='Total Users:', value=memberCount)
        embed.add_field(name='Bot Developers:', value="Mossyegghead01, DistinctNoot, AFK_Pilot, Ken the law abiding")

        embed.set_footer(text=f"BADEV {self.bot.user.name}")
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def close(self, ctx):
        await self.bot.close()

def setup(bot):
    bot.add_cog(Commands(bot))
    return