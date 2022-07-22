import discord
from discord.ext import commands
import asyncio, time, os, sys
from random import choice, randint
bot = commands.Bot(command_prefix=['dia '])

dialog_answers = {
    'А, чего тебе?': ['Ты там живой ещё?'],
    'Да... наверное...': ['Как надумаешь умирать меня позови'],

    'Да, и с радостью поспал бы сейчас': ['Воот', 'Я знаю пару способов для хорошего и долгого сна'],
    'Что-то мне не нравится к чему ты клонишь': ['Да нормально всё', 'Так вот, для этого нужна верёвка, табуретка и...'],

    'Ля спать хочу': ['О', 'Ты живой'],
    'Только спать жутко хочу': ['Ты когда-нибудь пробовал лежать в гробу?', 'Там очень удобно, особенно если он обшит внутри', 'Ты слушаешь?', 'Эй танака', '...'],

    'Как же я сегодня устал': ['Я почему-то не удивлён'],
    'Я от переутомления глаза закрыть не могу': ['Хе-хе, чего чего, а вот такого я не ожидал', 'В принципе могу порекомендовать хорошее снотворное. Я как-то пытался с его помощью вызвать передозировку', 'В итоге проспал 15 часов на полу с пузырьком в руках'],
    'Если бы не эта история, я бы спросил название': ['Ну не хочешь и не надо'],
    'Да, я пожалуй как-нибудь сам разберусь': ['Ну удачи тебе'],

    'Чё опять прикопался': ['Как у тебя ничего не затекает так долго спать?', 'Я вот сериальчик смотрел на диване и когда на рекламе попытался встать чуть не упал'],
    'На самом деле в последнее время и правда бывают такие проблемы. Подумывал даже меньше на физ-ре спать': ['Мне вот кажется массаж может помочь', 'Я как-то думал попробовать обмотаться тротилом, чтобы…'],



}



@commands.has_permissions(administrator=True)
@bot.command()
async def re(ctx):
    print('Сейчас это окно закроется')
    time.sleep(3)
    os.startfile('dialogs_D.py')
    sys.exit()

@bot.event
async def on_command_error(ctx, error):
    pass

async def dialods(channels):
    while True:
        channel = bot.get_channel(int(choice(channels)))
        await asyncio.sleep(randint(28800, 43200))
        dialogs = [
            ['Танака', 'Танака подъём'],
            ['Слушай, танака', 'Ты же любишь спать']
        ]
        dia = choice(dialogs)
        async with channel.typing():
            for i in dia:
                await channel.send(i)
                await asyncio.sleep(1)


#969267582811140096 - танака
#883298372960784415 - дазай

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author.id == 972156642537926656 and message.content in dialog_answers:
        dia = dialog_answers[message.content]
        for i in dia:
            async with message.channel.typing():
                await asyncio.sleep(1.5)
                await message.channel.send(i)


    #if message.author.id == 883298372960784415 and message.content in dialog_dops:
    #    async with message.channel.typing():
    #        await asyncio.sleep(1)
    #        await message.channel.send(dialog_dops[message.content])


@bot.event
async def on_ready():
    print('Dazai dialogs start')
    bot.loop.create_task(dialods([883306033836068936,778568273741480029,619203527406780437]))
    #bot.loop.create_task(dialods(778568273741480029))
    #bot.loop.create_task(dialods(619203527406780437))

bot.run('ODgzMjk4MzcyOTYwNzg0NDE1.YTH5tw.Ko3_GZY5OgmYxvDBx_bUz6Uu6uM')
