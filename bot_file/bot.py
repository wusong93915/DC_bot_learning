import discord
from discord.ext import commands
import json
import os

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='[',intents = intents)

@bot.event
async def on_ready():   
    print("Bot's online")

@bot.command()
async def load(ctx,extention):
    bot.load_extension(f'cmds.{extention}')
    await ctx.send(f'Loaded {extention} done.')

@bot.command()
async def unload(ctx,extention):
    bot.unload_extension(f'cmds.{extention}')
    await ctx.send(f'Un-Loaded {extention} done.')

@bot.command()
async def reload(ctx,extention):
    bot.reload_extension(f'cmds.{extention}')
    await ctx.send(f'Re-Loaded {extention} done.')


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['token'])