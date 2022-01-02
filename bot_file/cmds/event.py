import random
import discord
from discord.ext import commands

from core.classes import Cog_Extension

import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)



class Event(Cog_Extension):
   
    @commands.Cog.listener()
    async def on_message(self,msg):
        hi_keyword = jdata['hi']
        if msg.content in hi_keyword  and msg.author != self.bot:
            await msg.channel.send('hi hi')
        morning_keyword = jdata['morning']
        if msg.content in morning_keyword  and msg.author != self.bot:
            await msg.channel.send('早阿~')
        what_keyword = jdata['what_kw']
        if msg.content  in what_keyword and msg.author != self.bot:
            random_pic = random.choice(jdata['what'])
            pic = discord.File(random_pic)
            await msg.channel.send(file = pic)
        night_keyword = jdata['night']
        if msg.content in night_keyword and msg.author != self.bot:
            await msg.channel.send('晚安~')
        ungood_keyword = jdata['ungood']
        if ungood_keyword in msg.content and msg.author != self.bot:
            pic = discord.File('Z:\\pic\\pic\\6e1c59ee29bf45bd6a7c45650b582802.JPG')
            await msg.channel.send(file = pic)
        if '不知道' in msg.content and msg.author != self.bot:
            pic = discord.File('Z:\\pic\\pic\\FB_IMG_1591088102287.jpg')
            await msg.channel.send(file = pic)
        if '算你倒霉我就愛這樣玩' in msg.content and msg.author != self.bot:
            pic = discord.File('Z:\\pic\\pic\\UQeWZhX.jpg')
            await msg.channel.send(file = pic)
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(jdata['out/in'])
        await channel.send(f'{member}進入礦區!')
    
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(jdata['out/in'])
        await channel.send(f'{member}離開礦區')


def setup(bot):
    bot.add_cog(Event(bot))