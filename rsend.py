import discord, random, requests, json
from random import randint
from discord.ext import commands
from config import settings, servers, channels
import sys, os, asyncio, time



pref = ['daz ', 'rsend ']
client = commands.Bot(command_prefix = pref)

@commands.has_permissions(administrator=True)
@client.command()
async def suicide(ctx):
	sys.exit()

@commands.has_permissions(administrator=True)
@client.command()
async def re(ctx):
	print('Сейчас это окно закроется')
	time.sleep(5)
	sys.exit()



	

async def rem(serv, name):	
	print(serv)
	n = 0
	for i, v in enumerate(serv, 1):
		locals()[f'chan{i}'] = v
		n += 1

	while True:
		t = time.localtime() 
		cut = time.strftime("%H", t)
		if int(cut) < 6:
			await asyncio.sleep(1800)
			print('ночь')
		else:
			h = randint(1800, 18000)
			print(f'Задержка = {h}, канал {name}')
			#testchannel = client.get_channel(int(896752165899616257))
			#await testchannel.send(f'Задержка = {h}, канал {name}')
			await asyncio.sleep(h)
			await client.wait_until_ready()
			
			

							
			chan = randint(0,(n - 1))
			channelt = client.get_channel(int(serv[chan]))

				

			number = randint(0, 27)
			if number == 0:
				await channelt.send(f'Выбираю веревку для профилактического самоповешанья')
				time.sleep(3)
				await channelt.send('как оказалось, в округе не так много магазинов с хозтоварами')

			elif number == 1:
				await channelt.send(f'Думаю с моста что-ли прыгнуть')
				time.sleep(2)
				await channelt.send('Пока что планирую сигануть с моста Золотые Ворота в Сан-Франциско')
				time.sleep(3)
				await channelt.send('Если заинтересовался, вот топ мостов https://top10reiting.com/top-10-samye-krasivye-mosty-v-mire.html')

			elif number == 2:
				await channelt.send(f'пытаюсь купить наркотик для суицида, но как оназалось это не так просто как зайти на алик. Есть что посоветовать?')
				time.sleep(2)
				await channelt.send('Вот она, хорошая мотивация подтянуть химию')

			elif number == 3:
				await channelt.send(f'Купил книгу "самоубийство для чайников", планирую сегодня почитать')
				time.sleep(3)
				await channelt.send(f'кажется там есть что-то про грибы')
				time.sleep(3)
				await channelt.send(f'Вроде вот эти грибы')
				time.sleep(3)
				await channelt.send(f'Я наконец поймал тебя радужный кот печенька')

			elif number == 4:
				await channelt.send('Мне тут весело')
				time.sleep(3)
				await channelt.send('Я пытаюсь подавиться печеньками насмерть')

			elif number == 5:
				await channelt.send('Нашёл в инете прикольный способ самоубийства японских самураев - харакири или сэппуку')
				time.sleep(1)
				await channelt.send('Этот способ доказывал смелость перед лицом бога смерти и чистоту своих помыслов')
				time.sleep(1)
				await channelt.send('Как красиво сказано то. Я даже вдохновился')
				time.sleep(2)
				await channelt.send('Теперь буду копить на правильное проведение ритуала')

			elif number == 6:
				await channelt.send('https://cdn.discordapp.com/emojis/810658496977829908.gif?v=1')

			elif number == 7:
				await channelt.send('<:fck_u_cat:784100508620423219> ')

			elif number == 8:
				await channelt.send('<:che_durack:757204583138197504> ')

			elif number == 9:
				await channelt.send('<:nudanudaposhelyanaher:752475769225216061> ')

			elif number == 10:
				await channelt.send('<:ban:778548119200596019> ')

			elif number == 11:
				await channelt.send('<:lgbt:783584039075315762> ')

			elif number == 12:
				await channelt.send('<:no:783390304949764169> ')

			elif number == 13:
				await channelt.send('<:azerbajjj:769860176689233940> ')

			elif number == 14:
				await channelt.send('<:Nu_a_xule_nam:815966514821595207> ')

			elif number == 15:
				await channelt.send('<:kakao:808244649839165490>')

			elif number == 16:
				await channelt.send('https://cdn.discordapp.com/emojis/810658496977829908.gif?v=1')

			elif number == 17:
				await channelt.send('хочу печеньку')

			elif number == 18:
				await channelt.send('<:glider_pink:884042174373703681>')

			elif number == 19:
				await channelt.send('юхууу')

			elif number == 20:
				await channelt.send(':flag_al: ')

			elif number == 21:
				await channelt.send('Как думате какой трек лучше подходит для публичного самоубийства?')
				
			elif number == 22:
				await channelt.send('Я как овощь')
				time.sleep(1)
				await channelt.send('Мне нужна помощь')

			elif number == 23:
				await channelt.send('решил составить список причин жить')
				time.sleep(2)
				await channelt.send('как оказалось я живу потому что лень умирать')

			elif number == 24:
				await channelt.send('Сегодня я понял, что не важно что снаружи, важно то что внутри')
				time.sleep(1)
				await channelt.send('Это я про холодильник если что')

			elif number == 25:
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
			
			elif number == 26:
				await channelt.send('https://cdn.discordapp.com/attachments/778568273741480029/899711920918130698/2.jpg')	

			elif number == 27:
				await channelt.send('интересный факт:')
				await asyncio.sleep(2)
				await channelt.send('Словом можно обидеть')
				await asyncio.sleep(1)
				await channelt.send('А словарем убить')


@client.event
async def on_ready( ):	
	print('Дополнительная программа rsend запущена')



client.loop.create_task(rem(servers['ghosts'], 'ghost'))
client.loop.create_task(rem(servers['shrek'], 'shrek'))
client.loop.create_task(rem(servers['a9'], '9A class'))


client.run(settings['token'])
a = input()