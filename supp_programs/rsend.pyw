import discord
from random import randint
from discord.ext import commands
from config import settings, servers, em_list
import sys, asyncio, time



pref = ['daz ', 'rsend ']
client = commands.Bot(command_prefix = pref)

@commands.has_role(889842559487189002)
@client.command()
async def suicide(ctx):
	sys.exit()

@commands.has_role(889842559487189002)
@client.command()
async def re(ctx):
	print('Сейчас это окно закроется')
	time.sleep(3)
	sys.exit()

@client.event
async def on_ready( ):
	print('Дополнительная программа rsend запущена')


async def rem(serv, name):
	n = 0
	for i, v in enumerate(serv, 1):
		locals()[f'chan{i}'] = v
		n += 1

	while True:
		t = time.localtime()
		cut = time.strftime("%H", t)
		tim = time.strftime("%H:%M", t)
		if int(cut) < 6:
			await asyncio.sleep(1800)
			print('ночь')
		else:
			h = randint(5400, 28800)
			aw = str(h//3600) + ':' + str(h%3600//60)
			print(f'Задержка = {aw}, канал {name}. {tim}')
			await asyncio.sleep(h)
			await client.wait_until_ready()




			chan = randint(0,(n - 1))
			channelt = client.get_channel(int(serv[chan]))



			number = randint(0, 26)
			if number == 0:
				await channelt.send(f'Выбираю веревку для профилактического самоповешанья')
				time.sleep(3)
				await channelt.send('как оказалось, я не умею вязать петли')

			elif number == 1:
				await channelt.send(f'кхе-кхем')
				await asyncio.sleep(2)
				await channelt.send('У меня важное объявление')
				await asyncio.sleep(1)
				await channelt.send('@everyone Вы все гандоны')


			elif number == 2:
				await channelt.send(f'пытаюсь купить наркотик для суицида, но как оназалось это не так просто как зайти на алик. Есть что посоветовать?')
				time.sleep(2)
				await channelt.send('Вот она, хорошая мотивация подтянуть химию')

			elif number == 3:
				await channelt.send(f'Кто-нибудь знает как можно нажраться без похмелья?')


			elif number == 4:
				await channelt.send('Мне тут весело')
				time.sleep(3)
				await channelt.send('Я пытаюсь подавиться печеньками насмерть')

			elif number == 5:
				await channelt.send('Ебаать')
				await asyncio.sleep(2)
				await channelt.send('Нашел похоронное бюро со скидками до 50%')
				await asyncio.sleep(2)
				await channelt.send('Называется "Хуй нам Хуй вам"')


			elif number == 6:
				await channelt.send('Как думате какой трек лучше подходит для публичного самоубийства?')

			elif number == 7:
				await channelt.send('Я как овощь')
				time.sleep(1)
				await channelt.send('Мне нужна помощь')

			elif number == 8:
				await channelt.send('решил составить список причин жить')
				time.sleep(2)
				await channelt.send('как оказалось я живу потому что лень умирать')

			elif number == 9:
				await channelt.send('Сегодня я понял, что не важно что снаружи, важно то что внутри')
				time.sleep(1)
				await channelt.send('Это я про холодильник если что')

			elif number == 10:
				t = time.localtime()
				cut = time.strftime("%H", t)
				if int(cut) < 18:
					await channelt.send('Решил попробовтаь сесть на диету, а то внутренний мир моего холодильника начал иссякать')
					await asyncio.sleep(2)
					await channelt.send('Ноя начинаю сомневаться в том что это хорошая идея')
				elif int(cut) >= 18:
					await channelt.send('Решил попробовтаь сесть на диету, а то внутренний мир моего холодильника начал иссякать')
					await asyncio.sleep(2)
					await channelt.send('Правда к концу дня я понял, что лучше потратить 5 мин и пойти купить дошик с печньками.')

			elif number == 11:
				await channelt.send('https://cdn.discordapp.com/attachments/778568273741480029/899711920918130698/2.jpg')

			elif number == 12:
				await channelt.send('интересный факт:')
				await asyncio.sleep(2)
				await channelt.send('Словом можно обидеть')
				await asyncio.sleep(1)
				await channelt.send('А словарем убить нахуй')

			elif number == 13:
				await channelt.send(f'У вас не бывает дикого желания, чтобы вас уебало метеоритом или сбила фура?')


			elif number == 14:
				await channelt.send('Запомните! Я ваш бог, поклоняйтесь суки')

			elif number == 15:
				await channelt.send('Парни, не забывайте следить, чтобы ваши сочные попки были в безопасности')

			elif number == 16:
				await channelt.send('Скажи наркотикам нет')
				await asyncio.sleep(1)
				await channelt.send('А потом посмотри, что они тебе ответят')


			elif number in range(17, 24):
				count_in_mes = randint(1,4)
				i = 1
				mes = str()
				for i in range(count_in_mes):
					dob = em_list[randint(1,44)]
					mes = mes + dob

				await channelt.send(mes)

			elif number == 25:
				await channelt.send('Зачем привязываться к людям, если можно привязаться к люстре?')

			elif number == 26:
				await channelt.send('Ничто так хорошо не помогает развеяться, как сжигание с последующим распылением твоего праха')






client.loop.create_task(rem(servers['ghosts'], 'ghost'))
client.loop.create_task(rem(servers['shrek'], 'shrek'))

client.run(settings['token'])
a = input()
