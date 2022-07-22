from discord.ext import commands
from config import settings
import sys, discord, time
from discord import utils

pref = ['daz ', '!']
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=pref, intents = intents)


@commands.has_role(889842559487189002)
@bot.command()
async def suicide(ctx):
	sys.exit()

@commands.has_role(889842559487189002)
@bot.command()
async def re(ctx):
	print('Сейчас это окно закроется')
	time.sleep(3)
	sys.exit()

@bot.event
async def on_ready( ):
	print('Дополнительная программа get_role запущена')
	print('')
	print('')



@bot.event
async def on_member_join(member):
    if member.guild.id == 883306033307615293:
        role = discord.utils.get(member.guild.roles, id=967122251545739406)
        print ('user join the servers')
        await member.add_roles(role)
        channel = await bot.fetch_channel(883306033836068936)
        await channel.send(embed=discord.Embed(description=f'@{member} добро пожаловать в секту', color=0xffc238))

    elif member.guild.id == 619203526941343754:
        role = discord.utils.get(member.guild.roles, id=777936848105242705)
        print('user join the servers')
        await member.add_roles(role)
        channel = await bot.fetch_channel(883306033836068936)
        await channel.send(embed=discord.Embed(description=f'@{member} готовь очко', color=0xffc238))

bot.run(settings['token'])
a = input()