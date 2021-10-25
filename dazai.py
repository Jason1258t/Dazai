import discord
import time
import random
from random import randint
import requests, json
from discord.ext import commands
from config import settings
from config import channels
from config import emojI, emojiid, month, colors
import sys, os, asyncio



bot = commands.Bot(command_prefix = settings['prefix'])
Client = discord.Client()

@bot.event
async def on_ready():
	os.startfile(r'C:\Users\user\Desktop\питон\Дазай\rsend.py')
	#os.startfile(r'C:\Users\user\Desktop\питон\Дазай\moderate.py')
	await bot.change_presence(activity=discord.Game(name="real life ебаный блять | команды: 'даз ало'"))

print('Loading...')

api_key = "ca532f2f510bb6a0360d385f4c19b384"										#Погода
base_url = "http://api.openweathermap.org/data/2.5/weather?"

@commands.has_permissions(administrator=True)
@bot.command()
async def suicide(ctx):
	sys.exit()

@commands.has_permissions(administrator=True)
@bot.command()
async def re(ctx):
	os.startfile(r'C:\Users\user\Desktop\питон\Дазай\dazai.py')
	print('Сейчас это окно закроется')
	time.sleep(5)
	sys.exit()

@bot.command()
async def пред(ctx):
	return

@bot.command()
async def преды(ctx):
	return

@bot.command()
async def добавить(ctx):
	return

@bot.command()
async def снятьпреды(ctx):
	return

@bot.command()
async def снятьпред(ctx):
	return

@bot.command()
async def кик(ctx):
	return

