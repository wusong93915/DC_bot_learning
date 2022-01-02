import discord
from discord.ext import commands

from core.classes import Cog_Extension

class Main(Cog_Extension):
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.command()
    async def em(self,ctx):
        embed=discord.Embed(title="about bot", description="A bot for learning python and discord.py", color=0x2771d3)
        embed.set_author(name="五松不打虎")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def clean(self,ctx,num : int):
        await ctx.channel.purge(limit = num+1)
    
    @commands.command()
    async def clean_bulk(self,ctx):
        await ctx.channel.purge(bulk = True)

def setup(bot):
    bot.add_cog(Main(bot))