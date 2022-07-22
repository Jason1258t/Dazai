import asyncio
import discord


phrases = {
    1: {'text': 'фраза номер 1', 'author': 'Dazai', 'answer': {'user': 'Tanaka', 'code': 2}, 'timeout': 'текст таймаута'},  # тексты фраз, тот кто ее должен писать, в answer тот кто должен ответить и номер фразы из ответа
    2: {'text': 'фраза номер 2', 'author': 'Tanaka', 'answer': {'user': 'Dazai', 'code': 1}, 'timeout': 'текст таймаута'}   # timeout, это если окажется что бот офлайн, чтобы диалог не оборвался просто так ее надо ставить
                                                                                                                            # только на фразы которые начинают диалог, сам придумаешь что поставить, если ничего то просто пусто
                                                                                                                            # кстати вместо имен ботов будут их id
}

dazai_phrase = []   #   коды стартовых фраз для дазая
tanaka_phrase = []   #   коды стартовых фраз для танаки
# .... и так далее, просто чтоб можно было как-то начинать диалог


class dialogs:
    def __init__(self, code):
        self.code = code
        self.user = phrases[code]['answer']['user']
        self.acode = phrases[code]['answer']['code']
        self.text = phrases[code]['text']
        self.author = phrases[code]['author']
        self.timeout = phrases[code]['timeout']

    @classmethod
    def sendphrase(self, code, channel_id, bot):
        channel = bot.get_channel(channel_id)
        tech_channel = bot.get_channel(983403292925239447)
        phrase = phrases[code]
        phtext = phrase['text']
        answer = phrase['answer']
        await channel.send(phtext)
        await tech_channel.send(f'channel:{channel_id};fcode:{answer["code"]};author:{answer["user"]}')
        try:
            msg = await bot.wait_for('message', check=lambda m: m.channel.id==983403292925239447 and m.author.id==answer["user"])
        except asyncio.TimeoutError:
            try:
                await channel.send(phrase['timeout'])
            except: pass

#       ЧИСТО ФУНКЦИЯ ДЛЯ ПРОВЕРКИ

def dialog():
    n = int(input('введите номер фразы: '))
    phrase = dialogs(n)
    print(f'phrase code: {phrase.code}')
    print(f'phrase text: {phrase.text}')
    print(f'phrase author: {phrase.author}')
    print(f'phrase answer user: {phrase.user}')
    print(f'phrase answer code: {phrase.acode}')