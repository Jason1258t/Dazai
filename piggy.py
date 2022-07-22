import discord
import time
import random, asyncio
from random import randint
import requests, json
from discord.ext import commands
from configP import settings

import sys
import os


bot = commands.Bot(command_prefix = 'pigi ')



print('Loading...')

@bot.command()
async def чмошник(ctx):
	user = ctx.message.author
	name = user.nick
	await ctx.send(f'{name} чмошник ебаный ты')
	await ctx.send ('https://tenor.com/view/pizdets-kot-ti-che-chto-gif-5535551')
	



@commands.has_permissions(administrator=True)
@bot.command()
async def su(ctx):
	sys.exit()


@commands.has_permissions(administrator=True)
@bot.command()
async def ебанаты(ctx):
	os.startfile(r'C:\Users\user\Desktop\питон\Дазай\piggy.py')
	await asyncio.sleep(5)
	sys.exit()


@commands.has_permissions(administrator=True)
@bot.command()
async def очисти(ctx, *, text):
	await ctx.channel.purge(limit = int(text))
	await ctx.send(f'Очиска сообщений завершена')
	await ctx.send('<:Nu_a_xule_nam:815966514821595207>')


@bot.command()
@commands.has_any_role('Модератор')
async def удали(ctx, user: discord.Member, *, text):
    await ctx.channel.purge(limit=int(text), check=lambda m: m.author==user)
    await ctx.send(f'Сообщения пользователя {user} удалены')



@bot.command()
async def ы(ctx):
	emogiN = randint(0,13)
	if emogiN == 0:
		await ctx.send('<:fck_u_cat:784100508620423219> ')
	elif emogiN == 1:
		await ctx.send('<:che_durack:757204583138197504> ')
	elif emogiN == 2:
		await ctx.send('<:nudanudaposhelyanaher:752475769225216061> ')
	elif emogiN == 3:
		await ctx.send('<:ban:778548119200596019> ')
	elif emogiN == 4:
		await ctx.send('<:lgbt:783584039075315762> ')
	elif emogiN == 5:
		await ctx.send('<:no:783390304949764169> ')
	elif emogiN == 6:
		await ctx.send('<:azerbajjj:769860176689233940> ')
	elif emogiN == 7:
		await ctx.send('Щас я ебану пивка ')
		await ctx.send('<:Nu_a_xule_nam:815966514821595207> ')
	elif emogiN == 8:
		await ctx.send('<:kakao:808244649839165490>')
	elif emogiN == 9:
		await ctx.send('хочу печеньку')
	elif emogiN == 10:
		await ctx.send('юхууу')
	elif emogiN == 11:
		await ctx.send('Когда мне уже обнову выкатят')
	elif emogiN == 12:
		await ctx.send('Жопер сасат')
	elif emogiN == 13:
		await ctx.send('https://cdn.discordapp.com/emojis/810658496977829908.gif?v=1')
	elif emogiN == 14:
		await ctx.send('https://tenor.com/view/fard-fart-among-us-gif-20809513')





@bot.command()
async def boobs(ctx):
	await ctx.send('https://rt.pornhub.com/')
	await ctx.send('<:crazytrollface:813440618780426300>')

@bot.command()
async def hent(ctx):
	await ctx.send('https://animefox.org/hentai/')
	await ctx.send('<:crazytrollface:813440618780426300>')

@bot.event
async def on_message(message):
	await bot.process_commands(message)

	if message.author == bot.user: return
	textM = message.content.split()
	if textM[-1] == 'да' or textM[-1] == 'Да':
		await message.channel.send('@everyone пизда')

	elif textM[-1] == 'пизда' or textM[-1] == 'Пизда':
		await message.channel.send('@everyone хуй')

	elif textM[-1] == 'хуй' or textM[-1] == 'Хуй' or textM[-1] == 'ХУЙ':
		a = randint(1,2)
		if a == 1:
			await message.channel.send('@everyone пизда')
		elif a == 2:
			await message.channel.send('@everyone ХУЙ')

	elif textM[-1] == 'нет' or textM[-1] == 'Нет':
		await message.channel.send('пидора ответ')

	elif textM[-1] == 'антон' or textM[-1] == 'Антон':
		await message.channel.send('гандон')




	chance = randint(1,40)
	if chance == 16:
		emogiN = randint(0,12)
		if emogiN == 0:
			await message.channel.send('<:fck_u_cat:784100508620423219> ')
		elif emogiN == 1:
			await message.channel.send('<:che_durack:757204583138197504> ')
		elif emogiN == 2:
			await message.channel.send('<:nudanudaposhelyanaher:752475769225216061> ')
		elif emogiN == 3:
			await message.channel.send('<:ban:778548119200596019> ')
		elif emogiN == 4:
			await message.channel.send('<:lgbt:783584039075315762> ')
		elif emogiN == 5:
			await message.channel.send('<:no:783390304949764169> ')
		elif emogiN == 6:
			await message.channel.send('<:azerbajjj:769860176689233940> ')
		elif emogiN == 7:
			await message.channel.send('<:Nu_a_xule_nam:815966514821595207> ')
		elif emogiN == 8:
			await message.channel.send('<:kakao:808244649839165490>')
		elif emogiN == 9:
			await message.channel.send('https://cdn.discordapp.com/emojis/810658496977829908.gif?v=1')
		elif emogiN == 10:
			await message.channel.send('хочу печеньку')
		elif emogiN == 12:
			await message.channel.send('юхууу')


@bot.command()
async def all(ctx):
	for i in range(15):
		await ctx.send('@everyone лохи')

print('Программа успешно запущенна')
print('Основные функции работают')
print('Возможны неполадки со стороны сложных команд')
print('Бот "piggy" готов к работе, не закрывайте это окно')


bot.run(settings['token'])
a = input()
