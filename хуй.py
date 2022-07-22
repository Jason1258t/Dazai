import discord
from discord.ext.commands import Bot as bot0
from config import settings
import telebot

bot = bot0(command_prefix='!', intents=discord.Intents.all())

@bot.command()
async def передай(ctx, user: discord.Member, *, text):
    tg_bot = telebot.TeleBot('5315337669:AAG8SHRoX3jqT_RTmha1J8MTgHcqJA9fXVI')
    main_chat_id = -609001063
    danya_id = 47697619
    word_1 = text.split()[0].lower()
    word_2 = text.split()[1].lower()
    split_text = text.lower().split()
    ignore_words = ['что', 'чтобы', "чтоб"]
    if word_1 in ignore_words:
        del split_text[0]
        pronouns = ["он", "она", "оно"]
        print(word_2.lower())
        if word_2 in pronouns and word_1 == 'что':
            split_text[0] = 'ты'
        elif word_2 in pronouns and word_1 == 'чтобы' or word_1 == 'чтоб':
            t = f'от: {ctx.author.name}\nсообщение: {ctx.message.content}'
            tg_bot.send_message(main_chat_id, t)
            await ctx.send('я ему передал')
            return

    text = ''
    for i in split_text:
        text = f'{text} {i}'

    tg_bot.send_message(main_chat_id, text)
    await ctx.send('я ему передал')

bot.run('ODgzMjk4MzcyOTYwNzg0NDE1.GLEQcO.6g36CEUU3nFRSFT4Pj6NoYu6uwABjUrKLlY9Ls')



