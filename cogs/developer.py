import discord
import contextlib
import io
import sys
import subprocess
from discord.ext import commands

class developer(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  @commands.has_role("Bot developer")
  async def eval(self,ctx,*,code:str):
        try:
            if code.startswith('') and code.endswith(''):
                code = code[5:-3]
            elif code.startswith('') and code.endswith(''):
                code = code[1:-1]
            @contextlib.contextmanager
            def evaluate(stdout = None):
                old = sys.stdout
                if stdout == None:
                    sys.stdout = io.StringIO()
                yield sys.stdout
                sys.stdout = old
            
            with evaluate() as e:
                exec(code, {})

            msg = await ctx.send('Evaluating...')
            await msg.delete()
            embed = discord.Embed(title = f'Results: \n', description = e.getvalue(), color =0x9E0B0B)
            await ctx.send(embed = embed)
        except Exception as e:
            embed = discord.Embed(title = 'Ran into a error while evaluating...', color=0x9E0B0B)
            embed.add_field(name = 'Error: ', value = e)
            await ctx.send(embed = embed)

  @commands.command()
  async def run(self, ctx, *, command_string):
    output = subprocess.getoutput(command_string)
    await ctx.send(output)

def setup(client):
    client.add_cog(developer(client))
    return
