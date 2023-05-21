import discord
from discord.ext import commands

from kirlilik_fonksiyonlari import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def cop(ctx, arg1):
    await ctx.send(cop_ayristirma(arg1))


bot.run('TOKEN')