@bot.command()
async def погода(ctx, *, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
        async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            embed = discord.Embed(title=f"Погода в {city_name}",													#само сообщение
                              color=ctx.guild.me.top_role.color,
                              timestamp=ctx.message.created_at,)
            embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Температура(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Влажность(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Давление(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
        await channel.send(embed=embed)
    else:
    	await channel.send('Это че за мухосранск')


@commands.has_permissions(administrator=True)	
@bot.command()
async def очисти(ctx, *, text):
	limit = int(text) + 1
	await ctx.channel.purge(limit = limit)
	await ctx.send(f'Очиска сообщений завершена')
	await ctx.send('<:Nu_a_xule_nam:815966514821595207>')


@bot.command()
@commands.has_any_role('Модератор')
async def удали(ctx, user: discord.Member, *, text):
    await ctx.channel.purge(limit=int(text), check=lambda m: m.author==user)
    await ctx.send(f'Сообщения пользователя {user} удалены')

@bot.command() 
async def привет(ctx): 
	t = time.localtime() 
	current_time = time.strftime("%H", t)
	if int(current_time) < 12:		
	    await ctx.send(f'Доброе утро') 
	    time.sleep(3)
	    await ctx.send('<:kakao:808244649839165490> ')
	elif int(current_time) >= 12 and int(current_time) < 17:
		await ctx.send('Дбрый день кожанные мешки')
	elif int(current_time) >= 17:
		await ctx.send('Вечер, а значит время страдать херней')
		await ctx.send('<:crazytrollface:813440618780426300>')

@bot.event
async def on_member_join(member):
	await member.send('О, добро пожаловать кожанный мешок с говном')


@bot.command()
async def голос1(ctx, *, text):
	await ctx.channel.purge(limit = 1)
	emb = discord.Embed(title = f'{text}', description='Голосование', colour = discord.Color.purple())
	message = await ctx.send(embed = emb)
	await message.add_reaction('✅')
	await message.add_reaction('❌')

@bot.command()
async def голосование(ctx, *, text):

	name = text.split(': ')[0]
	options = text.split(': ')[1]
	emb = discord.Embed(title = f'{name}', description='Голосование', colour = 0x00ff69)
	i = 1
	for opt in options.split(';'):
		emb.add_field(name=f'{emojiid[str(i)]} : {opt}', value=':🎰:', inline=False)
		i = i+1

	mes = await ctx.send(embed = emb)

	i = 1

	for opt in options.split(';'):
		em = emojiid[str(i)]
		await mes.add_reaction(em)
		i = i+1

@bot.command()
async def роль(ctx, memID,  *, c):
	if c in colors:
		colour = colors[c]
		role = await ctx.guild.create_role(name = str(c), colour = colour)
		member = await ctx.guild.fetch_member(int((memID.split('!')[1]).split('>')[0]))

		await member.add_roles(role)
		await role.edit(hoist = True)
		count_of_role = 0
		for i in ctx.guild.roles:
			count_of_role = count_of_role + 1 
		position = count_of_role - 2
		await role.edit(position = position)
	else:
		role = await ctx.guild.create_role(name = str(c), colour = 0x00f4ff)
		member = await ctx.guild.fetch_member(int((memID.split('!')[1]).split('>')[0]))
		await member.add_roles(role)
		await role.edit(hoist = True)
		count_of_role = 0
		for i in ctx.guild.roles:
			count_of_role = count_of_role + 1 
		position = count_of_role - 2
		await role.edit(position = position)
	await ctx.send(f'Роль {c} пользователя {memID} выдана')
	await asyncio.sleep(2700)
	await role.delete()

version = '1.9.9'
@bot.command()																#список команд
async def ало(ctx):
	
	await ctx.send(f'Информация')	
	embed = discord.Embed(title=f'Версия {version}', color=0xffdd00)
	embed.add_field(name='префиксы', value='"дазай "  "дазай, "  "Дазай "  "Дазай, "  "даз "  "албанец "  "Албанец "  "албанец, "  "Албанец, "', inline=False)
	embed.add_field(name='дазай, привет', value="приветствие", inline=False)
	embed.add_field(name='дазай, как дела', value="рандомная дичь от дазая", inline=False)
	embed.add_field(name='дазай, голос *НАЗВАНИЕ*', value="простое голосование Да/Нет", inline=False)
	embed.add_field(name='дазай, голосование *НАЗВАНИЕ*: 1вариант; 2вариант; ...Nвариант', value="голосование с выбором варианта", inline=False)
	embed.add_field(name='дазай, jutsu', value="сайт", inline=False)
	embed.add_field(name='дазай, animego', value="сайт", inline=False)
	embed.add_field(name='дазай, ы', value="эмоджики", inline=False)
	embed.add_field(name='дазай, погода *НАЗВАНИЕ ГОРОДА*', value="погода в городе", inline=False)
	embed.add_field(name='дазай, очисти *КОЛ-ВО СООБЩЕНИЙ*', value='через промежуток времени очистит указанное количество сообщений', inline=False)
	embed.add_field(name='дазай, cat/dog/fox', value='отправляет рандомного котика/песеля/лису', inline=False)
	embed.add_field(name='дазай, вероятность *ТЕКСТ*', value='выдаст рандомную вероятность на указанный вами текст')
	embed.add_field(name='дазай, удали *ПОЛЬЗОВАТЕЛЬ* *кол-во*', value='удалит указанное кол-во сообщений указанного пользователя', inline=False)
	embed.add_field(name='дазай, ава', value='покажет аватарку пользователя, также можно пингануть другого пользователя', inline=False)
	embed.add_field(name='дазай, монетка', value='Выведет орел/решка', inline=False)
	embed.add_field(name='дазай, число *меньшее число* *большее число*', value='выведет случайное число', inline=False)
	embed.add_field(name='дазай, забань *Имя*', value='выведет шуточное сообщение о бане', inline=False)
	embed.add_field(name='дзаай, all', value='пинганет всех 15 раз', inline=False)
	embed.add_field(name='дзаай, сервера', value='выдаст сервера на которых есть этот бот', inline=False)
	embed.add_field(name='дзаай, серв', value='выведет информацию о сервере', inline=False)
	embed.add_field(name='дзаай, модерация', value='выдаст информацию о командах для работы с предупреждениями', inline=False)

	await ctx.send(embed=embed)

@bot.command()
async def модерация(ctx):
	emb = discord.Embed(title='Работа с предупреждениями', color=0xffdd00)
	emb.add_field(name='добавить *USER*', value='Добавит пользователя в базу предупреждений, является обязательной перед использованием остальных команд на новом пользователе', inline = False)
	emb.add_field(name='преды *USER*', value='Покажет количество предупреждений пользователя', inline = False)
	emb.add_field(name='пред *USER*', value='Добавит пользователю одно предупреждение', inline = False)
	emb.add_field(name='снятьпред *USER*', value='Снимет пользователю одно предупреждение', inline = False)
	emb.add_field(name='снятьпреды *USER*', value='Снимет все предупреждения пользователя', inline = False)
	emb.add_field(name='кик *USER*', value='Кикнет указанного пользователя. После указания пользователя можно указать причину кика. Необходимо иметь права на изгнание участников', inline=False)
	await ctx.send(embed = emb)

@bot.command()
async def патч(ctx):
	emb = discord.Embed(title=f'Патч {version}', color=0x00ffcb)
	emb.add_field(name='Информация', value = 'В этом обновлении была добавлена возможность выдавать верменные роли. Как цветные так и просто именные')
	await ctx.send(embed = emb)

@bot.command()
async def цвета(ctx):
	emb = discord.Embed(title='\u200b', color=0x00ffcb)
	emb.add_field(name='Список цветов', value = 'purple, yellow, blue, green, pink, cyan, red, orange, negr')
	await ctx.send(embed = emb)

@bot.command()																#команда "ы"
async def ы(ctx):
	emogiN = randint(0,15)
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
	elif emogiN == 15:
		await ctx.send('https://cdn.discordapp.com/attachments/778568273741480029/899711920918130698/2.jpg')

@bot.command()
async def сервера(ctx):
	servers = bot.guilds
	embed = discord.Embed(title=f'Сервера', color=0x07ff00)
	for guild in servers:
		a = guild.name
		embed.add_field(name=f'{a}', value="\u200b", inline=False)
	await ctx.send(embed=embed)
	

@bot.command()
async def серв(ctx):
	name = str(ctx.guild.name)
	owner = str(ctx.guild.owner)
	region = str(ctx.guild.region)
	afk = str(ctx.guild.afk_channel)
	members = str(ctx.guild.member_count)
	icon = str(ctx.guild.icon_url)
	creat = str(ctx.guild.created_at)
	day = creat.split('-')[2]
	creat = f'{day.split()[0]} {month[creat.split("-")[1]]} {creat.split("-")[0]} г'
	description = str(ctx.guild.description)
	emb = discord.Embed(title=f'Информация о сервере', color=0xfff700)
	emb.add_field(name='Название', value=name, inline=True)
	#emd.set_image(url=icon)
	emb.add_field(name='Создан', value=creat, inline=True)
	emb.add_field(name='\u200b', value='\u200b', inline=False)
	emb.add_field(name='Количество участников', value=members, inline=True)
	emb.add_field(name='\u200b', value='\u200b', inline=True)
	emb.add_field(name='Регион', value=region, inline=True)
	emb.add_field(name='Афк канал', value=afk, inline=False)
	await ctx.send(embed=emb)


@bot.command() 																						#команда "как дела"
async def как(ctx, *, text):
	if text == 'дела':
		number = randint(0, 11)
		print(number)
		if number == 0:
			await ctx.send(f'Выбираю веревку для профилактического самоповешанья')
			await asyncio.sleep(3)
			await ctx.send('как оказалось, в округе не так много магазинов с хозтоварами')

		elif number == 1:
			await ctx.send(f'Подыскиваю мост по-вкусу')
			await asyncio.sleep(2)
			await ctx.send('Пока что планирую сигануть с моста Золотые Ворота в Сан-Франциско')
			await asyncio.sleep(3)
			await ctx.send('Если заинтересовался, вот топ мостов https://top10reiting.com/top-10-samye-krasivye-mosty-v-mire.html')

		elif number == 2:
			await ctx.send(f'Пытаюсь купить наркотик для суицида. Есть что посоветовать?')
			await asyncio.sleep(2)
			await ctx.send(f'Но кажется в химии я не силен')
			await asyncio.sleep(2)
			await ctx.send('Вот она, хорошая мотивация подтянуть химию')

		elif number == 3:
			await ctx.send(f'Купил книгу "самоубийство для чайников", планирую сегодня почитать')
			await asyncio.sleep(3)
			await ctx.send(f'кажется там есть что-то про грибы')
			await asyncio.sleep(3)
			await ctx.send(f'Вроде вот эти грибы')
			await asyncio.sleep(3)
			await ctx.send(f'Я наконец поймал тебя радужный кот печенька')

		elif number == 4:
			await ctx.send('Не мешай')
			await asyncio.sleep(3)
			await ctx.send('Я пытаюсь подавиться печеньками насмерть')

		elif number == 5:
			await ctx.send('Нашёл в инете прикольный способ самоубийства японских самураев - харакири или сэппуку')
			await asyncio.sleep(1)
			await ctx.send('Этот способ доказывал смелость перед лицом бога смерти и чистоту своих помыслов')
			await asyncio.sleep(1)
			await ctx.send('Как красиво сказано то. Я даже вдохновился')
			await asyncio.sleep(2)
			await ctx.send('Теперь буду копить на правидьное проведение ритуала')

		elif number == 6:
			await ctx.send('Как думате какой трек лучше подходит для публичного самоубийства?')

		elif number == 7:
			await ctx.send('Я как овощь')
			await asyncio.sleep(1)
			await ctx.send('Мне нужна помощь')

		elif number == 8:
			await ctx.send('решил составить список причин жить')
			await asyncio.sleep(2)
			await ctx.send('как оказалось я живу потому что лень умирать')

		elif number == 9:
			t = time.localtime() 
			cut = time.strftime("%H", t) 
			if int(cut) < 12:
				await ctx.send('Вчера я понял, что не важно что снаружи, важно то что внутри')
				await asyncio.sleep(1)
				await ctx.send('Это я про холодильник если что')				
			elif int(cut) >= 12:
				await ctx.send('Сегодня я понял, что не важно что снаружи, важно то что внутри')
				await asyncio.sleep(1)
				await ctx.send('Это я про холодильник если что')

		elif number == 10:
			t = time.localtime() 
			cut = time.strftime("%H", t)
			if int(cut) < 18:
				await ctx.send('Решил попробовтаь сесть на диету, а то внутренний мир моего холодильника начал иссякать')
				await asyncio.sleep(2)
				await ctx.send('Но я начинаю сомневаться в том что это хорошая идея')
			elif int(cut) >= 18:
				await ctx.send('Решил попробовтаь сесть на диету, а то внутренний мир моего холодильника начал иссякать')
				await asyncio.sleep(2)
				await ctx.send('Правда к концу дня я понял, что лучше потратить 5 мин и пойти купить дошик с печньками.')

		elif number == 11:
			await ctx.send('интересный факт:')
			await asyncio.sleep(2)
			await ctx.send('Словом можно обидеть')
			await asyncio.sleep(1)
			await ctx.send('А словарем убить нахуй')



@bot.command()
async def jutsu(ctx):
	await ctx.send('https://jut.su/anime')

@bot.command()
async def animego(ctx):
	await ctx.send('https://animego.org')

@bot.command()
async def boobs(ctx):
	await ctx.send('https://rt.pornhub.com/')
	await ctx.send('<:crazytrollface:813440618780426300>')

@bot.command()
async def hent(ctx):
	await ctx.send('https://animefox.org/hentai/')
	await ctx.send('<:crazytrollface:813440618780426300>')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, данной команды не существует.**', color=0x0c0c0c))

@bot.event
async def on_message(message):
	await bot.process_commands(message)

	if message.author == bot.user: return
	textM = message.content.split()
	if textM[-1] == 'да' or textM[-1] == 'Да':
		chance = randint(0,1)
		if chance == 1:
			await message.channel.send('пизда')

	elif textM[-1] == 'пизда' or textM[-1] == 'Пизда':
		await message.channel.send('хуй')

	elif textM[-1] == 'хуй' or textM[-1] == 'Хуй':
		a = randint(1,2)
		if a == 1:
			await message.channel.send('пизда')
		elif a == 2:
			await message.channel.send('ХУЙ')

	elif textM[-1] == 'ХУЙ':
		await message.channel.send('ХУУУУУУУЙ')

	elif textM[-1] == 'нет' or textM[-1] == 'Нет':
		chance = randint(0,1)
		if chance == 1:
			await message.channel.send('пидора ответ')

	elif textM[-1] == 'антон' or textM[-1] == 'Антон':
		await message.channel.send('гандон')



	for word in message.content.split():
		if word == '@everyone':
			if message.channel.id == 632944075368300565:
				return
			await message.channel.send('нахер ты всех позвал')

	if message.author.name == 'Ashim':
		num = randint(1,10)
		if num == 2:
			em = randint(1,3)
			if em == 1:	
				await message.add_reaction('<:glider:884042375834517555>')
			elif em == 2:
				await message.add_reaction('<:glider_pink:884042174373703681>')
			elif em == 3:
				await message.add_reaction('<:glider_s9:812202670160740382>')
			elif em == 4:
				await message.add_reaction('🇦:regional_indicator_l: ')
	elif message.author.name == 'ебанько':
		num = randint(1,100)
		if num == 2:
			await message.channel.send(f'Jason, пиздуй делать обнову')


	if message.author == bot.user: return
	banwords = ['блять', 'бля', 'долбаеб', 'еблан', 'пидарас', 'пидор', 'педик', 'бляя', 'уебище']
	for word in banwords:
		a = message.content.lower()
		if word in a.split():
			if randint(1,2) == 2:
				ans = randint(0,2)
				if ans == 1:
					await message.channel.send('Какие слова знаем 😇')
				elif ans == 2:
					await message.channel.send('Матюкайтесь пореже')
				elif ans == 0:
					await message.channel.send('<:crazytrollface:813440618780426300>')
			break

	daunwords = ['даун', 'даунобот', 'дегработ', 'рободаун', 'дегенерат бот']
	for word in daunwords:
		a = message.content.lower()
		if word in a.split():
			await message.channel.send('ты '+ word +' {}'.format(message.author.nick))
			break
	b = ['блин']
	for word in b:
		a = message.content.lower()
		if word in a.split():
			await message.channel.send('Не блин, а блять')
			break

	chance = randint(1,40)
	if chance == 16:
		emogiN = randint(0,13)
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
		elif emogiN == 11:
			await message.channel.send('<:glider_pink:884042174373703681>')
		elif emogiN == 12:
			await message.channel.send('юхууу')
		elif emogiN == 13:
			await message.channel.send('🇦:regional_indicator_l: ')

	if message.content == 'https://cdn.discordapp.com/emojis/810658496977829908.gif?v=1':
		await message.channel.send('https://cdn.discordapp.com/emojis/810658496977829908.gif?v=1')


@bot.command()
async def cat(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Рандомный кiт') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def dog(ctx):
    response = requests.get('https://some-random-api.ml/img/dog') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Рандомный песель') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Рандомный лис') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def ава(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.author
    emb = discord.Embed(color=discord.Color.green())
    emb.set_image(url=member.avatar_url)
    await ctx.send(embed=emb)

@bot.command()
async def вероятность(ctx, *, text):

	message = str()
	for word in text.split():
		if word == 'я':
			message = message + ' ты'
		elif word == 'ты':
			message = message + ' я'
		elif word == 'меня':
			message = message + ' тебя'
		elif word == 'тебя':
			message = message + ' меня'
		elif word == 'нас':
			message = message + ' вас'
		elif word == 'мне':
			message = message + ' тебе'
		elif word == 'тебе':
			message = message + ' мне'
		elif word == 'нам':
			message = message + ' вам'
		else:
			message = message + f' {word}'

	chance = randint(0,100)
	answer = "Как по мне вероятность " + message + " примерно " + str(chance) + "%"
	await ctx.send(answer)

@bot.command()
async def й(ctx):
	ans = randint(1,2)
	if ans == 1:
		await ctx.send('Я тут')
	elif ans == 2:
		await ctx.send('чо надо')

@bot.command()
async def монетка(ctx):
	m = randint(1,2)
	if m == 1:
		await ctx.send('Орёл')
	else:
		await ctx.send('Решка')

@bot.command()
async def число(ctx, *, text):
	numbers = str.split(text)
	num1 = numbers[0]
	num2 = numbers[1]
	num = randint(int(num1), int(num2))
	await ctx.send(f'Число {num}')

@bot.command()
async def забань(ctx, *, text):
	await ctx.send(f'Баню пользователя "{text}"')
	time.sleep(1)
	await ctx.send('До бана:')
	time.sleep(1)
	await ctx.send('5')
	time.sleep(1)
	await ctx.send('4')
	time.sleep(1)
	await ctx.send('3')
	time.sleep(1)
	await ctx.send('2')
	time.sleep(1)
	await ctx.send('1')
	time.sleep(1)
	await ctx.send('БАААААН')
	await ctx.send('<:ban:778548119200596019><:ban:778548119200596019><:ban:778548119200596019><:ban:778548119200596019>')

@bot.command()
async def all(ctx):
	for i in range(15):
		await ctx.send('@everyone лохи')

@bot.command()
async def ебанаты(ctx):
	os.startfile(r'C:\Users\user\Desktop\питон\Дазай\piggy.py')
	os.startfile(r'C:\Users\user\Desktop\питон\Дазай\piggys.py')


print('Программа успешно запущенна')
print('Основные функции работают')
print('Возможны неполадки со стороны сложных команд')
print('Бот готов к работе, не закрывайте это окно')


bot.run(settings['token'])
a = input()