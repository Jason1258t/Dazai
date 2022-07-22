import discord
from discord.ext import commands
import requests
from datetime import datetime
import asyncio, threading

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


weather = {
    'sun': 'https://cdn.discordapp.com/attachments/973998982630109224/974910625299972116/sun_evening.gif',
    'snow': 'https://cdn.discordapp.com/attachments/973998982630109224/974910624909905950/snow.gif',
    'rain': 'https://cdn.discordapp.com/attachments/973998982630109224/974910624603709460/rain.gif',
    'clouds': {
		'небольшая облачность': 'https://cdn.discordapp.com/attachments/973998982630109224/974910624150716517/clouds.gif',
		'пасмурно':'https://cdn.discordapp.com/attachments/973998982630109224/974909912670941215/clouds-anime.gif',
		'переменная облачность': 'https://cdn.discordapp.com/attachments/973998982630109224/974909911911784458/broken_clouds.gif',
		'облачно с прояснениями': 'https://cdn.discordapp.com/attachments/973998982630109224/974909912159240212/scattered_clouds.gif'
	}
}


"""
clouds: ['облачно с прояснениями', 'пасмурно', 'переменная облачность', 'небольшая облачность']
clear: ['ясно']
rain = ['небольшой дождь', 'небольшой проливной дождь', 'дождь', 'сильный дождь', 'проливной дождь']
snow: ['снег', 'небольшой снег', 'небольшой снег с дождём']
"""



api_key = "ca532f2f510bb6a0360d385f4c19b384"										#Погода
base_url = "http://api.openweathermap.org/data/2.5/weather?"

citis = [
    'Абакан',
    'Абу-Даби',
    'Алматы',
    'Амман',
    'Амстердам',
    'Анапа',
    'Анкара',
    'Антверпен',
    'Архангельск',
    'Астана',
    'Астрахань',
    'Афины',
    'Баку',
    'Бангкок',
    'Барселона',
    'Берлин',
    'Братислава',
    'Брюгге',
    'Брюссель',
    'Бухарест',
    'Буэнос-Айрес',
    'Варна',
    'Варшава',
    'Вашингтон',
    'Вена',
    'Венеция',
    'Вильнюс',
    'Волгоград',
    'Гавана',
    'Гагра',
    'Гамбург',
    'Геленджик',
    'Гонконг',
    'Дели',
    'Днепр',
    'Дрезден',
    'Дубай',
    'Евпатория',
    'Ейск',
    'Екатеринбург',
    'Елабуга',
    'Ереван',
    'Ессентуки',
    'Женева',
    'Загреб',
    'Иерусалим',
    'Измир',
    'Йошкар-Ола',
    'Казань',
    'Каир',
    'Канны',
    'Карловы Вары',
    'Кёльн',
    'Керчь',
    'Киев',
    'Копенгаген',
    'Кронштадт',
    'Лас-Вегас',
    'Лондон',
    'Мадрид',
    'Майами-Бич',
    'Марсель',
    'Милан',
    'Минеральные Воды',
    'Минск',
    'Москва',
    'Мюнхен',
    'Набережные Челны',
    'Нарва',
    'Нижний Новгород',
    'Никосия',
    'Ницца',
    'Новосибирск',
	'Новокузнецк',
    'Нур-Султан',
    'Нью-Дели',
    'Нью-Йорк',
    'Одесса',
    'Омск',
    'Париж',
    'Пекин',
    'Пермь',
    'Прага',
    'Пятигорск',
    'Рабат',
    'Рига',
    'Рим',
    'Ростов-на-Дону',
    'Самара',
    'Санкт-Петербург',
    'Севастополь',
    'Сеул',
    'Сидней',
    'Сингапур',
    'Соль-Илецк',
    'София',
    'Сочи',
    'Стамбул',
    'Стокгольм',
    'Сухум',
    'Сан Франциско',
    'Таллин',
    'Тарту',
    'Ташкент',
    'Тбилиси',
    'Уфа',
    'Феодосия',
    'Флоренция',
    'Ханой',
    'Харьков',
    'Хельсинки',
    'Хошимин',
    'Цюрих',
    'Челябинск',
    'Штутгарт',
    'Щецин',
    'Эйлат',
    'Юрмала',
    'Ялта',
    'Тромсё',
    'Норильск',
    'Североморск',
    'Мурманск',
    'Апатиты',
    'Воркута',
    'Усть-Куйга',
    'Караул',
    'Чукочья',
    'Жилинда',
    'Прадхо-Бей',
    'Хаммерфест',
    'Хоннингсвог',
    'Гамвик',
    'Скарсвог',
    'Юрибей',
    'Порт-Алберни'
]

rain = ['небольшой дождь', 'небольшой проливной дождь', 'дождь', 'сильный дождь', 'проливной дождь', 'сильный проливной дождь']
snow = ['снег', 'небольшой снег', 'небольшой снег с дождём']
dust = ['пыльная буря']
haze = ['мгла']
thunderstorm = ['гроза с небольшим дождём', 'гроза', 'гроза с дождём']
fog = ['плотный туман']
mist = ['туман']
Drizzle = ['небольшая морось', 'морось', 'небольшой моросящий дождь', 'моросящий дождь']
Squall = ['шквальный ветер']
Smoke = ['дымка']

