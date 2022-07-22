import discord
from discord.ext.commands import Bot as bot0
from config import settings


bot = bot0(command_prefix='!', intents=discord.Intents.all())

api_key = "ca532f2f510bb6a0360d385f4c19b384"										#Погода
base_url = "http://api.openweathermap.org/data/2.5/forecast?"



@bot.command()
async def test(ctx, user: discord.Member = None):
    if user:
        print(user.id)
    else:
        print(ctx.author.id)

bot.run(settings['token'])
