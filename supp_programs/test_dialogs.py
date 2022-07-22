import discord
from discord.ext import commands
import asyncio, time, os, sys
from random import choice, randint

dazai = commands.Bot(command_prefix=['!'])
tanaka = commands.Bot(command_prefix=['!'])

dialog_answers = {
    1:{
        1: {'text': 'Танака', 'author': 'D'},
        2: {'text': 'Танака подъём', 'author': 'D'},
        3: {'text': 'А, чего тебе', 'author': 'T'},
        4: {'text': 'Ты там живой ещё?', 'author': 'D'},
        5: {'text': 'Да… наверное…', 'author': 'T'},
        6: {'text': 'Как надумаешь умирать маня позови', 'author': 'D'},
        7: {'text': 'Да, да как скажешь', 'author': 'T'},
        8: {'text': 'Если это всё, то я спать', 'author': 'T'}

    }
}


dazai_room = 883306033836068936

@commands.has_permissions(administrator=True)
@dazai.command()
async def re(ctx):
    print('Сейчас это окно закроется')
    time.sleep(3)
    os.startfile('dialogs_D.py')
    sys.exit()



async def sender(message, channel):
    channel = dazai.fetch_channel(channel)
    await channel.send(message)

async def dialogs(channel_id):
    await dazai.wait_until_ready()
    while True:
        channel = dazai.fetch_channel(channel_id)
        await asyncio.sleep(10)
        for replica in dialog_answers[randint(1, 1)]:
            if dialog_answers[replica]['author'] == 'D':
                dazai.loop.create_task(sender(replica['text'], channel_id))
                await asyncio.sleep(1)
            elif replica['author'] == 'T':
                tanaka.loop.create_task(sender(replica['text'], channel_id))
                await asyncio.sleep(1)


@dazai.event
async def on_ready():
    print('Dazai dialogs start')



loop = asyncio.get_event_loop()

loop.create_task(dazai.start('ODgzMjk4MzcyOTYwNzg0NDE1.YTH5tw.Ko3_GZY5OgmYxvDBx_bUz6Uu6uM'))
loop.create_task(tanaka.start('OTcyMTU2NjQyNTM3OTI2NjU2.YnU9bQ.pNw7eTMPMwg5-jqZvGLUqckxTEw'))