tumbnails = {
    'ясно': 'https://cdn.discordapp.com/attachments/973998982630109224/977260751200866304/a3d2cca96da352e7.png',
    'пасмурно': 'https://cdn.discordapp.com/attachments/973998982630109224/977260750269730886/6f9208f822832df8.png',
    'небольшая облачность': 'https://cdn.discordapp.com/attachments/973998982630109224/977260749175021628/46b36864090d55f3.png',
    'облачно с прояснениями': 'https://cdn.discordapp.com/attachments/973998982630109224/977260750051618826/d6b86f25978c2841.png',
    'переменная облачность': 'https://cdn.discordapp.com/attachments/973998982630109224/977260750512996372/8e6db87a24643c8b.png',
    'небольшой дождь': 'https://cdn.discordapp.com/attachments/973998982630109224/977260749514764318/b04592a8cb6ceb91.png',
    'небольшой проливной дождь': 'https://cdn.discordapp.com/attachments/973998982630109224/977260749514764318/b04592a8cb6ceb91.png',
    'дождь': 'https://cdn.discordapp.com/attachments/973998982630109224/977260748868825138/8f2d906366c9515e.png',
    'проливной дождь': 'https://cdn.discordapp.com/attachments/973998982630109224/977260748868825138/8f2d906366c9515e.png',
    'сильный дождь': 'https://cdn.discordapp.com/attachments/973998982630109224/977260748868825138/8f2d906366c9515e.png',
    'снег': 'https://cdn.discordapp.com/attachments/973998982630109224/977260750953385994/a99266cd9517621a.png',
    'небольшой снег': 'https://cdn.discordapp.com/attachments/973998982630109224/977260749745455125/f6484440298090a2.png',
    'небольшой снег с дождём': 'https://cdn.discordapp.com/attachments/973998982630109224/977260750714314772/2fe6b00a1e002155.png'


}
def main():
    n = 0
    from time import sleep
    while True:
        n+=1
        for city in citis:
            complete_url = base_url + "appid=" + api_key + "&q=" + city + '&lang=ru'
            response = requests.get(complete_url)
            try:
                description = response.json()["weather"][0]['description']
                main = response.json()["weather"][0]['main']
                if main == 'Rain':
                    if description not in rain:
                        print('New rain description: {0}'.format(description))
                        rain.append(description)
                elif main == 'Snow':
                    if description not in snow:
                        print('New snow description: {0}'.format(description))
                        snow.append(description)

                elif main == 'Clear': pass
                elif main == 'Clouds': pass
                elif main == 'Dust':
                    if description not in dust:
                        print('New dust description: {0}'.format(description))
                        dust.append(description)
                elif main == 'Haze':
                    if description not in haze:
                        print('New haze description: {0}'.format(description))
                        haze.append(description)
                elif main == 'Thunderstorm':
                    if description not in thunderstorm:
                        print('New thunderstorm description: {0}'.format(description))
                        thunderstorm.append(description)
                elif main == 'Fog':
                    if description not in fog:
                        print('New fog description: {0}'.format(description))
                        fog.append(description)
                elif main == 'Mist':
                    if description not in mist:
                        print('New mist description: {0}'.format(description))
                        mist.append(description)
                elif main == 'Drizzle':
                    if description not in Drizzle:
                        print('New drizzle description: {0}'.format(description))
                        Drizzle.append(description)
                elif main == 'Squall':
                    if description not in Drizzle:
                        print('New Squall description: {0}'.format(description))
                        Squall.append(description)
                elif main == 'Smoke':
                    if description not in Smoke:
                        print('New Smoke description: {0}'.format(description))
                        Smoke.append(description)

                else: print(f'{city}: {main}; {description}')

            except: pass

        print('№{0} цикл пройден {1}'.format(n, datetime.now().strftime('%H:%M')))
        #print(f'Rain: {rain}')
        #print(f'Snow: {snow}')
        #print(f'Dust: {dust}')
        #print(f'Haze: {haze}')
        #print(f'Thunderstorm: {thunderstorm}')
        #print(f'Fog: {fog}')
        #print(f'Mist: {mist}')
        sleep(600)

def supp():
    while True:
        print('supp')
        a = input('введите действие: ')
        if a == 'find whether type':
            print('Типы погоды: ')
            print('Clouds, Clear, Rain, Snow, Dust, Haze, Thunderstorm,Fog, Mist, Drizzle, Squall, Smoke')
            b = input('введите тип погоды: ')
            print('щас поищем')
            answ = 0
            for city in citis:
                complete_url = base_url + "appid=" + api_key + "&q=" + city + '&lang=ru'
                response = requests.get(complete_url)
                try:
                    description = response.json()["weather"][0]['description']
                    main = response.json()["weather"][0]['main']
                    if main == b:
                        print(f'{city}: main: {main}; description: {description}')
                        answ = 1
                        break
                except: pass

            if answ == 0: print('не получилось найти такую погоду')


#th = threading.Thread(target= main())
th2 = threading.Thread(target= supp())


if 1 == 1:
    #th.start(),
    #th.join(),
    th2.start()
    th2.join()

#loop = asyncio.new_event_loop()
#loop.create_task(main())
#loop.create_task(supp())
#loop.run_forever()











