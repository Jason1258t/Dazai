import discord
from discord.ext import commands
import asyncio, time, os, sys
from random import choice, randint
bot = commands.Bot(command_prefix=['dia '])

dialog_answers = {
    'Танака подъём': choice([['А, чего тебе?'], ['Чё опять прикопался']]),
    'Ты там живой ещё?': ['Да... наверное...'],
    'Как надумаешь умирать меня позови': ['Да, да как скажешь', 'Если это всё, то я пойду спать'],

    'Ты же любишь спать': ['Да, и с радостью поспал бы сейчас'],
    'Я знаю пару способов для хорошего и долгого сна': ['Что-то мне не нравится к чему ты клонишь'],
    'Так вот, для этого нужна верёвка, табуретка и...': ['Так блять, дазай иди в пизду', 'Я спать'],

    'Ты живой': ['Только спать жутко хочу'],

    'Я почему-то не удивлён': ['Мне сегодня вообще не давали поспать', 'Я от переутомления глаза закрыть не могу'],
    'В итоге проспал 15 часов на полу с пузырьком в руках': ['Если бы не эта история, я бы спросил название'],
    'Ну не хочешь и не надо': ['Да, я пожалуй как-нибудь сам разберусь'],

    'Я вот сериальчик смотрел на диване и когда на рекламе попытался встать чуть не упал': ['Даже не знаю', 'На самом деле в последнее время и правда бывают такие проблемы. Подумывал даже меньше на физ-ре спать'],
    'Я как-то думал попробовать обмотаться тротилом, чтобы…': ['Не продолжай', 'Хмм… Всё-таки попрошу как-нибудь Отто сделать мне массаж']
}

@commands.has_permissions(administrator=True)
@bot.command()
async def re(ctx):
    print('Сейчас это окно закроется')
    time.sleep(3)
    os.startfile('dialogs_T.py')
    sys.exit()

@bot.event
async def on_command_error(ctx, error):
    pass

async def dialods(channels):
    while True:
        channel = bot.get_channel(int(choice(channels)))
        await asyncio.sleep(randint(28800, 43200))
        dialogs = [
            ['Ля спать хочу'],
            ['Хуух', 'Как же я сегодня устал']
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
    if message.author.id == 883298372960784415 and message.content in dialog_answers:
        dia = dialog_answers[message.content]
        for i in dia:
            async with message.channel.typing():
                await asyncio.sleep(1.5)
                await message.channel.send(i)

    #if message.author.id == 969267582811140096 and message.content in dialog_dops:
    #    async with message.channel.typing():
    #        await asyncio.sleep(2)
    #        await message.channel.send(dialog_dops[message.content])


@bot.event
async def on_ready():
    print('Tanaka dialogs start')
    bot.loop.create_task(dialods(choice([883306033836068936,778568273741480029,619203527406780437])))

bot.run('OTcyMTU2NjQyNTM3OTI2NjU2.YnU9bQ.pNw7eTMPMwg5-jqZvGLUqckxTEw')
