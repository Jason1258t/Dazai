import random
import telebot
import discord, time, requests, json, sqlite3, googletrans, datetime
import sys, os, asyncio
from random import randint
from discord.ext import commands
from config import settings, emojiid, month, colors, net_replic, deth_info, deth_info2, em_list, bad_translator, nicknames, return_names, day_in_month, name_month, lvls, ach_list, ach_id, ach_values, net_replic, reackt_names, ach_bonus_exp, user_colors, ignor_voice, mut_roles, caps
from googletrans import Translator
from discord import utils
import test_config
from PIL import Image, ImageDraw, ImageFont, ImageOps
from random import choice
import class_config
import remanga
from config import keyboard_en, keyboard_ru
mangaclient = remanga.Client()
mangaclient.signin_by_access_token(access_token="SnWbvGtABsfXuTpMTnVcpQocYmvieO")


def up_mp_2(user_id):
	date = datetime.datetime.now().strftime('%d.%m.%Y')
	time = datetime.datetime.now().strftime('%H:%M')
	dbdate = f'mp_stats/{user_id}_date.db'
	dbtime = f'mp_stats/{user_id}_time.db'
	dates = []
	mpdates = []
	with sqlite3.connect(dbdate) as db:
		cur = db.cursor()
		cur.execute("""CREATE TABLE IF NOT EXISTS main(number INTEGER, date TEXT, c INTEGER)""")

		cur.execute("""SELECT date FROM main""")
		d0 = cur.fetchall()
		for d in d0:
			dates.append(d[0])

		cur.execute("""SELECT c FROM main""")
		d0 = cur.fetchall()
		for d in d0:
			mpdates.append(d[0])

	times = []
	mptimes = []

	with sqlite3.connect(dbtime) as db:
		cur = db.cursor()
		cur.execute("""CREATE TABLE IF NOT EXISTS main(number INTEGER, time TEXT, c INTEGER)""")

		cur.execute("""SELECT time FROM main""")
		d0 = cur.fetchall()
		for d in d0:
			times.append(d[0])

		cur.execute("""SELECT c FROM main""")
		d0 = cur.fetchall()
		for d in d0:
			mptimes.append(d[0])

	'''         СТАТИСТИКА ПО ДАТЕ      '''

	bcg = Image.open('mp_stats/test.jpg')
	draw = ImageDraw.Draw(bcg)
	cord = []
	n = 0
	for i in range(5):
		try:
			a = mpdates[n]
			cord.append(a)
			n += 1
		except: pass
	cord2 = []
	for i in cord:
		c = 77 + (100 - i) * 2.73
		cord2.append(c)

	cordx = [[136-10, 144-10], [227-10, 235-10], [318-10, 326-10], [409-10, 417-10], [500-10, 508-10]]

	n = 0
	for i in range(4):
		try:
			draw.line(((cordx[n][0] + cordx[n][1]) / 2, cord2[n], (cordx[n + 1][0] + cordx[n + 1][1]) / 2, cord2[n + 1]), 0x7500ff, 3)
			n += 1
		except: pass

	n = 0
	for x in cordx:
		try:
			draw.ellipse((x[0], cord2[n] - 4, x[1], cord2[n] + 4), 0x7500ff, 0x7500ff)
			n += 1
		except: pass

	cordt = [[108, 25], [199, 25], [290, 25], [381, 25], [471, 25]]
	n = 0
	for i in range(5):
		try:
			date = dates[n]
			font = ImageFont.truetype("arial.ttf", size=12)
			draw.text((cordt[n][0], cordt[n][1]), text=date, font=font, fill=(0x000000))
			n += 1
		except: pass

	#bcg.save('mp_stats/finish.jpg')

	'''     СТАТИСТИКА ПО ВРЕМЕНИ       '''

	#bcg = Image.open('mp_stats/bcg.jpg')
	#draw = ImageDraw.Draw(bcg)
	cord = []
	n = 0
	for i in range(5):
		try:
			a = mptimes[n]
			cord.append(a)
			n += 1
		except:
			pass
	cord2 = []
	for i in cord:
		c = 77 + (100 - i) * 2.73
		cord2.append(c)

	cordx = [[136+10, 144+10], [227+10, 235+10], [318+10, 326+10], [409+10, 417+10], [500+10, 508+10]]

	n = 0
	for i in range(4):
		try:
			draw.line(
				((cordx[n][0] + cordx[n][1]) / 2, cord2[n], (cordx[n + 1][0] + cordx[n + 1][1]) / 2, cord2[n + 1]),
				0x00FF22, 3)
			n += 1
		except:
			pass

	n = 0
	for x in cordx:
		try:
			draw.ellipse((x[0], cord2[n] - 4, x[1], cord2[n] + 4), 0x005EFF, 0x005EFF)
			n += 1
		except:
			pass

	cordt = [[124, 363], [215, 363], [306, 363], [397, 363], [488, 363]]
	n = 0
	for i in range(5):
		try:
			date = times[n]
			font = ImageFont.truetype("arial.ttf", size=12)
			draw.text((cordt[n][0], cordt[n][1]), text=date, font=font, fill=(0x000000))
			n += 1
		except:
			pass

	bcg.save('mp_stats/finish_time.jpg')

def up_mp_1(user_id, l):
	date = datetime.datetime.now().strftime('%d.%m.%Y')
	time = datetime.datetime.now().strftime('%H:%M')
	dbdate = f'mp_stats/{user_id}_date.db'
	dbtime = f'mp_stats/{user_id}_time.db'
	mp = randint(l[0], l[1])
	#print(f'{mp} маны')
	with sqlite3.connect(dbdate) as db:
		cur = db.cursor()
		cur.execute("""CREATE TABLE IF NOT EXISTS main(number INTEGER, date TEXT, c INTEGER)""")

		cur.execute("""SELECT date FROM main WHERE date = ?""", (date,))
		if cur.fetchone() is None:

			cur.execute("""SELECT number FROM main""")
			cdate = cur.fetchall()
			# print(cdate)
			if len(cdate) == 5:
				cur.execute("""DELETE FROM main WHERE number = 1""")
				cur.execute("""UPDATE main SET number = 1 WHERE number = 2""")
				cur.execute("""UPDATE main SET number = 2 WHERE number = 3""")
				cur.execute("""UPDATE main SET number = 3 WHERE number = 4""")
				cur.execute("""UPDATE main SET number = 4 WHERE number = 5""")

			cur.execute("""SELECT number FROM main""")
			cdate = cur.fetchall()
			# print(cdate)
			num = len(cdate) + 1

			cur.execute("""INSERT INTO main(number, date, c) VALUES(?, ?, 0)""", (num, date,))

		cur.execute("""UPDATE main SET c = ? WHERE date = ?""", (mp, date,))


	with sqlite3.connect(dbtime) as db:
		cur = db.cursor()
		cur.execute("""CREATE TABLE IF NOT EXISTS main(number INTEGER, time TEXT, c INTEGER)""")

		cur.execute("""SELECT time FROM main WHERE time = ?""", (time,))
		if cur.fetchone() is None:

			cur.execute("""SELECT number FROM main""")
			ctime = cur.fetchall()
			# print(ctime)
			if len(ctime) >= 5:
				cur.execute("""DELETE FROM main WHERE number = 1""")
				cur.execute("""UPDATE main SET number = 1 WHERE number = 2""")
				cur.execute("""UPDATE main SET number = 2 WHERE number = 3""")
				cur.execute("""UPDATE main SET number = 3 WHERE number = 4""")
				cur.execute("""UPDATE main SET number = 4 WHERE number = 5""")

			cur.execute("""SELECT number FROM main""")
			ctime = cur.fetchall()
			# print(ctime)
			# print(f'длина: {len(ctime)}')
			num = len(ctime) + 1

			cur.execute("""INSERT INTO main(number, time, c) VALUES(?, ?, 0)""", (num, time,))

		cur.execute("""UPDATE main SET c = ? WHERE time = ?""", (mp, time,))

	return mp


intents = discord.Intents.all()
bot = commands.Bot(command_prefix = settings['prefix'], intents=intents)
Client = discord.Client()

async def give_ach(name, user_id, dbname, chan):
	channel = bot.get_channel(chan)
	guild = channel.guild
	#print(f'{name}  {user_id}  {dbname}  {channel}')
	get_exp = 0
	use_ach = False
	while True:
		try:
			with sqlite3.connect(dbname) as db:
				cur = db.cursor()

				cur.execute("""SELECT user_id FROM achivs WHERE user_id = ?""", (user_id,))
				if cur.fetchone() is None:
					randomC = randint(1,10)
					cur.execute("""INSERT INTO achivs(user_id, color) VALUES (?, ?)""", (user_id, randomC,))

				command = f'SELECT {name} FROM achivs WHERE user_id = ?'

				cur.execute(command, (user_id,))
				a = cur.fetchone()


				if a[0] == 0:
					use_ach = True
					if name == 'blm':
						cur.execute("""UPDATE achivs SET blm = True WHERE user_id = ?""", (user_id,))
					elif name == 'amogus':
						cur.execute("""UPDATE achivs SET amogus = True WHERE user_id = ?""", (user_id,))
					elif name == 'sus_dance':
						cur.execute("""UPDATE achivs SET sus_dance = True WHERE user_id = ?""", (user_id,))
					elif name == 'free_time':
						cur.execute("""UPDATE achivs SET free_time = True WHERE user_id = ?""", (user_id,))
					elif name == 'ucraine':
						cur.execute("""UPDATE achivs SET ucraine = True WHERE user_id = ?""", (user_id,))
					elif name == 'pupa':
						cur.execute("""UPDATE achivs SET pupa = True WHERE user_id = ?""", (user_id,))
					elif name == 'biba':
						cur.execute("""UPDATE achivs SET biba = True WHERE user_id = ?""", (user_id,))
					elif name == 'cenz':
						cur.execute("""UPDATE achivs SET cenz = True WHERE user_id = ?""", (user_id,))
					elif name == 'net_pidor':
						cur.execute("""UPDATE achivs SET net_pidor = True WHERE user_id = ?""", (user_id,))
					elif name == 'pidor_full':
						cur.execute("""UPDATE achivs SET pidor_full = True WHERE user_id = ?""", (user_id,))
					elif name == 'da_pizda':
						cur.execute("""UPDATE achivs SET da_pizda = True WHERE user_id = ?""", (user_id,))
					elif name == 'russian_game':
						cur.execute("""UPDATE achivs SET russian_game = True WHERE user_id = ?""", (user_id,))
					elif name == 'hikki':
						cur.execute("""UPDATE achivs SET hikki = True WHERE user_id = ?""", (user_id,))
					elif name == 'money_1':
						cur.execute("""UPDATE achivs SET money_1 = True WHERE user_id = ?""", (user_id,))
					elif name == 'money_2':
						cur.execute("""UPDATE achivs SET money_2 = True WHERE user_id = ?""", (user_id,))
					elif name == 'bebra':
						cur.execute("""UPDATE achivs SET bebra = True WHERE user_id = ?""", (user_id,))
					elif name == 'anton':
						cur.execute("""UPDATE achivs SET anton = True WHERE user_id = ?""", (user_id,))
					elif name == 'luck_casino':
						cur.execute("""UPDATE achivs SET luck_casino = True WHERE user_id = ?""", (user_id,))
					elif name == 'master_lose':
						cur.execute("""UPDATE achivs SET master_lose = True WHERE user_id = ?""", (user_id,))
					elif name == 'master_lose_2':
						cur.execute("""UPDATE achivs SET master_lose_2 = True WHERE user_id = ?""", (user_id,))
					elif name == 'azart_player':
						cur.execute("""UPDATE achivs SET azart_player = True WHERE user_id = ?""", (user_id,))
					elif name == 'lucky_player':
						cur.execute("""UPDATE achivs SET azart_player = True WHERE user_id = ?""", (user_id,))
					elif name == 'stupid_player':
						cur.execute("""UPDATE achivs SET stupid_player = True WHERE user_id = ?""", (user_id,))
					elif name == 'russia_vp':
						cur.execute("""UPDATE achivs SET russia_vp = True WHERE user_id = ?""", (user_id,))
					elif name == 'lh_daz':
						cur.execute("""UPDATE achivs SET lh_daz = True WHERE user_id = ?""", (user_id,))
					elif name == 'motivate':
						cur.execute("""UPDATE achivs SET motivate = True WHERE user_id = ?""", (user_id,))
					elif name == 'cookie':
						cur.execute("""UPDATE achivs SET cookie = True WHERE user_id = ?""", (user_id,))
					elif name == 'gop':
						cur.execute("""UPDATE achivs SET gop = True WHERE user_id = ?""", (user_id,))
					elif name == 'hui_na':
						cur.execute("""UPDATE achivs SET hui_na = True WHERE user_id = ?""", (user_id,))
					elif name == 'low_iq1':
						cur.execute("""UPDATE achivs SET low_iq1 = True WHERE user_id = ?""", (user_id,))
					elif name == 'low_iq2':
						cur.execute("""UPDATE achivs SET low_iq2 = True WHERE user_id = ?""", (user_id,))
					elif name == 'pasol_nahui':
						cur.execute("""UPDATE achivs SET pasol_nahui = True WHERE user_id = ?""", (user_id,))

					cur.execute("""SELECT exp FROM achivs WHERE user_id = ?""", (user_id,))
					exp = int(cur.fetchone()[0])
					exp_b = 0
					exp_b += ach_bonus_exp[name]
					exp_b += 2000
					exp += exp_b
					get_exp = exp_b
					cur.execute("""SELECT lvl FROM achivs WHERE user_id = ?""", (user_id,))
					lvl = cur.fetchone()[0]
					cur.execute("""UPDATE achivs SET exp = ? WHERE user_id = ?""", (exp, user_id,))
					for i in range(3):
						if exp >= lvls[lvl]:
							exp -= lvls[lvl]
							lvl += 1
							cur.execute("""UPDATE achivs SET lvl = ? WHERE user_id = ?""", (lvl, user_id,))
							cur.execute("""UPDATE achivs SET exp = ? WHERE user_id = ?""", (exp, user_id,))
							await channel.send(f'вы апнули уровень {lvl - 1} --> {lvl}')


		except sqlite3.OperationalError:
			print('Ошибка')
			continue

		break

	if use_ach == True:
		msg1 = await channel.send('вы нашли пасхалку')

		title = ach_id[name]
		value = ach_values[name]
		emb = discord.Embed(title='Вы получили достижение', color=0xFFFFFF)
		emb.add_field(name=title, value=value, inline=False)
		emb.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/896752165899616257/931821527748468816/depositphotos_113117000-stock-illustration-medal-award-icon.png')
		emb.set_footer(text=f'получено {get_exp} опыта')
		msg2 = await channel.send(embed = emb)

		await asyncio.sleep(5)
		await msg1.delete()
		await msg2.delete()

		user = await bot.fetch_user(user_id)
		await user.send('вы нашли пасхалку')
		await user.send(embed=emb)


async def give_exp(exp, user_id, guild, chan):
	dbname = 'database/' + guild.name + '_achivs.db'
	channel = bot.get_channel(chan)
	while True:
		try:
			with sqlite3.connect(dbname) as db:
				cur = db.cursor()
				cur.execute("""SELECT user_id FROM achivs WHERE user_id = ?""", (user_id,))
				if cur.fetchone() is None:
					randomC = randint(1, 10)
					cur.execute("""INSERT INTO achivs(user_id, color) VALUES (?,?)""", (user_id, randomC,))

				cur.execute("""SELECT exp FROM achivs WHERE user_id = ?""", (user_id,))
				exp0 = cur.fetchone()[0]
				exp1 = exp0 + exp
				cur.execute("""SELECT lvl FROM achivs WHERE user_id = ?""", (user_id,))
				lvl = cur.fetchone()[0]
				cur.execute("""UPDATE achivs SET exp = ? WHERE user_id = ?""", (exp1, user_id,))
				for i in range(5):
					if exp1 >= lvls[lvl]:
						exp1 -= lvls[lvl]
						lvl += 1
						cur.execute("""UPDATE achivs SET exp = ? WHERE user_id = ?""", (exp1, user_id,))
						cur.execute("""UPDATE achivs SET lvl = ? WHERE user_id = ?""", (lvl, user_id,))
						await channel.send(f'Вы апнули уровень: {lvl - 1} --> {lvl} ')
						dbname_2 = f'database/{guild.name}_config.db'
						dic = class_config.settings().get_range_roles(dbname_2)
						for i in dic:
							if dic[i] <= lvl:
								try:
									role = utils.get(guild.roles, id=int(i))
									user = utils.get(guild.members, id=int(user_id))
									await user.add_roles(role)
								except: pass

		except sqlite3.OperationalError:
			print(f'Ошибка выдачи опыта: \n \tdatabase: {dbname}; user_id: {user_id}')
			await asyncio.sleep(randint(1,5))
			continue

		break

async def shtraf_exp(exp, user_id, dbname, chan):
	channel = bot.get_channel(chan)
	while True:
		try:
			with sqlite3.connect(dbname) as db:
				cur = db.cursor()
				cur.execute("""SELECT user_id FROM achivs WHERE user_id = ?""", (user_id,))
				if cur.fetchone() is None:
					randomC = randint(1, 10)
					cur.execute("""INSERT INTO achivs(user_id, color) VALUES (?, ?)""", (user_id, randomC,))

				cur.execute("""SELECT exp FROM achivs WHERE user_id = ?""", (user_id,))
				exp0 = cur.fetchone()[0]
				exp1 = exp0 + exp
				cur.execute("""SELECT lvl FROM achivs WHERE user_id = ?""", (user_id,))
				lvl = cur.fetchone()[0]
				cur.execute("""UPDATE achivs SET exp = ? WHERE user_id = ?""", (exp1, user_id,))
				for i in range(5):
					if exp1 < 0:
						exp1 = lvls[lvl - 1] + exp1
						lvl -= 1
						cur.execute("""UPDATE achivs SET exp = ? WHERE user_id = ?""", (exp1, user_id,))
						cur.execute("""UPDATE achivs SET lvl = ? WHERE user_id = ?""", (lvl, user_id,))
						await channel.send(f'Вы потеряли уровень уровень: {lvl + 1} --> {lvl} ')

		except sqlite3.OperationalError:
			print('Ошибка выдачи опыта')
			await asyncio.sleep(randint(1,5))
			continue
		break

async def tm1(dbname, user, t):
	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""CREATE TABLE IF NOT EXISTS voice_time(user INTEGER, t1 INTEGER)""")

		cur.execute("""SELECT user FROM voice_time WHERE user = ?""", (user,))
		if cur.fetchone() is None:
			cur.execute("""INSERT INTO voice_time(user, t1) VALUES (?, 0)""", (user,))

		cur.execute("""UPDATE voice_time SET t1 = ? WHERE user = ?""", (t, user,))

async def tm2(dbname, user, t2):
	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""CREATE TABLE IF NOT EXISTS voice_time(user INTEGER, t1 INTEGER)""")

		cur.execute("""SELECT user FROM voice_time WHERE user = ?""", (user,))
		if cur.fetchone() is None:
			cur.execute("""INSERT INTO voice_time(user, t1) VALUES (?, 0)""", (user,))

		cur.execute("""SELECT t1 FROM voice_time WHERE user = ?""", (user,))
		t1 = cur.fetchone()[0]

		get_time = int(round(t2 - t1))
		return get_time

async def up_voice(dbname, user, t):
	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""SELECT voice FROM achivs WHERE user_id = ?""", (user,))
		vt1 = cur.fetchone()[0]
		vt1 += t
		cur.execute("""UPDATE achivs SET voice = ? WHERE user_id = ?""", (vt1, user,))

async def perm_casino(user_id, dbname, tryes):
	timer = False
	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""SELECT tryes FROM permissions_casino WHERE user_id = ?""", (user_id,))
		if cur.fetchone() is None:
			cur.execute("""INSERT INTO permissions_casino(user_id, tryes, perm) VALUES (?, 0, True)""", (user_id,))
		cur.execute("""SELECT tryes FROM permissions_casino WHERE user_id = ?""", (user_id,))
		try_2 = cur.fetchone()[0]
		try_2 += tryes
		cur.execute("""UPDATE permissions_casino SET tryes = ? WHERE user_id = ?""", (try_2, user_id))
		cur.execute("""SELECT tryes FROM permissions_casino WHERE user_id = ?""", (user_id,))
		if cur.fetchone()[0] >= 150:
			cur.execute("""UPDATE permissions_casino SET perm = False WHERE user_id = ?""", (user_id,))
			timer = True

	if timer == True:
		await asyncio.sleep(3600 * 12)
		with sqlite3.connect(dbname) as db:
			cur = db.cursor()
			cur.execute("""UPDATE permissions_casino SET perm = True WHERE user_id = ?""", (user_id))

async def get_perm(user_id, dbname):
	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""SELECT perm FROM permissions_casino WHERE user_id = ?""", (user_id,))
		if cur.fetchone() is None:
			cur.execute("""INSERT INTO permissions_casino(user_id, tryes, perm) VALUES (?, 0, True)""", (user_id,))

		cur.execute("""SELECT perm FROM permissions_casino WHERE user_id = ?""", (user_id,))

		if cur.fetchone()[0] == 1:
			return True
		else:
			return False

def true_perm(dbname):
	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""UPDATE permissions_casino SET tryes = 0, perm = True""")

def get_exp(user_id, dbname):
	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""SELECT user_id FROM achivs WHERE user_id = ?""", (user_id,))
		if cur.fetchone() is None:
			randomC = randint(1,10)
			cur.execute("""INSERT INTO achivs(user_id, color) VALUES (?, ?)""", (user_id, randomC,))
		cur.execute("""SELECT exp FROM achivs WHERE user_id = ?""", (user_id,))
		exp = cur.fetchone()[0]
	return exp

async def up_exp(user_id, dbname, exp, channel):
	channel = bot.get_channel(channel)
	while True:
		try:
			with sqlite3.connect(dbname) as db:
				cur = db.cursor()
				cur.execute("""SELECT user_id FROM achivs WHERE user_id = ?""", (user_id,))
				if cur.fetchone() is None:
					randomC = randint(1, 10)
					cur.execute("""INSERT INTO achivs(user_id, color) VALUES (?, ?)""", (user_id, randomC,))

				cur.execute("""SELECT exp FROM achivs WHERE user_id = ?""", (user_id,))
				exp0 = cur.fetchone()[0]
				exp1 = exp0 + exp
				cur.execute("""SELECT lvl FROM achivs WHERE user_id = ?""", (user_id,))
				lvl = cur.fetchone()[0]
				cur.execute("""UPDATE achivs SET exp = ? WHERE user_id = ?""", (exp1, user_id,))
				for i in range(5):
					if exp1 >= lvls[lvl]:
						exp1 -= lvls[lvl]
						lvl += 1
						cur.execute("""UPDATE achivs SET exp = ? WHERE user_id = ?""", (exp1, user_id,))
						cur.execute("""UPDATE achivs SET lvl = ? WHERE user_id = ?""", (lvl, user_id,))
						await channel.send(f'Вы апнули уровень: {lvl - 1} --> {lvl} ')

		except sqlite3.OperationalError:
			print('Ошибка выдачи опыта')
			await asyncio.sleep(randint(1,5))
			continue
		break

async def daily(guild, user, channel):
	dbname1 = 'database/' + guild.name + '.db'
	dbname2 = 'database/' + guild.name + '_achivs.db'
	with sqlite3.connect(dbname1) as db:
		cur = db.cursor()
		cur.execute("""CREATE TABLE IF NOT EXISTS mem_daily(id INTEGER, day INTEGER, month INTEGER)""")
		cur.execute("""SELECT id FROM mem_daily WHERE id = ?""", (user,))
		if cur.fetchone() is None:
			cur.execute("""INSERT INTO mem_daily(id, day, month) VALUES(?, ?, ?)""", (user, 0, 0))

		cur.execute("""SELECT day FROM mem_daily WHERE id = ?""", (user,))
		day = cur.fetchone()[0]
		cur.execute("""SELECT month FROM mem_daily WHERE id = ?""", (user,))
		month = cur.fetchone()[0]

		if day != datetime.date.today().day or month != datetime.date.today().month:
			day = datetime.date.today().day
			month = datetime.date.today().month
			await give_exp(500, user, guild, channel)
			channel = bot.get_channel(channel)
			await channel.send('Вы собрали дейлик')
			cur.execute("""UPDATE mem_daily SET day=?, month=? WHERE id = ?""",(day, month, user))


def bl():
	n = 1
	while True:
		if n == 1:
			print('Loading.')
			n+=1
		elif n == 2:
			print('Loading..')
			n+=1
		elif n == 3:
			print('Loading...')
			n=1
		os.system('cls')

@bot.event
async def on_ready():
	#for command in bot.commands:
	#	print(command)
	os.startfile(r'C:\Users\user\Desktop\питон\Дазай\supp_programs\rsend.pyw')
	os.startfile(r'C:\Users\user\Desktop\питон\Дазай\supp_programs\reaction.py')
	#os.startfile(r'C:\Users\user\Desktop\питон\Дазай\supp_programs\get_roles.py')
	os.startfile(r'C:\Users\user\Desktop\питон\Дазай\supp_programs\backupRoles.py')

	with sqlite3.connect('C:/Users/user/Desktop/питон/Дазай/database/Шрекотопия_achivs.db') as db:
		cur = db.cursor()
		cur.execute("""UPDATE permissions_casino SET tryes = 0, perm = True""")

	with sqlite3.connect('C:/Users/user/Desktop/питон/Дазай/database/Комната дазая_achivs.db') as db:
		cur = db.cursor()
		cur.execute("""UPDATE permissions_casino SET tryes = 0, perm = True""")

	with sqlite3.connect('C:/Users/user/Desktop/питон/Дазай/database/GhostSquad_achivs.db') as db:
		cur = db.cursor()
		cur.execute("""UPDATE permissions_casino SET tryes = 0, perm = True""")
	# ПРОСТАНОВКА НОВЫХ ЭМОДЗИ ДЛЯ РОЛЕЙ
	#channel = bot.get_channel(815806098027708476)  # получаем id канала
	#message = await channel.fetch_message(test_config.POST_ID_G)  # получаем id сообщения

	#for i in test_config.ROLES_G:
	#	await message.add_reaction(i)

	await bot.change_presence(activity=discord.Game(name="REAL LIFE ебаный блять | команды: 'даз ало'"))
	with sqlite3.connect('restart.db') as db:
		cursor = db.cursor()
		cursor.execute("""CREATE TABLE IF NOT EXISTS rest(id INTEGER, info INTEGER)""")
		cursor.execute("""SELECT info FROM rest WHERE id = 1""")
		a = cursor.fetchone()[0]
		if a == 1:
			channel = bot.get_channel(896752165899616257)
			await channel.send('перезагрузка завершена')
			cursor.execute("""UPDATE rest SET info = 0 WHERE id = 1""")

	os.system('cls')
	print('Программа успешно запущенна')
	print('Основные функции работают')
	print('Возможны неполадки со стороны сложных команд')
	print('Бот готов к работе, не закрывайте это окно')
	print('  ')
	print('  ')
	print('  ')

	import win10toast

	toaster = win10toast.ToastNotifier()
	toaster.show_toast("Дазай", "Бот вроде бы успешно запущен", icon_path='dazai.ico')


print('Loading...')



@commands.has_role(889842559487189002)
@bot.command()
async def suicide(ctx):
	sys.exit()

@commands.has_role(889842559487189002)
@bot.command()
async def re(ctx):
	print('Сейчас это окно закроется')
	with sqlite3.connect('restart.db') as db:
		cursor = db.cursor()
		cursor.execute("""CREATE TABLE IF NOT EXISTS rest(id INTEGER, info INTEGER)""")
		cursor.execute("""SELECT info FROM rest WHERE id = 1""")
		a = cursor.fetchone()[0]
		cursor.execute("""UPDATE rest SET info = 1 WHERE id = 1""")

	time.sleep(3)
	os.startfile(r'C:\Users\user\Desktop\питон\Дазай\dazai.py')
	sys.exit()

@commands.has_role(889842559487189002)
@bot.command()
async def qcheck(ctx):
	global question
	msg = 'каналы: '
	for i in question:
		name = bot.get_channel(int(i)).name
		msg = msg + str(name) + '; '

	await ctx.send(msg)

@commands.has_role(889842559487189002)
@bot.command()
async def qremove(ctx, channel_name):
	global question
	channels = {}
	for qid in question:
		qname = bot.get_channel(int(qid)).name
		channels[qname] = qid

	if channel_name in channels:
		await ctx.send(f'Вы действительно хотите убрать канал {channel_name}? Y/N')
		msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author and m.channel == ctx.channel)
		if msg.content == 'Y':
			question.remove(channels[channel_name])
			m = 'каналы: '
			for i in question:
				c = bot.get_channel(i).name
				m = f'{m} {c},'

			await ctx.send('по идее теперь канал удален')
			await ctx.send(m)
		else:
			await ctx.send('Отмена')
			return

	else:
		await ctx.send('Ошибка ключа')


@commands.has_permissions(administrator=True)
@bot.command()
async def add_spam_ignore(ctx):
	dbname = f'database/{ctx.guild.name}_config.db'
	id = ctx.channel.id
	answer = class_config.settings().add_spamignore(dbname, int(id))
	await ctx.send(answer)

@commands.has_permissions(administrator=True)
@bot.command()
async def remove_spam_ignore(ctx):
	dbname = f'database/{ctx.guild.name}_config.db'
	id = ctx.channel.id
	answer = class_config.settings().remove_spamignore(dbname, int(id))
	await ctx.send(answer)

@commands.has_permissions(administrator=True)
@bot.command()
async def add_word_ignore(ctx, member: discord.Member = None):
	dbname = f'database/{ctx.guild.name}_config.db'
	id = ctx.channel.id if member is None else member.id
	if member is None:
		answer = class_config.settings().add_banwords_ignore(dbname, int(id), 'chan')
	else:
		answer = class_config.settings().add_banwords_ignore(dbname, int(id), 'us')

	await ctx.send(answer)


@commands.has_permissions(administrator=True)
@bot.command()
async def remove_word_ignore(ctx, member: discord.Member = None):
	dbname = f'database/{ctx.guild.name}_config.db'
	id = ctx.channel.id if member is None else member.id
	if member is None:
		answer = class_config.settings().remove_banwords_ignore(dbname, int(id), 'chan')

	else:
		answer = class_config.settings().remove_banwords_ignore(dbname, int(id), 'us')

	await ctx.send(answer)

@commands.has_permissions(administrator=True)
@bot.command()
async def set_spam_limit(ctx, lim):
	dbname = f'database/{ctx.guild.name}_config.db'
	try:
		a = int(lim)
		if a < 0:
			await ctx.send('Кривое значение лимита')
			return
	except:
		await ctx.send('Кривое значение лимита')
		return

	answer = class_config.settings().set_spam_limit(dbname, int(lim))

	await ctx.send(answer)


@commands.has_permissions(administrator=True)
@bot.command()
async def set_spam_alert(ctx, lim):
	dbname = f'database/{ctx.guild.name}_config.db'
	try:
		a = int(lim)
		if a < 0:
			await ctx.send('Кривое значение лимита')
			return
	except:
		await ctx.send('Кривое значение лимита')
		return

	answer = class_config.settings().set_spam_alert(dbname, int(lim))

	await ctx.send(answer)


@commands.has_permissions(administrator=True)
@bot.command()
async def set_spam_text(ctx, *, text):
	dbname = f'database/{ctx.guild.name}_config.db'
	answer = class_config.settings().set_spam_text(dbname, text)

	await ctx.send(answer)

@bot.command()
async def get_spam_limit(ctx):
	dbname = f'database/{ctx.guild.name}_config.db'
	answer = class_config.settings().get_spam_limit(dbname)

	await ctx.send(f'лимит на оповещение: {answer["limit"]} лимит на предупреждение: {answer["alert"]} техт предупреждения (1): {answer["text"]}')


weather = {
	'Clear': 'https://cdn.discordapp.com/attachments/973998982630109224/974910625299972116/sun_evening.gif',
	'Snow': 'https://cdn.discordapp.com/attachments/973998982630109224/974910624909905950/snow.gif',
	'Rain': 'https://cdn.discordapp.com/attachments/973998982630109224/974910624603709460/rain.gif',
	'Drizzle': 'https://cdn.discordapp.com/attachments/973998982630109224/974910624603709460/rain.gif',
	'Thunderstorm': 'https://cdn.discordapp.com/attachments/973998982630109224/977593171695509595/thunderstorm.gif',
	'clouds': {
		'небольшая облачность': 'https://cdn.discordapp.com/attachments/973998982630109224/974910624150716517/clouds.gif',
		'пасмурно':'https://cdn.discordapp.com/attachments/973998982630109224/974909912670941215/clouds-anime.gif',
		'переменная облачность': 'https://cdn.discordapp.com/attachments/973998982630109224/974909911911784458/broken_clouds.gif',
		'облачно с прояснениями': 'https://cdn.discordapp.com/attachments/973998982630109224/974909912159240212/scattered_clouds.gif'
	},
	'Dust': 'https://cdn.discordapp.com/attachments/973998982630109224/977593170210738176/dust.gif',
	'Haze': 'https://cdn.discordapp.com/attachments/973998982630109224/977594118261833789/unknown.png',
	'Fog': 'https://cdn.discordapp.com/attachments/973998982630109224/977593170873421874/fog.gif',
	'Mist': 'https://cdn.discordapp.com/attachments/973998982630109224/977593170479185981/fog_or_mist.gif',
	'Smoke': 'https://cdn.discordapp.com/attachments/973998982630109224/977594118261833789/unknown.png',
	'Squall': 'https://cdn.discordapp.com/attachments/973998982630109224/977625843566280714/wind.gif',


}


api_key = "ca532f2f510bb6a0360d385f4c19b384"										#Погода
base_url = "http://api.openweathermap.org/data/2.5/weather?"

tumbnails = {
	'ясно': 'https://cdn.discordapp.com/attachments/973998982630109224/977260751200866304/a3d2cca96da352e7.png',
	'пасмурно': 'https://cdn.discordapp.com/attachments/973998982630109224/977260750269730886/6f9208f822832df8.png',
	'небольшая облачность': 'https://cdn.discordapp.com/attachments/973998982630109224/977260749175021628/46b36864090d55f3.png',
	'облачно с прояснениями': 'https://cdn.discordapp.com/attachments/973998982630109224/977260750051618826/d6b86f25978c2841.png',
	'переменная облачность': 'https://cdn.discordapp.com/attachments/973998982630109224/977260750512996372/8e6db87a24643c8b.png',
	'небольшой дождь': 'https://cdn.discordapp.com/attachments/973998982630109224/977260749514764318/b04592a8cb6ceb91.png',
	'небольшой проливной дождь': 'https://cdn.discordapp.com/attachments/973998982630109224/977260749514764318/b04592a8cb6ceb91.png',
	'дождь': 'https://cdn.discordapp.com/attachments/973998982630109224/977260748868825138/8f2d906366c9515e.png',
	'сильный дождь': 'https://cdn.discordapp.com/attachments/973998982630109224/977260748868825138/8f2d906366c9515e.png',
	'небольшая морось': 'https://cdn.discordapp.com/attachments/973998982630109224/977592571658395648/422bc6713aebc6e2.png',
	'морось': 'https://cdn.discordapp.com/attachments/973998982630109224/977592571658395648/422bc6713aebc6e2.png',
	'небольшой моросящий дождь': 'https://cdn.discordapp.com/attachments/973998982630109224/977592571658395648/422bc6713aebc6e2.png',
	'моросящий дождь': 'https://cdn.discordapp.com/attachments/973998982630109224/977592571658395648/422bc6713aebc6e2.png',
	'снег': 'https://cdn.discordapp.com/attachments/973998982630109224/977260750953385994/a99266cd9517621a.png',
	'небольшой снег': 'https://cdn.discordapp.com/attachments/973998982630109224/977260749745455125/f6484440298090a2.png',
	'небольшой снег с дождём': 'https://cdn.discordapp.com/attachments/973998982630109224/977260750714314772/2fe6b00a1e002155.png',
	'дымка': 'https://cdn.discordapp.com/attachments/973998982630109224/977592571905839155/5390fb9ba7c87855.png',
	'туман': 'https://cdn.discordapp.com/attachments/973998982630109224/977592571905839155/5390fb9ba7c87855.png',
	'мгла': 'https://cdn.discordapp.com/attachments/973998982630109224/977592571905839155/5390fb9ba7c87855.png',
	'плотный туман': 'https://cdn.discordapp.com/attachments/973998982630109224/977592571905839155/5390fb9ba7c87855.png',
	'гроза с небольшим дождём': 'https://cdn.discordapp.com/attachments/973998982630109224/977624148807405588/321e7390bc0cd471.png',
	'гроза с дождём': 'https://cdn.discordapp.com/attachments/973998982630109224/977624148807405588/321e7390bc0cd471.png',
	'гроза': 'https://cdn.discordapp.com/attachments/973998982630109224/977961096306630727/ec461c4e0adbe56d.png',
	'шквальный ветер': 'https://cdn.discordapp.com/attachments/973998982630109224/977592571905839155/5390fb9ba7c87855.png',

}


@bot.command()
async def погода(ctx, *, city: str):
	complete_url = base_url + "appid=" + api_key + "&q=" + city + '&lang=ru'
	response = requests.get(complete_url)
	x = response.json()
	channel = ctx.message.channel
	if x["cod"] != "404":
		async with channel.typing():
			y = x["main"]
			current_temperature = y["temp"]
			current_temperature_celsiuis = str(round(current_temperature - 273.15))
			current_pressure = round(int(y["pressure"]) * 0.75 - 10)
			current_humidity = y["humidity"]
			wind = round(int(x['wind']['speed']))
			z = x["weather"]
			weather_description = z[0]["description"]
			city_name = ''
			n = 1
			last_i = ''
			for i in city:
				if n == 1 or last_i == '-' or last_i == ' ':
					city_name = city_name + i.upper()
					n += 1
				else:
					city_name = city_name + i

				last_i = i

		embed = discord.Embed(title=f"{city_name}  {current_temperature_celsiuis}°C , {weather_description}",
							  color=discord.Color.blue(), timestamp=ctx.message.created_at)
		embed.add_field(
			name=f"<:wind:977245932947116064> Ветер: {wind} м/с \n<:humidity:977245933236547604> Влажность: {current_humidity}% \n<:preasure1:977249527515971614> Давление: {current_pressure} мм р.ст.",
			value='** **', inline=False)

		# embed.add_field(name="Погода", value=f"**{weather_description}**", inline=False)
		# embed.add_field(name="Ветер", value=f"**{wind} м/с**", inline=False)
		# embed.add_field(name="Влажность(%)", value=f"**{current_humidity}%**", inline=False)
		# embed.add_field(name="", value=f"**{current_pressure} мм р.ст.**", inline=False)

		embed.set_thumbnail(url=tumbnails[weather_description])
		embed.set_footer(text=f"Requested by {ctx.author.name}")

		if z[0]['main'] != 'Clouds':
			embed.set_image(url=weather[z[0]['main']])
		else:
			embed.set_image(url=weather['clouds'][weather_description])

		await channel.send(embed=embed)

	else:
		await channel.send('Это че за мухосранск')




@bot.command()
async def привет(ctx):
	t = time.localtime()
	current_time = time.strftime("%H", t)
	if int(current_time) < 12:
		await ctx.send(f'Доброе утро')
		time.sleep(3)
		await ctx.send('<:kakao:808244649839165490> ')
	elif int(current_time) >= 12 and int(current_time) < 17:
		await ctx.send('Добрый день кожанные мешки')
	elif int(current_time) >= 17:
		await ctx.send('Вечер, а значит время страдать херней')
		await ctx.send('<:crazytrollface:813440618780426300>')


@bot.command()
async def позови(ctx, user: discord.Member):
	if user.id == 495597472173916160:
		tg_bot = telebot.TeleBot('5315337669:AAG8SHRoX3jqT_RTmha1J8MTgHcqJA9fXVI')
		main_chat_id = -609001063
		danya_id= 476976197
		tg_bot.send_message(danya_id, 'Зайди в дискорд')
		await ctx.send('я ему написал')
	elif user.id == 883298372960784415:
		await ctx.send('Ало дазай блять')
		await ctx.send('Ой блять передоз не удался')
	elif user.id == ctx.author.id:
		await ctx.send('Ты ебанутый?')
	else:
		await ctx.send('не ебу как я его должен позвать')

@bot.command()
async def передай(ctx, user: discord.Member, *, text):
	if user.id == 495597472173916160:
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
				tg_bot.send_message(danya_id, t)
				await ctx.send('я ему передал')
				return

		text = ''
		for i in split_text:
			text = f'{text} {i}'

		tg_bot.send_message(danya_id, text)
		await ctx.send('я ему передал')
	else:
		await ctx.send('проблемка в том что я не ебу как мне его звать, если я его телегу не знаю')


@bot.command()
async def го(ctx, *, text):
	if text == 'в валорант':

		a = [
			#'<@962014488578654219>', - aeless
			'<@587619835433713694>', #- Ист
			'<@758981285347328020>', #- вдова
			'<@967046236031025183>', #- dok
			'<@306418077359144961>', #- мюсля
			'<@485708614409912341>', #- Lix
			'<@587537042968412160>', #- никалас
		]


		tg_bot = telebot.TeleBot('5315337669:AAG8SHRoX3jqT_RTmha1J8MTgHcqJA9fXVI')
		main_chat_id = -609001063
		danya_id = 476976197
		tg_bot.send_message(danya_id, 'го в валорант')
		text = '<@962014488578654219> '
		for i in range(4):
			text = text + choice(a) + ' '

		await ctx.send(text)


@bot.command()
async def голос1(ctx, *, text):
	await ctx.channel.purge(limit=1)
	emb = discord.Embed(title=f'{text}', description='Голосование', colour=ctx.author.top_role.color)

	if len(ctx.message.attachments) > 0:
		attachment = ctx.message.attachments[0]
		if attachment.filename.endswith(".jpg") or attachment.filename.endswith(
				".jpeg") or attachment.filename.endswith(".png") or attachment.filename.endswith(
				".webp") or attachment.filename.endswith(".gif"):
			image = attachment.url
			emb.set_image(url=image)
	else:
		pass

	message = await ctx.send(embed=emb)
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


@commands.has_permissions(administrator=True)
@bot.command()
async def add_ColorRole(ctx, *, name):
	role = utils.get(ctx.guild.roles, name=name)
	if role:
		answer = class_config.settings().add_ColorRole(f'database/{ctx.guild.name}_config.db', name)
		await ctx.send(answer)
	else:
		await ctx.send('нет такой роли пиздабол блять')

@commands.has_permissions(administrator=True)
@bot.command()
async def del_ColorRole(ctx, *, name):
	answer = class_config.settings().del_ColorRole(f'database/{ctx.guild.name}_config.db', name)
	await ctx.send(answer)

@commands.has_permissions(administrator=True)
@bot.command()
async def get_ColorRoles(ctx):
	answer = class_config.settings().get_ColorRoles(f'database/{ctx.guild.name}_config.db')
	await ctx.send(answer)


@bot.command()
async def цвета(ctx):
	colors = class_config.settings().get_ColorRoles(f'database/{ctx.guild.name}_config.db')
	text=''
	for i in colors:
		text = f'{text} {i},'

	if text == '':
		await ctx.send('на этом сервере еще нет подтвержденных цветных ролей')
		await ctx.send('Команды для добавления:\ndaz add_ColorRole **name**\ndaz del_ColorRole **name**\ndaz get_ColorRoles\nДля того чтобы добавить роль необходимо сначала создать роль с таким названием')
		return
	emb = discord.Embed(title='Цвета на этом сервере', color=0x00ffcb)
	emb.add_field(name='вот эта параша', value=text, inline=False)
	await ctx.send(embed = emb)


@bot.command()
async def роль(ctx, user: discord.Member, *, name):
	role_list = class_config.settings().get_ColorRoles(f'database/{ctx.guild.name}_config.db')
	if name in role_list:
		color_role = utils.get(ctx.guild.roles, name = name)
		try:
			await user.add_roles(color_role)
			await ctx.send('Дал цветную роль, а хотел в рот')
		except:
			await ctx.send(f'Пробемка с цветной ролью {name}; {role_list}')

	else:
		await ctx.send('Хочешь цвет какой-нибудь? Y/N')
		msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
		if msg.content == 'Y':
			await ctx.send('введи цвет (то что поле #)')
			msg2 = await bot.wait_for('message', check=lambda m:m.author == ctx.author and m.channel == ctx.channel)
			try:
				a = int(msg2.content, 16)
				color = a
			except:
				await ctx.send('кривое значение цвета')
				return
		else: color = None

		free_role = utils.get(ctx.guild.roles, name='undefined')

		if free_role:
			if color:
				await free_role.edit(color=color)

			await free_role.edit(name=name)

			await user.add_roles(free_role)
			await ctx.send('Дал в рот, ой роль')
			await asyncio.sleep(3600)
			await user.remove_roles(free_role)
			await free_role.edit(name='undefined')

		else:
			await ctx.send('Сорян, свободных ролей нет')


@bot.command()
async def снятьроль(ctx, user: discord.Member, *, name):
	role_list = class_config.settings().get_ColorRoles(f'database/{ctx.guild.name}_config.db')
	if name in role_list:
		role = utils.get(ctx.guild.roles, name=name)
		await user.remove_roles(role)
		await ctx.send(f'по идее снял роль {name}')
	else:
		await ctx.send('сорян, но эта роль не относится к цветным, которые может снимать любой')


@commands.has_permissions(administrator=True)
@bot.command()
async def set_rangeRole(ctx, id: int, lvl):
	role = utils.get(ctx.guild.roles, id=id)
	if role:
		dbname = f'database/{ctx.guild.name}_config.db'
		answer = class_config.settings().set_range_role(dbname, lvl, id, role.name)
		await ctx.send(answer)

	else:
		await ctx.send('проблемы с id роли, или с ботом. хз даже')


@commands.has_permissions(administrator=True)
@bot.command()
async def del_rangeRole(ctx, id: int):
	role = utils.get(ctx.guild.roles, id=id)
	if role:
		dbname = f'database/{ctx.guild.name}_config.db'
		answer = class_config.settings().del_range_role(dbname, id, role.name)
		await ctx.send(answer)
	else:
		await ctx.send('проблемы с id роли, или с ботом. хз даже')

@commands.has_permissions(administrator=True)
@bot.command()
async def ранги(ctx):
	dbname = f'database/{ctx.guild.name}_config.db'
	dic = class_config.settings().get_range_roles(dbname)

	value = ''

	lvls = []

	for i in dic:
		lvls.append(dic[i])

	lvls.sort()

	dic_copy = {}

	for i in lvls:
		for c in dic:
			if dic[c] == i: dic_copy[i] = c

	#print(dic_copy)

	for i in dic_copy:
		role = utils.get(ctx.guild.roles, id = int(dic_copy[i]))
		name = role.name
		lvl = i
		value = f'{value}{lvl}:   **{name}**\n'



	if value != '':
		emb = discord.Embed(title='Ранги на сервере', color=0x0082ff, timestamp=ctx.message.created_at, description=value)
		emb.set_image(url='https://cdn.discordapp.com/attachments/918913868330311731/986659952691146752/1580210665_tumblr_c648e56088ad90b754fe85b78f504627_21ae42b3_540.gif')
		emb.set_footer(icon_url=ctx.author.avatar_url, text=f'запросил {ctx.author.name if ctx.author.nick is None else ctx.author.nick}')
		await ctx.send(embed=emb)
	else:
		emb = discord.Embed(title='уровни еще не настроены', color=0x0082ff, timestamp=ctx.message.created_at)
		emb.set_image(url='https://cdn.discordapp.com/attachments/918913868330311731/986657617311047720/---.gif')
		await ctx.send(embed=emb)


@commands.has_permissions(administrator=True)
@bot.command()
async def update_range(ctx):
	async with ctx.channel.typing():
		dbname_1 = 'database/' + ctx.guild.name + '_achivs.db'
		dbname_2 = f'database/{ctx.guild.name}_config.db'
		dic = class_config.settings().get_range_roles(dbname_2)
		users_lvl = {}
		with sqlite3.connect(dbname_1) as db:
			cur = db.cursor()
			cur.execute(f'SELECT user_id FROM achivs')
			all_us = cur.fetchall()
			for i in all_us:
				cur.execute(f'SELECT lvl FROM achivs WHERE user_id = {int(i[0])}')
				users_lvl[i[0]] = cur.fetchone()[0]
		count = 0

		for i in users_lvl:
			try:
				user = utils.get(ctx.guild.members, id=int(i))
				lvl = users_lvl[i]
				for c in dic:
					if dic[c] <= lvl:
						role = utils.get(ctx.guild.roles, id=int(c))
						await user.add_roles(role, reason='награда ранга')
						count += 1
			except: pass

	await ctx.send('Теоретически роли должны быть обновлены')
	await ctx.send(f'выдано {count} ролей')

"""
@bot.command()
async def роль(ctx, member: discord.Member,  *, c):
	if c in colors:
		colour = colors[c]
		role = await ctx.guild.create_role(name = str(c), colour = colour)

		await member.add_roles(role)
		position = member.top_role.position
		await role.edit(position = position)
	else:
		role = await ctx.guild.create_role(name = str(c), colour = 0x00f4ff)
		await member.add_roles(role)
		await role.edit(hoist = True)
		position = member.top_role.position
		await role.edit(position = position, color = member.top_role.color)

	await ctx.send(f'Роль {c} пользователю {member} выдана')
	await asyncio.sleep(2700)
	await ctx.send(f'Роль {c} пользователя {member} удалена')
	await role.delete()
"""
version = '3.5.0'
date = '3 сентебря 2021г.'
dateUp = '17.04.2022'

#		ИФОРМАЦИОННЫЕ КОМАНДЫ

@bot.command()
async def ало(ctx):

	await ctx.send(f'Информация о самом умном создание в этом мире')
	embed = discord.Embed(title=f'Версия {version}', color=0xffdd00)
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/973998982630109224/974909913329463396/Osamu-Dazai.gif')
	embed.add_field(name='префиксы', value='"дазай "  "дазай, "  "Дазай "  "Дазай, "  "даз "  "албанец "  "Албанец "  "албанец, "  "Албанец, "', inline=False)
	embed.add_field(name='дазай, переводчик', value="информация о возможностях для перевода", inline=False)
	embed.add_field(name='дазай, погода *НАЗВАНИЕ ГОРОДА*', value="погода в городе", inline=False)
	embed.add_field(name='дазай, модерация', value='выдаст информацию о командах для работы с предупреждениями', inline=False)
	embed.add_field(name='дазай, вероятности', value='выдаст информацию о командах по типу монетка, веротность', inline=False)
	embed.add_field(name='дазай, картинки', value='выдаст информацию о командах которые выводят изображения, например ваш акатар или котика', inline=False)
	embed.add_field(name='дазай, голоса', value='выдаст информацию о командах голосования', inline=False)
	embed.add_field(name='дазай, аниме', value='выдаст информацию о командах связанных с аниме', inline=False)
	embed.add_field(name='дазай, собеседник', value='выдаст команды для недо-диалога, и разные плюшки про предсказания и вопросы', inline=False)
	embed.add_field(name='дазай, херня', value='выдаст инфу о дополнительных командах', inline=False)
	embed.add_field(name='дазай, настройки', value='Иформация о настройках для сервера', inline=False)
	embed.set_footer(text = f'создан {date}  последнее обновление {dateUp}')

	await ctx.send(embed=embed)


@bot.command()
async def херня(ctx):
	embed = discord.Embed(title='Весёлости', color=ctx.author.top_role.color)
	embed.add_field(name='дазай (без всего)', value='скажет "я тут"', inline=False)
	embed.add_field(name='дазай, ы', value="эмоджики", inline=False)
	embed.add_field(name='дазай, забань *Имя*', value='выведет ШУТОЧНОЕ, а не настоящее сообщение о бане', inline=False)
	embed.add_field(name='дзаай, all', value='пинганет всех 15 раз, но необходимо иметь права администратора', inline=False)
	embed.add_field(name='дазай, казино1', value='запустит миниигру казино без ставок', inline=False)
	embed.add_field(name='дазай, казино2', value='запустит миниигру казино со ставками, валютой является опыт на текущем уровне', inline=False)
	embed.add_field(name='дазай, статмана', value='покажет изменение вашей маны по дням и времени', inline=False)

	await ctx.send(embed=embed)

@bot.command()
async def собеседник(ctx):
	emb = discord.Embed(title='команды для диалога', color=0xffdd00)
	emb.add_field(name='дазай, привет', value="приветствие", inline=False)
	emb.add_field(name='дазай, как дела', value="рандомная дичь от дазая", inline=False)
	emb.add_field(name='дазай, истории', value="самые лучшие советы только у дазая", inline=False)
	emb.add_field(name='дазай, лайфхаки', value="рандомные истории от дазая", inline=False)
	emb.add_field(name='дазай, моя смерть', value='выдаст предсказание о твоей смерти', inline=False)
	emb.add_field(name='дазай, кто я(*ПОЛЬЗОВАТЕЛЬ*)', value="выдаст кто этот пользователь", inline=False)
	emb.add_field(name='дазай, когда *СОБЫТИЕ*', value='выдаст случайную даты проишествия события', inline=False)
	emb.add_field(name='дазай, стоит *ЧТО-ТО* или *ЧТО-ТО*', value='выберет один из предложенных вариантов разделенных ИЛИ(возможно до 5)', inline=False)
	emb.add_field(name='дазай, *ТЕКСТ* и обязатенльно в конце "?"', value='выдаст случайный ответ да/нет', inline=False)
	emb.add_field(name='дазай, напомни *часы:минуты* *текст напоминания*', value='Напомнит вам в указанное время о том, что вы должны сделать. Распостраняется только на текущий день', inline=False)
	emb.add_field(name='дазай, во что игарть',value='напишет одну из игр в которую в играете(выберите игры в канале выдачи ролей под специальным сообщением)',inline=False)
	await ctx.send(embed = emb)

@bot.command()
async def аниме(ctx):
	emb = discord.Embed(title='Анмие', color=0xffdd00)
	emb.add_field(name='дазай, jutsu', value="сайт", inline=False)
	emb.add_field(name='дазай, animego', value="сайт", inline=False)
	emb.add_field(name='дазай, арты', value="Аниме арты", inline=False)
	emb.add_field(name='дазай, раниме', value="Выдаст рандомное аниме из библиотеки от автора", inline=False)
	emb.add_field(name='дазай, обои', value='отправит аниме-обои для рабочего стола(пк)', inline=False)
	emb.add_field(name='бонус', value='если напишите ему в личку "дазай добавь аниме/обои/арт и либо url картинки либо собственно название аниме, то вашу так сказатб заявку примут на рассмотрение(просто разрабу лень самому это все искать)"', inline=False)
	await ctx.send(embed = emb)


@bot.command()
async def голоса(ctx):
	emb = discord.Embed(title='Работа с голосованиями', color=0xffdd00)
	emb.add_field(name='дазай, голос1 *НАЗВАНИЕ*', value="простое голосование Да/Нет", inline=False)
	emb.add_field(name='дазай, голосование *НАЗВАНИЕ*: 1вариант; 2вариант; ...Nвариант', value="голосование с выбором варианта", inline=False)
	await ctx.send(embed = emb)

@bot.command()
async def картинки(ctx):
	emb = discord.Embed(title='Картинки', color=0xffdd00)
	emb.add_field(name='дазай, cat/dog/fox/panda/bird', value='отправляет рандомного котика/песеля/лису/панду/птицу(ходячий обед)', inline=False)
	emb.add_field(name='дазай, ава', value='покажет аватарку пользователя, также можно пингануть другого пользователя', inline=False)
	emb.add_field(name='дазай, мэджик', value='покажет приколяху, также можно пингануть другого пользователя', inline=False)
	emb.add_field(name='дазай, арты', value='отправит арт, из библиотеки бота', inline=False)
	emb.add_field(name='дазай, мемы', value='отправит мем, из библиотеки бота', inline=False)
	emb.add_field(name='дазай, обои', value='отправит обои из библиотеки', inline=False)
	await ctx.send(embed = emb)


@bot.command()
async def вероятности(ctx):
	emb = discord.Embed(title='Вероятности', color=0xffdd00)
	emb.add_field(name='дазай, вероятность *ТЕКСТ*', value='выдаст рандомную вероятность на указанный вами текст')
	emb.add_field(name='дазай, монетка', value='Выведет орел/решка', inline=False)
	emb.add_field(name='дазай, число *меньшее число* *большее число*', value='выведет случайное число', inline=False)

	await ctx.send(embed = emb)


@bot.command()
async def модерация(ctx):
	emb = discord.Embed(title='Работа с предупреждениями', color=0xffdd00)
	emb.add_field(name='добавить *USER*', value='Добавит пользователя в базу предупреждений, является обязательной перед использованием остальных команд на новом пользователе', inline = False)
	emb.add_field(name='преды *USER*', value='Покажет количество предупреждений пользователя', inline = False)
	emb.add_field(name='пред *USER*', value='Добавит пользователю одно предупреждение', inline = False)
	emb.add_field(name='снятьпред *USER*', value='Снимет пользователю одно предупреждение', inline = False)
	emb.add_field(name='снятьпреды *USER*', value='Снимет все предупреждения пользователя', inline = False)
	emb.add_field(name='кик *USER*', value='Кикнет указанного пользователя. После указания пользователя можно указать причину кика. Необходимо иметь права на изгнание участников', inline=False)
	emb.add_field(name='дазай, очисти *КОЛ-ВО СООБЩЕНИЙ*', value='через промежуток времени очистит указанное количество сообщений', inline=False)
	emb.add_field(name='дазай, удали *ПОЛЬЗОВАТЕЛЬ* *кол-во*', value='удалит указанное кол-во сообщений указанного пользователя', inline=False)
	emb.add_field(name='дзаай, сервера', value='выдаст сервера на которых есть этот бот', inline=False)
	emb.add_field(name='дзаай, серв', value='выведет информацию о сервере', inline=False)
	emb.add_field(name='дзаай, БАН *USER* *reason*', value='забанит пользователя на сервере, поле причины не обязательно, пользователь будет автоматически разбанен через время(ознакомьтесь по команде баны)', inline=False)
	emb.add_field(name='дзаай, пардон', value='разбанит пользователя', inline=False)
	emb.add_field(name='дзаай, баны', value='выдаст количество банов у автора сообщения или того кого укажут', inline=False)
	emb.add_field(name='дзаай, бан_инфо', value='информация о таймерах банов', inline=False)
	await ctx.send(embed = emb)

@bot.command()
async def бан_инфо(ctx, user: discord.Member = None):
	if not user:
		emb = discord.Embed(title='Время банов', color=0xffdd00)
		emb.add_field(name='1 бан', value='1 час', inline=False)
		emb.add_field(name='2 бан', value='2 часа', inline=False)
		emb.add_field(name='3 бан', value='1 день', inline=False)
		emb.add_field(name='больше 3 банов', value='1 неделя', inline=False)
		emb.add_field(name='Также по этой команде если указать пользователя можно узнать его количество банов', value='как то так', inline = False)
		await ctx.send(embed=emb)
	else:
		dbname = 'database/' + str(ctx.guild.name) + '.db'
		with sqlite3.connect(dbname) as db:
			cur = db.cursor()
			cur.execute("""SELECT ban FROM bans WHERE id = ?""", (user.id,))
			await ctx.send(f'Количество банов пользователя: {cur.fetchone()[0]}')

@bot.command()
async def патч(ctx):
	emb = discord.Embed(title=f'Патч {version}', color=0x00ffcb)
	emb.add_field(name='Информация', value = 'делал что-то с выдачей ролей, кажется он теперь их возвращает тем кто перезаходит и выдает роли по умолчанию', inline=False)
	emb.set_footer(text = dateUp)
	await ctx.send(embed = emb)



@bot.command()
async def переводчик(ctx):
	emb = discord.Embed(title='Команды переаодчика', color=0xffb600)
	emb.add_field(name='дазай, переведи *метка язвка*(например ru) *text*', value='переведет текст на указанный язык и даже напишет произношение', inline=False)
	emb.add_field(name='дазай, языки', value="выведет доступные языки и их значения для перевода", inline=False)
	emb.add_field(name='дазай, язык *обозначение* или *сам язык*',value="выведет непонятный вам язык иди его обозначени в зависимости от того что ввести",inline=False)
	await ctx.send(embed = emb)

@bot.command()
async def настройки(ctx):
	emb = discord.Embed(title='Команды для настройки бота', color=ctx.author.top_role.color)
	emb.add_field(name='add_spam_ignore кажется', value='Добавит канал сообщения в список каналов где он игнорит спам', inline=False)
	emb.add_field(name='remove_spam_ignore кажется', value='удалит канал сообщения из списока каналов где он игнорит спам', inline=False)
	emb.add_field(name='set_spam_limit кажется', value='установит количество повторов, после которых он напомнит не спамить, при 0 функция отключается', inline=False)
	emb.add_field(name='set_spam_alert кажется', value='установит количество повторов, после которых он дас предупреждение, при 0 функция отключается', inline=False)
	emb.add_field(name='set_spam_text кажется', value='установит текст при повторах', inline=False)
	emb.add_field(name='get_spam_limit кажется', value='выдаст установленные настройки спама', inline=False)
	emb.add_field(name='set_join_channel', value='установит канал для приветствий(без аргументо), обязательно для работы функции', inline=False)
	emb.add_field(name='set_join_text', value='установит текст для приветствий(текст после), обязательно для работы функции', inline=False)
	emb.add_field(name='set_join_embed', value='установит настройку embed для приветствий(True или False после), не обязательно для работы функции', inline=False)
	emb.add_field(name='set_join_img', value='установит картику embed для приветствий(url картинки после), не обязательно для работы функции', inline=False)
	emb.add_field(name='set_join_role', value='установит роль, которая выдастся при заходе нового пользователя(id роли после), не обязательно для работы функции', inline=False)
	emb.add_field(name='add_word_ignore', value='добавит либо пользователя либо канал (в зависимости от того указан ли пользователь) в игнор банвордов', inline=False)
	emb.add_field(name='remove_word_ignore', value='удалит либо пользователя либо канал (в зависимости от того указан ли пользователь) из игнора банвордов', inline=False)

	await ctx.send(embed=emb)

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
	afk = str(ctx.guild.afk_channel) if ctx.guild.afk_channel is not None else 'отсутствует'
	ver = str(ctx.guild.verification_level)
	print(ver)
	if ver == 'none': ver = 'хуевый'
	elif ver == 'high': ver = 'Высокий'
	elif ver == 'low': ver = 'днищенский'
	elif ver == 'medium': ver = 'такой себе'
	elif ver == 'extreme': ver = 'фсб блять'
	members = str(ctx.guild.member_count)
	icon = str(ctx.guild.icon_url)
	creat = str(ctx.guild.created_at)
	day = creat.split('-')[2]
	creat = f'{day.split()[0]} {month[creat.split("-")[1]]} {creat.split("-")[0]} г'
	description = str(ctx.guild.description)

	member = ctx.guild.members
	channels = ctx.guild.channels
	online = 0
	offline = 0
	dnd = 0
	bots = 0
	users = 0
	text = 0
	voice = 0
	all_channels = 0
	for mem in member:
		if mem.status == discord.Status.online: online+=1
		elif mem.status == discord.Status.offline: offline+=1
		elif mem.status == discord.Status.dnd: online+=1
		elif mem.status == discord.Status.idle: dnd+=1

		if mem.bot == True: bots+=1
		else: users+=1

	for i in channels:
		if isinstance(i, discord.TextChannel):
			text+=1
			all_channels+=1
		elif isinstance(i, discord.VoiceChannel):
			voice+=1
			all_channels+=1


	emb = discord.Embed(title=f'Информация о сервере {ctx.guild.name}', color=0xfff700, timestamp=ctx.message.created_at)
	emb.set_thumbnail(url=icon)
	emb.add_field(name='Участники', value=f'<:members:967293692387938324> всего: **{members}**\n<:users:967293679301693490> людей: **{users}**\n<:bot:967293706304630814> ботов: **{bots}**', inline=True)
	emb.add_field(name=f'По статусам', value=f'<:online:967289326645968906> в сети: **{online}**\n<:dnd:967291170478755890> не актив: **{dnd}**\n<:offline:967289338633265183> не в сети: **{offline}**', inline=True)
	emb.add_field(name=f'Каналы', value=f'<:all:967305339567493162> всего: **{all_channels}**\n<:text:967305351407996978> текстовые: **{text}**\n<:voice:967305367702872084> голосовые: **{voice}**', inline=True)

	emb.add_field(name='Афк канал', value=afk, inline=True)
	emb.add_field(name='Владелец', value=f'{owner}', inline=True)
	emb.add_field(name='Дата создания', value=f'{creat}', inline=True)

	emb.add_field(name='Высшая роль', value=ctx.guild.roles[-1].name, inline=True)
	emb.add_field(name='Уровень проверки', value=ver, inline=True)

	#emb.add_field(name='Описание', value=description, inline=False)

	authorName = ctx.author.name if ctx.author.nick is None else ctx.author.nick
	emb.set_footer(text=f'Requsted be {authorName}', icon_url=bot.user.avatar_url)

	await ctx.send(embed=emb)


@bot.command()
async def объясни(ctx):
	if ctx.message.reference and (msg := ctx.message.reference.resolved) and isinstance(msg, discord.Message):
		new_text = ''
		for i in msg.content:
			if i in keyboard_en:
				new_text = new_text + keyboard_ru[keyboard_en.index(i)]
			else:
				new_text = new_text + i

		await ctx.send(new_text)

	else:
		await ctx.send("что те объяснить то? что ты даун?")

@bot.command() 																						#команда "как дела"
async def как(ctx, *, text):
	if text.lower() == 'дела' or text.lower() == 'дела?':
		user_id = ctx.author.id
		dbname = 'database/' + ctx.guild.name + '_achivs.db'
		channel = ctx.channel.id
		number = randint(0, 11)
		if number == 0:
			await ctx.send(f'Выбираю веревку для профилактического самоповешанья')
			await asyncio.sleep(3)
			await ctx.send('как оказалось, в округе не так много магазинов с хозтоварами')
			await asyncio.sleep(2)
			await ctx.send('Вообще всем советую, особенно если что-то пойдет не так, о всех проблемах можно забыть')
			await give_ach('lh_daz', user_id, dbname, channel)


		elif number == 1:
			await ctx.send(f'Пытаюсь купить наркотик для суицида. Есть что посоветовать?')
			await asyncio.sleep(2)
			await ctx.send(f'Кажется я нашел хорошую мотивацию для изучения химии')
			await give_ach('motivate', user_id, dbname, channel)


		elif number == 3:
			await ctx.send('Не мешай')
			await asyncio.sleep(3)
			await ctx.send('Я пытаюсь подавиться печеньками насмерть')


		elif number == 4:
			await ctx.send('Как думаете какой трек лучше подходит для публичного самоубийства?')

		elif number == 5:
			await ctx.send('Я как овощь')
			await asyncio.sleep(1)
			await ctx.send('Мне нужна помощь')

		elif number == 6:
			await ctx.send('решил составить список причин жить')
			await asyncio.sleep(2)
			await ctx.send('как оказалось я живу потому что лень умирать')

		elif number == 7:
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

		elif number == 8:
			t = time.localtime()
			cut = time.strftime("%H", t)
			if int(cut) < 18:
				await ctx.send('Решил попробовать сесть на диету, а то внутренний мир моего холодильника начал иссякать')
				await asyncio.sleep(2)
				await ctx.send('Но я начинаю сомневаться в том что это хорошая идея')
			elif int(cut) >= 18:
				await ctx.send('Решил попробовать сесть на диету, а то внутренний мир моего холодильника начал иссякать')
				await asyncio.sleep(2)
				await ctx.send('Правда к концу дня я понял, что лучше потратить 5 мин и пойти купить дошик с печньками.')

		elif number == 9:
			await ctx.send('интересный факт:')
			await asyncio.sleep(2)
			await ctx.send('Словом можно обидеть')
			await asyncio.sleep(1)
			await ctx.send('А словарем убить нахуй')

		elif number == 10:
			await ctx.send('Скажи наркотикам нет')
			await asyncio.sleep(1)
			await ctx.send('А потом посмотри что они тебе ответят')
			await asyncio.sleep(1)
			await ctx.send('Ес что, это намек')
			await give_ach('lh_daz', user_id, dbname, channel)

		elif number == 11:
			await ctx.send('Зачем привязываться к людям, если можно привязаться к люстре?')


@bot.command()
async def истории(ctx):
	await ctx.send('здесь пока что ничего нет')


@bot.command()
async def лайфхаки(ctx):
	num = randint(1, 4)
	if num == 1:
		await ctx.send('Интересный способ избавиться от болей в шее')
		await asyncio.sleep(1)
		await ctx.send('Вообще он больше профилактический')
		await asyncio.sleep(1)
		await ctx.send('Для этого надо 2 раза в неделю (а лучше перед кр) проводить профилактическое самоповешанье')

	elif num == 2:
		await ctx.send('От болей в голове очень хорошо помогает гильотина')

	elif num == 3:
		await ctx.send('Недавно узнал класную технику массажа')
		await asyncio.sleep(1)
		await ctx.send('Для нее надо обмотаться троитилом. Это очень расслабляет и помогает избавиться от проблем')

	elif num == 4:
		await ctx.send('есть один класный бюджетный способ стрижки, который заставит многих обратить на вас внимание')
		await asyncio.sleep(1)
		await ctx.send('Для него нужен бензин и зажигалка')
		await asyncio.sleep(1)
		await ctx.send('Больше всего удивятся врачи с психологами')


@bot.command()
async def вернись(ctx, *, text):
	if text == 'в мафию':
		await ctx.send('pasol nahui')
		await give_ach('pasol_nahui', ctx.author.id, f'database/{ctx.guild.name}_achivs.db', ctx.channel.id)


@bot.command()
async def закажи(ctx, *, text):
	if text == 'гроб':
		colors = ['желтого цвета', 'красного цвета', 'синего цвета', 'розового цвета', 'цвета помоев', 'под цвет надгробия', 'цвета протухших носков']
		await ctx.send(f'заказываю на твое имя гроб {colors[randint(0, 6)]}')


@bot.command()
async def призови(ctx, *, text = None):
	alf0 = 'qwertyuiopasdfghjklzxcvbnm'
	alf1 = list(alf0)
	sog = list('wrtpsdfghjklzxcvbnm')
	gl = list('qeyuioa')
	alltext = ''
	strofs = randint(4, 8)
	colors = [0x5618FF, 0x066A24, 0x7500ff, discord.Color.dark_red(), ctx.author.top_role.color]
	embed = discord.Embed(title='заклинание призыва', color=choice(colors), timestamp=ctx.message.created_at)
	for i in range(strofs):
		count = randint(3, 6)
		allstr = ''
		for word in range(count):
			repgl = 0
			repsogl = 0
			sym = randint(2, 6)
			last_symbol = ''
			allword = ''
			for n in range(sym):
				s = alf1[randint(0, len(alf1)-1)]
				if last_symbol in sog and s in sog: repsogl += 1
				elif last_symbol in gl and s in gl: repgl += 1
				else:
					repgl = repsogl = 0

				if repsogl >= 2 or repgl >= 2:
					while repsogl >= 2 or repgl >= 2:
						#print('повторный выбор')
						s = choice(alf1)
						if last_symbol in sog and s in sog:
							repsogl += 1
						elif last_symbol in gl and s in gl:
							repgl += 1
						else:
							repgl = repsogl = 0
				last_symbol = s
				allword = f'{allword}{s}'
				#print(allword)

			allstr = f'{allstr} {allword}'
			#print(allstr)

		alltext = alltext + allstr + '\n'

	embed.add_field(name=alltext, value='\u200b', inline=False)
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/973998982630109224/974916403612237865/unknown.png')
	author = ctx.author.name if ctx.author.nick is None else ctx.author.nick
	embed.set_footer(text=f'Заказчик {author}')
	pr = text if text != None else ''
	await ctx.send(f'призываю {pr}')
	#print(alltext)
	await ctx.send(embed=embed)


	if text == 'ману':
		global users_mp
		try:
			mp = users_mp[ctx.author.id]
			if mp < 90:
				users_mp[ctx.author.id] += 10
			else:
				users_mp[ctx.author.id] = 1
		except KeyError:
			users_mp[ctx.author.id] = randint(35, 100)





@commands.has_permissions(administrator=True)
@bot.command()
async def зарплата(ctx, c, user: discord.Member):
	user_id = user.id
	dbname = 'database/' + ctx.guild.name + '_achivs.db'
	chan = ctx.channel.id
	await give_exp(int(c), user_id, ctx.guild, chan)

	await ctx.send(f'Начислено {c} опыта пользователю {user}')

@commands.has_permissions(administrator=True)
@bot.command()
async def штраф(ctx, c, user: discord.Member):
	user_id = user.id
	dbname = 'database/' + ctx.guild.name + '_achivs.db'
	chan = ctx.channel.id
	ci = -(int(c))
	await shtraf_exp(ci, user_id, dbname, chan)

	await ctx.send(f'Списано {c} опыта у пользователю {user}')

@bot.command()
async def сдохни(ctx):
	v = randint(1, 3)
	if v == 1:
		await ctx.send('Заманчивое предложение')

	elif v == 2:
		await ctx.send('Я то и не против, вот только разраб воскресит и пизды даст')

	elif v == 3:
		await ctx.send ('ок')


@bot.command()
async def jutsu(ctx):
	await ctx.send('https://jut.su/anime')

@bot.command()
async def animego(ctx):
	await ctx.send('https://animego.org')


#		МОДЕРАЦИЯ

@commands.has_permissions(administrator=True)
@bot.command()
async def очисти(ctx, limit):
	limit = int(limit) + 1
	await ctx.channel.purge(limit = limit)
	await ctx.send(f'Очищено {limit-1} сообщений')
	await ctx.send('<:Nu_a_xule_nam:815966514821595207>')


@bot.command()
@commands.has_any_role('Модератор')
async def удали(ctx, user: discord.Member, *, text):
	await ctx.channel.purge(limit=int(text), check=lambda m: m.author==user)
	await ctx.send(f'Сообщения пользователя {user} удалены')


@commands.has_permissions(administrator=True)
@bot.command()
async def добюз(ctx, user):
	dbname = 'database/' + str(ctx.guild.name) + '.db'
	mem = (user.split('!')[1]).split('>')[0]
	nameid = await ctx.guild.fetch_member(mem)
	name = nameid.name
	#print(name)
	i = 0
	with sqlite3.connect(dbname) as db:
		cursor = db.cursor()
		cursor.execute("""INSERT INTO members (id, name, warn) VALUES(?, ?, ?)""", (mem, name, i))

	await ctx.send(f'пользователь {user} добавлен в список предупреждений')


async def warning(chan: int, dbname: str, user_id: int, user_name: str):
	channel = bot.get_channel(chan)
	with sqlite3.connect(dbname) as db:
		cursor = db.cursor()
		cursor.execute("""SELECT warn FROM members WHERE id = ? """, (user_id,))
		if cursor.fetchone() == None:
			i = 0
			cursor.execute("""INSERT INTO members (id, name, warn) VALUES(?, ?, ?)""", (user_id, user_name, i))

		cursor.execute("""SELECT warn FROM members WHERE id = ? """, (user_id,))
		i = cursor.fetchone()
		i = i[0]
		i = int(i) + 1
		#print(i)
		cursor.execute("""UPDATE members SET warn = ? WHERE id = ? """, (i, user_id,))
	await channel.send(f'пользователь {user_name}, теперь имеет {i} предупреждений')
	return i


@commands.has_permissions(administrator=True)
@bot.command()
async def пред(ctx, user: discord.Member):
	dbname =  'database/' + str(ctx.guild.name) + '.db'
	user_id = user.id
	name = user.name
	chan = ctx.channel.id
	#print(dbname)

	preds = await warning(chan, dbname, user_id, name)
	if preds >= 10:
		await user.kick(reason='Превыщено допустимое кол-во предупреждений')
		await ctx.send(f'Пользователь {user.mention} был кикнут с сервера из-за превышения допустимого количества предупреждений')


@commands.has_permissions(administrator=True)
@bot.command()
async def снятьпреды(ctx, user: discord.Member):
	dbname = 'database/' + str(ctx.guild.name) + '.db'
	with sqlite3.connect(dbname) as db:
		cursor = db.cursor()
		cursor.execute("""UPDATE members SET warn = 0 WHERE id = ? """, (user.id,))
	await ctx.send(f'предупреждения пользователя {user} обнулены')


@commands.has_permissions(administrator=True)
@bot.command()
async def снятьпред(ctx, user: discord.Member):
	dbname =  'database/' + str(ctx.guild.name) + '.db'
	#print(dbname)
	with sqlite3.connect(dbname) as db:
		cursor = db.cursor()
		cursor.execute("""SELECT warn FROM members WHERE id = ? """, (user.id,))
		if cursor.fetchone() == None:
			nameid = await ctx.guild.fetch_member(user.id,)
			name = nameid.name
			i = 0
			cursor.execute("""INSERT INTO members (id, name, warn) VALUES(?, ?, ?)""", (user.id, name, i))

		cursor.execute("""SELECT warn FROM members WHERE id = ? """, (user.id,))
		i = cursor.fetchone()
		i = i[0]
		i = int(i) - 1
		#print(i)
		cursor.execute("""UPDATE members SET warn = ? WHERE id = ? """, (i, user.id,))
	await ctx.send(f'пользователь {user}, теперь имеет {i} предупреждений')



@bot.command()
async def преды(ctx, user: discord.Member):
	dbname = 'database/' + str(ctx.guild.name) + '.db'

	#print(dbname)
	with sqlite3.connect(dbname) as db:
		cursor = db.cursor()
		#print(user)
		#print(mem)
		cursor.execute("""SELECT warn FROM members WHERE id = ? """, (user.id,))
		if cursor.fetchone() == None:
			name = user.name
			i = 0
			cursor.execute("""INSERT INTO members (id, name, warn) VALUES(?, ?, ?)""", (user.id, name, i))

		cursor.execute("""SELECT warn FROM members WHERE id = ? """, (user.id,))
		i = cursor.fetchone()
		#print(i)
		i = i[0]
	await ctx.send(f'пользователь имеет {i} предупреждений')


@bot.command()
@commands.has_permissions(kick_members=True)
async def кик(ctx, user: discord.Member, *, reason = None):
	if not reason:
		await user.kick()
		await ctx.send(f"{user} был кикнут с сервера")
	else:
		await user.kick(reason=reason)
		await ctx.send(f"{user.split('#')[0]} был кикнут по причине {reason}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def БАН(ctx, user: discord.Member, *, reasone = None):


	if not reasone:
		await user.ban(delete_message_days=0)
		await ctx.send('Бан нахуй')
	else:
		await user.ban(reason = reasone, delete_message_days=0)
		await ctx.send('Бан нахуй')

	dbname = 'database/' + str(ctx.guild.name) + '.db'
	ban_time = int

	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""CREATE TABLE IF NOT EXISTS bans(id INTEGER, name TEXT, ban INTEGER)""")
		cur.execute("""SELECT ban FROM bans WHERE id = ?""", (user.id,))
		if cur.fetchone() is None:
			cur.execute("""INSERT INTO bans(id, name, ban) VALUES(?, ?, ?)""", (user.id, user.name, 0))

		cur.execute("""SELECT ban FROM bans WHERE id = ?""", (user.id,))
		cort = cur.fetchone()
		count_bans = cort[0]
		count_bans += 1

		cur.execute("""UPDATE bans SET ban = ? WHERE id = ?""", (count_bans, user.id,))

		if count_bans == 1:
			ban_time = 3600
		elif count_bans == 2:
			ban_time = 3600*2
		elif count_bans == 3:
			ban_time = 3600*24
		elif count_bans > 3:
			ban_time = 3600*24*7

	await asyncio.sleep(ban_time)
	await user.unban()
	await user.send('Тебя разбанили, так что можешь вернуться https://discord.gg/yWwMka2')


@bot.command()
@commands.has_permissions(ban_members=True)
async def пардон(ctx, user: discord.Member):
	await user.unban()
	await ctx.send('Разбанил его')
	await user.send('Тебя разбанили, так что можешь вернуться https://discord.gg/yWwMka2')

@bot.command()
async def баны(ctx, user: discord.Member = None):
	dbname = 'database/' + ctx.guild.name + '.db'
	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		user_id = int
		name = str
		if user is None:
			user_id = ctx.author.id
			name = ctx.author.name
		else:
			user_id = user.id
			name = user.name

		cur.execute("""SELECT ban FROM bans WHERE id = ?""", (user_id,))
		if cur.fetchone() is None:
			cur.execute("""INSERT INTO bans(id, name, ban) VALUES (?, ?, 0)""", (user_id, name,))
		cur.execute("""SELECT ban FROM bans WHERE id = ?""", (user_id,))
		count = cur.fetchone()[0]
		await ctx.send(f'Пользователь {name} имеет {count} банов')




@commands.has_permissions(administrator=True)
@bot.command()
async def добканал(ctx):
	channel = ctx.channel.id
	name = ctx.channel.name
	dbname = 'database/' + str(ctx.guild.name) + '.db'
	with sqlite3.connect(dbname) as db:
		cursor = db.cursor()
		cursor.execute("""INSERT INTO channels(id, name) VALUES(?, ?)""", (channel, name,))

	await ctx.send(f'канал {name} добавлен в список доступных каналов этого сервера')


@commands.has_permissions(administrator=True)
@bot.command()
async def add_banword(ctx, *, text):
	dbname = 'database/' + str(ctx.guild.name) + '.db'
	text = text.lower()
	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""SELECT word FROM banwords WHERE word = ?""", (text,))
		if cur.fetchone() is None:
			cur.execute("""INSERT INTO banwords(word) VALUES(?)""", (text,))
			await ctx.send(f'Слово {text} добавлено в список банвордов этого сервера')

		else:
			await ctx.send('Эта хуйня уже есть')

@commands.has_permissions(administrator=True)
@bot.command()
async def remove_banword(ctx, *, text):
	dbname = 'database/guild_' + str(ctx.guild.id) + '.db'
	text = text.lower()
	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""SELECT word FROM banwords WHERE word = ?""", (text,))
		if cur.fetchone() is None:
			await ctx.send('Этого и так нет')

		else:
			cur.execute("""DELETE FROM banwords WHERE word = ?""", (text,))
			await ctx.send(f'Слово {text} удалено из списока банвордов этого сервера')


@bot.command()
async def банворды(ctx):
	dbname = 'database/guild_' + str(ctx.guild.id) + '.db'
	words = []
	with sqlite3.connect(dbname) as db:
		cursor = db.cursor()
		cursor.execute("""SELECT word FROM banwords""")
		l = cursor.fetchall()
		count = len(l)
		for i in range(count):
			words.append(l[i][0])

	text = '** Банворды: **\n'
	for i in words:
		text = text + f'** {i} **\n'

	await ctx.send(text)



@bot.event
async def on_member_join(member):
	try: await member.send('Ебать, ты хто')
	except: pass
	guild = member.guild.name
	dbname = 'database/' + str(guild) + '.db'
	user_id = member.id
	user_name = member.name
	with sqlite3.connect(dbname) as db:
		cursor = db.cursor()
		cursor.execute("""SELECT warn FROM members WHERE id = ? """, (user_id,))
		if cursor.fetchone() == None:
			i = 0
			cursor.execute("""INSERT INTO members (id, name, warn) VALUES(?, ?, 0)""", (user_id, user_name,))

		else:
			cursor.execute("""UPDATE members SET warn = 0 WHERE id = ? """, (user_id,))

question = []

async def quest(message, ver = False):
	global question
	#print(question, ' ', message.channel.id)
	if message.channel.id not in question:
		print('question function starting in the {0}'.format(message.channel.name))
	else: return

	question.append(message.channel.id)

	try:
		msg = await bot.wait_for('message', check=lambda m: m.channel == message.channel and m.author != bot.user, timeout=60)
	except asyncio.TimeoutError:
		question.remove(message.channel.id)
		print('question function exit from the {0}'.format(message.channel.name))
		return

	#print(msg.content)
	#print(msg.content[-1])
	er = 0
	while er < 2:
		try:
			second_word = msg.content.split()[1]
		except IndexError:
			second_word = 'None'
		if list(msg.content)[-1] == '?' and (second_word not in bot.commands or (second_word == 'вероятность' and list(msg.content)[0].lower() == 'а')):
			varA = randint(1, 11)
			if randint(1, 100) == 1:
				await message.channel.send('иди нахуй')
				question.remove(message.channel.id)
				print('question function exit from the {0}'.format(message.channel.name))
				return
			if msg.content.lower().split()[0] == 'а':
				chance = randint(0, 100)
				variable = randint(1, 3)
				if variable == 1:
					answer = f'как по мне вероятность примерно {chance}%'
				elif variable == 2:
					answer = f'ну хз, процентов {chance}'
				else:
					answer = f'<:yikes:784100509446569997> наверное {chance}%'
				await msg.reply(answer)

			if varA in range(1, 6) and msg.content.lower().split()[0] != 'а':
				await message.channel.send('да')
			elif varA in range(6, 11) and msg.content.lower().split()[0] != 'а':
				await message.channel.send('нет')
			else:
				if msg.content.lower().split()[0] != 'а': await message.channel.send('<:hz:950666860649656360>')

		else: er += 1
		try:
			msg = await bot.wait_for('message', check=lambda m: m.channel == message.channel and m.author != bot.user, timeout=60)
		except asyncio.TimeoutError:
			question.remove(message.channel.id)
			print('question function exit from the {0}'.format(message.channel.name))
			return



	question.remove(message.channel.id)
	print('question function exit from the {0}'.format(message.channel.name))


"""@bot.event
async def on_command_error(ctx, error):
	if type(error) == discord.ext.commands.errors.CommandNotFound: pass
	elif type(error) == discord.ext.commands.errors.MissingRequiredArgument: await ctx.send('что-то в команде пропущено')
	elif type(error) == discord.ext.commands.errors.MissingPermissions: await ctx.send('нет прав')
	else:
		print(error)
		print(type(error))"""

#		ОБРАБОТКА СООБЩЕНИЙ

reackt_on_name = {}
play_casino = False
channel_casino = 0
spam = {}
cookie_check = []

@bot.event
async def on_message(message):
	await bot.process_commands(message)
	if message.author == bot.user: return
	if message.channel.type == discord.ChannelType.private: return
	global reackt_on_name
	global question
	try:
		dbname1 = 'database/' + str(message.guild.name) + '.db'

		with sqlite3.connect(dbname1) as db:

			cur = db.cursor()
			cur.execute("""CREATE TABLE IF NOT EXISTS members(id INTEGER, name TEXT, warn INTEGER)""")
			cur.execute("""CREATE TABLE IF NOT EXISTS channels(id INTEGER, name TEXT)""")
			cur.execute("""CREATE TABLE IF NOT EXISTS banwords(word TEXT)""")

		if message.author.id == 883711518062034955 or message.author.id == 890246306394689628:
			return
		else:
			for word in message.content.split():
				if word == '@everyone':
					if message.channel.id == 632944075368300565:
						return
					await message.channel.send('нахер ты всех позвал')

		#		ПОЛУЧЕНИЕ БАНВОРДОВ
		banword_channels = class_config.settings().get_word_ignore(f'database/{message.guild.name}_config.db')['channels']
		banword_users = class_config.settings().get_word_ignore(f'database/{message.guild.name}_config.db')['users']
		if message.channel.id in banword_channels or message.author.id in banword_users: pass
		else:
			banwords = []
			with sqlite3.connect(dbname1) as db:
				cursor = db.cursor()
				cursor.execute("""SELECT word FROM banwords""")
				l = cursor.fetchall()
				count = len(l)

				for i in range(count):
					banwords.append(l[i][0])

			#		БАНВОРДЫ
			if message.channel.id == 783305055150800956:
				return
			else:
				for word in banwords:
					a = message.content.lower()
					#print(f'|{a.split()[1]}|')
					try: second_word = a.split()[1]
					except: second_word = a
					if word in a.split():
						if word in banwords and len(message.content.split()) == 1 or 'add_banword' not in message.content and 'remove_banword' not in message.content:

							ans = randint(0, 2)
							if ans == 1:
								await message.channel.send('https://tenor.com/view/pizdets-kot-ti-che-chto-gif-5535551')
							elif ans == 2:
								await message.channel.send('Данное слово в списке банвордов этого сервера')
							elif ans == 0:
								await message.channel.send('<:crazytrollface:813440618780426300>')

							preds = await warning(message.channel.id, dbname1, message.author.id, message.author.name)
							if preds >= 10:
								await message.author.kick(reason='Превышение лимита предупреждений')
								await message.channel.send(
									f'Пользователь {message.author.mention} был кикнут из-за превышения димита предупреждений')

							break

		#		ПОЛУЧЕНИЕ ДОСТУПНЫХ КАНАЛОВ

		rchan = []
		with sqlite3.connect(dbname1) as db:
			cursor = db.cursor()
			cursor.execute("""SELECT id FROM channels""")
			chid = cursor.fetchall()
			count = len(chid)

			for i in range(count):
				rchan.append(chid[i][0])



		if message.channel.id in rchan:

			chance = randint(1, 40)
			if chance == 16:
				em = em_list[randint(1, len(em_list))]
				await message.channel.send(em)
				global cookie_check
				if em == 'хочу печеньку ' and message.channel.id not in cookie_check:
					cookie_check.append(message.channel.id)
					#print('попытка проверки')
					msg = await bot.wait_for('message', check=lambda m: m.channel == message.channel)
					#print(msg.content)
					if msg.content == '🍪':
						await give_ach('cookie', message.author.id, 'database/' + message.guild.name + '_achivs.db', message.channel.id)

					cookie_check.remove(message.channel.id)

			elif chance == 17 and randint(1, 2) == 1:
				await message.add_reaction('<:Nu_a_xule_nam:815966514821595207>')

	except: pass
	#		ОТПРАВЛЕНИЕ ЭМОДЖИКОВ В ДОСТУПНЫЕ КАНАЛЫ
	read = message.content.lower()
	read_list = read.split()

	read_list2 = list(read)
	read_list3 = list(message.content)

	capslock = list(caps.upper())
	read1 = list(message.content)
	read2 = list(read)
	new_text = message.content
	n2 = 0
	n1 = 0

	for i in read1:

		if i == '<':
			n1 = read1.index(i)
		elif i == '>':
			n2 = read1.index(i)
		if n1 != 0 and n2 != 0 or n1 == 0 and n2 != 0:
			new_text = new_text[:n1] + new_text[n2 + 1:]
			read1 = list(new_text)
			n2 = 0
			n1 = 0

	for i in new_text:
		if i in list(caps) or i in capslock: pass
		else:
			new_text = new_text.replace(i, '')


	last_symbol = ''
	ntext = ''
	for i in list(new_text.lower()):
		if i == last_symbol:
			pass
		else:
			ntext = ntext + i
			last_symbol = i



	if ntext.lower() == 'ы':
		count_in_mes = randint(1, 4)
		i = 1
		mes = str()
		for i in range(count_in_mes):
			c = randint(1, len(em_list))
			dob = em_list[c]
			if em_list[c] == 'https://cdn.discordapp.com/emojis/810658496977829908.gif?v=1':
				mes = ''
				await message.channel.send(em_list[c])
				break
			mes = mes + dob

		try:
			msg = await message.channel.send(mes)
			if 'хочу печеньку' in msg.content:
				msg1 = await bot.wait_for('message', check=lambda m: m.channel == message.channel and m.author != bot.user)
				if '🍪' in msg1.content:
					print('кто-то печенюхо собрал')
					try: await give_ach('cookie', message.author.id, 'database/' + message.guild.name + '_achivs.db', message.channel.id)
					except: pass
				elif msg.content.lower() == 'перехочешь' and randint(1, 3) == 1:
					await message.channel.send('че какой злой')
		except: pass

	elif ntext.lower() == 'а':
		if randint(1, 4) == 1:
			await message.channel.send('Хуй на')
			try: await give_ach('hui_na', message.author.id, 'database/' + message.guild.name + '_achivs.db', message.channel.id)
			except: pass

	if len(ntext) == 1: ntext = new_text

	# print(ntext)
	# print(new_text)
	try:
		if ntext[0] in capslock or ntext[1] in capslock:
			c = 0
			c1 = len(list(ntext))
			er = 0
			# print('c1: ', c1)
			for i in list(ntext):
				if i in capslock:
					c += 1
					er = 0

				else:
					if len(ntext) > 2: er += 1
					else: er += 2

					if er == 2: break
					else: c += 1

			symHA = ['х', 'а', 'п', 'з']
			haha = False
			errors_ha = 0
			tl = str(message.content.lower())
			for sym in tl:
				if sym in symHA and errors_ha < 2:
					haha = True
				else:
					errors_ha+=1


			cenz = ['блять', 'бля', 'ебать', 'пиздец', 'пизда', 'дазай', 'даз', 'сука']
			if c == c1:
				#print('кто-то капсом хуярит', ntext)
				if ntext.lower() in cenz:
					variable = randint(1, 2)
					if variable == 1:
						await message.channel.send('Че у тя там')
					elif variable == 2:
						await message.channel.send('Что опять случилось')

				else:
					if haha == True:
						pass
					else:
						if randint(1, 2) == 1:
							if len(read) > 3 and len(ntext) > 3:
								variable = randint(1, 2)
								if variable == 1:
									await message.channel.send('капс выключать не учили?')
								elif variable == 2:
									await message.channel.send('НЕ ОРИ ДОЛБОЕБ')
						else:
							pass
	except IndexError:
		pass

	spam_channel_check = class_config.settings().get_spamignore(f'database/{message.guild.name}_config.db')
	#print(spam_channel_check)
	#print(message.author.bot)

	if message.channel.id not in spam_channel_check and message.author.bot is False:
		global spam
		try:
			user_base = spam[message.author.id]
			try:
				lt = spam[message.author.id][message.channel.id]
			except KeyError:
				lt = ['', '', '', 0, 0]
		except KeyError:
			user_base = {}
			lt = ['', '', '', 0, 0]

		lt[2] = lt[1]
		lt[1] = lt[0]
		lt[0] = read
		if lt[0] != lt[1] and lt[0] != lt[2]:
			lt[3] += 1
			if lt[3] > 1:
				lt[4] = 0
				lt[3] = 0

		else:
			lt[3] = 0
			if len(read) >= 60:
				lt[4] += 3
			else:
				lt[4] += 1
			db = f'database/{message.guild.name}_config.db'
			limit = class_config.settings().get_spam_limit(db)['limit']
			al = class_config.settings().get_spam_limit(db)['alert']
			if limit == 0: pass
			else:
				if lt[4] >= limit:
					tech_channels = [918524331909337088, 919913221727600651, 918913868330311731]
					if message.channel.id in tech_channels:
						pass
					else:
						sp_text = class_config.settings().get_spam_limit(db)['text']
						if sp_text is None:
							await message.channel.send('хватит спамить')
						else:
							await message.channel.send(sp_text)
						if al == 0: pass
						else:
							if lt[4] >= al:
								#print('спамит сука')
								try: preds = await warning(message.channel.id, f'database/{message.guild.name}.db', message.author.id, message.author.name)
								except: preds = 0
								if preds >= 10:
									await message.author.kick(reason='Превышение лимита предупреждений')
									await message.channel.send(f'Пользователь {message.author.mention} был кикнут из-за превышения димита предупреждений')


		user_base[message.channel.id] = lt
		spam[message.author.id] = user_base

	try: await daily(message.guild, message.author.id, message.channel.id)
	except: pass

	symbolsha = ['а', 'х', 'з', 'п']
	ha = ['<:crazytrollface:813440618780426300>', '<:lgbt:783584039075315762>', '<:lgbt:783584039075315762>', '<:lgbt:783584039075315762>', 'хахахаха']
	if len(message.content.split()) == 1 and len(message.content) >= 5:
		rep = 0
		last_sym = ''
		if message.content == '<:lgbt:783584039075315762>':
			if randint(1, 3) == 1: await message.channel.send('<:lgbt:783584039075315762>')
		er = 0
		for i in list(message.content):
			if i in symbolsha:
				if i == last_sym: rep += 1
				last_sym = i
				if rep > 3: er += 5
				else: rep = 0
				pass
			else:
				er += 1
			if er == 2: break

		if er < 2:
			if randint(1, 15) == 1:
				await message.channel.send(ha[randint(0, len(ha) - 1)])
				#print(len(ha))

	if message.content == '<:NICE:926536218156625972>' and randint(1,3) == 1:
		await message.channel.send('<:bellisimo:950645448023101450>')


	if '<:kakao:808244649839165490>' in message.content and randint(1,10) == 5:
		await message.channel.send('<:kakao:808244649839165490>' if randint(1,2)==1 else '<:zilibobka:769654373138563092>')

	# 		ОБРАБОТКА РОФЛО-ОТВЕТОВ



	if read in net_replic['rep1']:
		if randint(1,4) == 1:
			await message.channel.send('шлюхи аргумент')
	elif read in net_replic['rep2']:
		await message.channel.send('Аргумент не нужен, пидор обнаружен')
	elif read in net_replic['rep3']:
		await message.channel.send('пидор засекречен, твой анал не вечен')
	elif read in net_replic['rep4']:
		await message.channel.send('Пидор мафиозный, твой анал спидозный')
	elif read in net_replic['rep5']:
		await message.channel.send('Анал мой вечен, твой помечен')

	try:
		if read_list[1] in return_names:
			return
		else:

			#print(question, ' ', message.channel.id)
			if message.channel.id not in question:
				#print('вопрос')

				t2 = list(read)
				t3 = list(read.lower())
				obr = t3[0] + t3[1] + t3[2]
				if t2[-1] == '?' and obr == 'даз' and message.content.split()[1] not in bot.commands:
					if message.channel.id not in question:
						question.append(message.channel.id)
						varA = randint(1,11)
						if varA in range(1,6):
							await message.channel.send('да')
						elif varA in range(6,11):
							await message.channel.send('нет')
						else:
							await message.channel.send('<:hz:950666860649656360>')

						ex = 0
						msg = await bot.wait_for('message', check=lambda m: m.channel == message.channel and m.author != bot.user)

						while list(msg.content)[-1] == '?' or ex < 2:
							if list(msg.content)[-1] == '?' and msg.content.split()[1] not in bot.commands:
								varA = randint(1, 11)
								if varA in range(1, 6):
									await message.channel.send('да')
								elif varA in range(6, 11):
									await message.channel.send('нет')
								else:
									await message.channel.send('<:hz:950666860649656360>')

								msg = await bot.wait_for('message', check=lambda m: m.channel == message.channel and m.author != bot.user)

							else:
								ex += 1
								msg = await bot.wait_for('message', check=lambda m: m.channel == message.channel and m.author != bot.user)

					question.remove(message.channel.id)

			else: pass


	except IndexError: pass

	try:
		msg = await message.channel.fetch_message(message.reference.message_id)
		user = msg.author
		if user == bot.user and message.content[-1] == '?':
			varA = randint(1, 11)
			if varA in range(1, 6):
				await message.channel.send('да')
			elif varA in range(6, 11):
				await message.channel.send('нет')
			else:
				await message.channel.send('<:hz:950666860649656360>')
			await quest(message)
	except: pass


	global reackt_on_name
	# ОПЫТ И АЧИВКИ
	try:
		dbname = 'database/' + message.guild.name + '_achivs' + '.db'
		with sqlite3.connect(dbname) as db:
			cur = db.cursor()
			cur.execute("""CREATE TABLE IF NOT EXISTS achivs(user_id INTEGER, lvl INTEGER DEFAULT 1, 
			exp INTEGER DEFAULT 0, voice INTEGER DEFAULT 0, color INTEGER DEFAULT 1, most_wins_casino INTEGER DEFAULT 0, blm BOOL DEFAULT False, 
			sus_dance BOOL DEFAULT False, free_time BOOL DEFAULT False, ucraine BOOL DEFAULT False, pupa BOOL DEFAULT False, biba BOOL DEFAULT False, 
			cenz BOOL DEFAULT False, net_pidor BOOL DEFAULT False, pidor_full BOOL DEFAULT False, da_pizda BOOL DEFAULT False, russian_game BOOL DEFAULT False, 
			hikki BOOL DEFAULT False, money_1 BOOL DEFAULT False, money_2 BOOL DEFAULT False, bebra BOOL DEFAULT False, anton BOOL DEFAULT False, 
			amogus BOOL DEFAULT False, luck_casino BOOL DEFAULT False, master_lose BOOL DEFAULT False, master_lose_2 BOOL DEFAULT False, azart_player BOOL DEFAULT False, 
			lucky_player BOOL DEFAULT False, stupid_player BOOL DEFAULT False, russia_vp BOOL DEFAULT False, lh_daz BOOL DEFAULT False, motivate BOOL DEFAULT False, 
			hui_na BOOL DEFAULT False, gop BOOL DEFAULT False, cookie BOOL DEFAULT False, low_iq1 BOOL DEFAULT False, low_iq2 BOOL DEFAULT False, pasol_nahui BOOL DEFAULT False)""")
	except: pass
	read_list1 = str
	try:
		read_list1 = read_list[-1]
	except IndexError: pass

	read_list2 = list(read)
	user_id = message.author.id
	channel = message.channel.id
	exp_mess = len(read_list2)
	blin = 'блин'
	if read in ach_list:
		if read == 'негры пидоры':
			await message.channel.send('поддерживаю')
			ach_name = 'blm'
			await give_ach(ach_name, user_id, dbname, channel)

		elif read == 'https://cdn.discordapp.com/emojis/810658496977829908.gif?v=1':
			i = randint(1, 2)
			if i == 1:
				await message.channel.send('https://cdn.discordapp.com/emojis/810658496977829908.gif?v=1')
			elif i == 2:
				await message.channel.send('https://tenor.com/view/mm-gif-23980179')
			ach_name = 'sus_dance'
			await give_ach(ach_name, user_id, dbname, channel)

		elif read == 'amogus':
			ach_name = 'amogus'
			await give_ach(ach_name, user_id, dbname, channel)
			await message.channel.send('is sus')

		elif read == 'чем заняться' or read == 'чем заняться?' or 'даз чем заняться':
			sui = randint(0, 100)
			if sui == 1:
				await message.channel.send('предлагаю пойти и устроить геноцид')
				ach_name = 'free_time'
				await give_ach(ach_name, user_id, dbname, channel)
			else:
				r = randint(1, 6)
				if r == 1:
					await message.channel.send('хз')
				elif r == 2 or r == 3:
					games = get_games(message.author.id)
					await message.channel.send(f'пойди в {choice(games)} поиграй')

				elif r == 4 or r == 5 or r == 6:
					try:
						user = message.author
						role_list = ['Манга', 'Аниме', 'Недопрограмист', 'Real Life', 'Игры']
						user_roles = []
						role_name = {
							'Манга': 'мангу почитай',
							'Аниме': 'посмотри какое-нибудь аниме(хент тоже как вариант)',
							'Недопрограмист': 'недопрограмист блет, иди учи нормально програмирование',
							'Культ дазая': 'я кшн понимаю что ты в моем культе, но меня мучать не надо',
							'Real Life': choice([' че в реал лайф делать, я не мазохист', ' че в реале Real life делать. Ну подрочи']),
							'Игры': 'Поиграй во что-нибудь'
						}
						for name in role_list:
							role = utils.get(message.guild.roles, name=name)
							#print(role)
							if role in user.roles:
								user_roles.append(name)
								#print(user_roles)

						conf_role = choice(user_roles)
						await message.channel.send(role_name[conf_role])
						if conf_role == 'Игры':
							games = get_games(message.author.id)
							await message.channel.send(f'В {choice(games)} например')

					except:
						await message.channel.send('хз')


		elif read == 'слава украине':
			i = randint(1, 5)
			text = str
			if i == 1:
				text = 'хохла спросить забыли'
			elif i == 2:
				text = 'Сала Украине'
			elif i == 3:
				text = 'Героям слава'
			elif i == 4:
				text = 'Салу слава'
			elif i == 5:
				text = 'СВОДУ ХОХЛАМ'

			await message.channel.send(text)
			ach_name = 'ucraine'
			await give_ach(ach_name, user_id, dbname, channel)

		elif read == 'пупа' or read == 'лупа':
			await message.channel.send('лупа и пупа')
			ach_name = 'pupa'
			await give_ach(ach_name, user_id, dbname, channel)

		elif read == 'биба' or read == 'боба' or read == 'biba' or read == 'boba':
			await message.channel.send('биба и боба')
			ach_name = 'biba'
			await give_ach(ach_name, user_id, dbname, channel)

		elif read == 'антон':
			await message.channel.send('гандон')
			ach_name = 'anton'
			await give_ach(ach_name, user_id, dbname, channel)

		elif read == 'нюхай бебру':
			await message.channel.send('сам занюхни')
			ach_name = 'bebra'
			await give_ach(ach_name, user_id, dbname, channel)


	elif read == 'нет':
		a = randint(1, 4)
		if a == 1:
			await message.channel.send('Пидора ответ')
			ach_name = 'net_pidor'
			await give_ach(ach_name, user_id, dbname, channel)

	elif read_list1 == 'нет':
		a = randint(1, 8)
		if a == 1:
			await message.channel.send('Пидора ответ')
			ach_name = 'net_pidor'
			await give_ach(ach_name, user_id, dbname, channel)

	elif read == 'да':
		a = randint(1, 5)
		if a == 1:
			await message.channel.send('Пизда')
			ach_name = 'da_pizda'
			await give_ach(ach_name, user_id, dbname, channel)

	elif read_list1 == 'да':
		a = randint(1, 10)
		if a == 1:
			await message.channel.send('Пизда')
			ach_name = 'da_pizda'
			await give_ach(ach_name, user_id, dbname, channel)

	elif read_list1 == 'ок' or read == 'ок':
		a = randint(1, 10)
		if a == 1:
			await message.channel.send('хуёк')
			ach_name = 'russian_game'
			await give_ach(ach_name, user_id, dbname, channel)

	elif read in net_replic['rep6'] or read in net_replic['rep7']:
		ach_name = 'pidor_full'
		i = randint(1, 3)
		if i == 1:
			await message.channel.send('Да иди ты нахуй, писатель ебаный')
		elif i == 2:
			await message.channel.send('хули ты такой креативный блять')
		elif i == 3:
			await message.channel.send('рифмоплет хуев')

		await give_ach(ach_name, user_id, dbname, channel)

	elif blin in read_list:
		a = randint(1, 2)

		if a == 1:
			await message.channel.send('Не блин, а блять')
			ach_name = 'cenz'
			await give_ach(ach_name, user_id, dbname, channel)

	elif read.lower() in reackt_names and (message.channel.id not in reackt_on_name or reackt_on_name[message.channel.id] == 0):

		reackt_on_name[message.channel.id] = 1
		ans = randint(1, 3)
		if reackt_on_name[message.channel.id] == 3:
			await message.channel.send('Да хули вы доебались')
			ach_name = 'hikki'
			await give_ach(ach_name, user_id, dbname, channel)
			reackt_on_name[message.channel.id] = 0
		if ans == 1:
			await message.channel.send('Я тут')
		elif ans == 2 or ans == 3:
			await message.channel.send('чо надо')
		try:
			msg = await bot.wait_for('message', check=lambda m: m.channel == message.channel, timeout=120)
			while msg.content in reackt_names:
				reackt_on_name[message.channel.id] += 1
				ans = randint(1, 3)
				if reackt_on_name[message.channel.id] == 3:
					await message.channel.send('Да хули вы доебались')
					ach_name = 'hikki'
					await give_ach(ach_name, user_id, dbname, channel)
					reackt_on_name[message.channel.id] = 0
				if ans == 1:
					await message.channel.send('Я тут')
				elif ans == 2 or ans == 3:
					await message.channel.send('чо надо')
				msg = await bot.wait_for('message', check=lambda m: m.channel == message.channel, timeout=120)
			reackt_on_name[message.channel.id] = 0
		except asyncio.TimeoutError:
			reackt_on_name[message.channel.id] = 0
			return
		try:
			try:
				second_word = msg.content.split()[1]
			except IndexError:
				second_word = 'None'
			if list(msg.content)[-1] == '?' and second_word not in bot.commands:

				if message.channel.id not in question:
					question.append(message.channel.id)
					varA = randint(1, 11)
					if varA in range(1, 6):
						await message.channel.send('да')
					elif varA in range(6, 11):
						await message.channel.send('нет')
					else:
						await message.channel.send('<:hz:950666860649656360>')

					ex = 0
					msg = await bot.wait_for('message', check=lambda m: m.channel == message.channel and m.author != bot.user, timeout=300)

					while list(msg.content)[-1] == '?' or ex < 2:
						try: second_word = msg.content.split()[1]
						except IndexError: second_word = 'None'
						if list(msg.content)[-1] == '?' and second_word not in bot.commands:
							varA = randint(1, 11)
							if varA in range(1, 6):
								await message.channel.send('да')
							elif varA in range(6, 11):
								await message.channel.send('нет')
							else:
								await message.channel.send('<:hz:950666860649656360>')
							msg = await bot.wait_for('message', check=lambda m: m.channel == message.channel and m.author != bot.user, timeout=300)

						else:
							ex += 1
							msg = await bot.wait_for('message', check=lambda m: m.channel == message.channel and m.author != bot.user, timeout=300)
		except asyncio.TimeoutError:
				question.remove(message.channel.id)



	else:
		if message.author.id == 883711518062034955 or message.author.id == 890246306394689628:
			return
		else:
			try:
				if message.content == 'пизда' or message.content == 'Пизда':
					i = randint(1, 4)
					if i == 1:
						await message.channel.send('хуй')
						ach_name = 'russian_game'
						await give_ach(ach_name, user_id, dbname, channel)

				elif message.content == 'хуй' or message.content == 'Хуй':
					a = randint(1, 2)
					i = randint(1, 4)
					if i == 1:
						if a == 1:
							await message.channel.send('пизда')
						else:
							await message.channel.send('ХУЙ')
						ach_name = 'russian_game'
						await give_ach(ach_name, user_id, dbname, channel)

				elif message.content == 'ХУЙ':
					await message.channel.send('ХУУУУУУУЙ')
					ach_name = 'russian_game'
					await give_ach(ach_name, user_id, dbname, channel)

				else:
					global casino_players
					global casino_channels
					if message.channel.id in casino_channels and message.author.id in casino_players and message.channel.id != 783305055150800956:
						pass
					else:
						await give_exp(exp_mess, user_id, message.guild, channel)
			except: pass

	if 'найс' in message.content.lower() and randint(1, 4) == 1:
		await message.channel.send('<:NICE:926536218156625972>')

	if message.channel.id == 896752165899616257 and message.author.id == 971839492245819433:
		if message.content.split()[0] == 'mp':
			uid = int(message.content.split()[1])
			global users_mp
			try:
				mp = users_mp[uid]
			except KeyError:
				mp = 'None'

			await message.channel.send(f'{uid}:{mp}')
@bot.event
async def on_voice_state_update(member, before, after):
	dbname = 'database/' + member.guild.name + '_achivs.db'
	#chaname = before.channel.name if not after.channel else after.channel
	if before.channel is None and after.channel is not None and after.channel.id not in ignor_voice:
		t1 = time.time()
		t1 = int(round(t1))
		await tm1(dbname, member.id, t1)

	elif before.channel is not None and after.channel is None and before.channel.id not in ignor_voice:
		t2 = time.time()
		t2 = int(round(t2))
		tm = await tm2(dbname, member.id, t2)
		exp = int(round(tm / 60) * 5)
		await give_exp(exp, member.id, member.guild, 934827044238426112)
		await up_voice(dbname, member.id, tm)


	#else: print(f'канал {chaname} не поддерживается')




# 		КАРТИНКИ БЕЗ БД

@bot.command()
async def cat(ctx):
	response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
	json_data = json.loads(response.text) # Извлекаем JSON
	chance = randint(1,2)
	name = str
	if chance == 1:
		name = 'Рандомный кiт'
	elif chance ==  2:
		name = 'Кiт, ты маму мав?'
	embed = discord.Embed(color = 0xff9900, title = name) # Создание Embed'a
	embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
	await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def dog(ctx):
	response = requests.get('https://some-random-api.ml/img/dog') # Get-запрос
	json_data = json.loads(response.text) # Извлекаем JSON
	chance = randint(1,3)
	name = str
	if chance == 1:
		name = 'рандомный обед корейца'

	elif chance == 2:
		name = 'Рандомная шаверма'

	elif chance == 3:
		name = 'Песель'

	embed = discord.Embed(color = 0xff9900, title = name) # Создание Embed'a
	embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
	await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def fox(ctx):
	response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
	json_data = json.loads(response.text) # Извлекаем JSON
	chance = randint(1,3)
	if chance == 1:
		name = 'Девятихвостый после запоя'
	elif chance ==  2:
		name = 'Рандомный лис'
	elif chance == 3:
		name = 'лисица сэнуо на минималках'
	embed = discord.Embed(color = 0xff9900, title = name) # Создание Embed'a
	embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
	await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def panda(ctx):
	response = requests.get('https://some-random-api.ml/img/panda') # Get-запрос
	json_data = json.loads(response.text) # Извлекаем JSON
	chance = randint(1,2)
	name = str
	if chance == 1:
		name = 'Рандомная панда'
	elif chance ==  2:
		name = 'Кунг фу панда на минималках'
	embed = discord.Embed(color = 0xff9900, title = name) # Создание Embed'a
	embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
	await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def bird(ctx):
	response = requests.get('https://some-random-api.ml/img/bird') # Get-запрос
	json_data = json.loads(response.text) # Извлекаем JSON
	chance = randint(1,2)
	name = str
	if chance == 1:
		name = 'Рандомная птица'
	elif chance ==  2:
		name = 'WINNER WINNER CHICKEN DINNER'
	embed = discord.Embed(color = 0xff9900, title = name) # Создание Embed'a
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
async def мэджик(ctx, member: discord.Member=None):
	async with ctx.channel.typing():
		if member is None:
			member = ctx.author

		im1 = Image.open(r'ы\test1.jpg') if randint(1,2) == 1 else Image.open('ы/test1_2.jpg')
		if member.name == 'yavseznay':
			im1 = Image.open('ы/senya.jpg')
		url = member.avatar_url
		img_data = requests.get(url).content
		with open('ы/test2.jpg', 'wb') as handler:
			handler.write(img_data)

		im2 = Image.open('ы/test2.jpg')
		ns1 = im2.size[0]*10
		ns2 = im2.size[1]*10
		im2 = im2.resize((ns1, ns2))
		im2.thumbnail((270, 270))

		mask_im = Image.new("L", im2.size, 0)
		draw = ImageDraw.Draw(mask_im)
		draw.ellipse((0, 0, 270, 270), fill=255)

		new_im = im1.copy()
		new_im.paste(im2, (400, 150), mask_im)
		new_im.save(r'ы\new_img.jpg', quality = 95)
		#new_im.show()

		im1.close()
		im2.close()
		mask_im.close()
		file = r'ы\new_img.jpg'

		await ctx.send(file=discord.File(file))


@bot.command()
async def помянем(ctx, member: discord.Member = None):
	async with ctx.channel.typing():
		if member is None:
			return

		im1 = Image.open('ы/maxresdefault.jpg')

		resp = requests.get(member.avatar_url, stream=True).raw

		im2 = Image.open(resp)
		ns1 = im2.size[0] * 5
		ns2 = im2.size[1] * 5
		im2 = im2.resize((ns1, ns2))
		im2.thumbnail((160, 160))
		im2 = ImageOps.expand(im2, border=5, fill=0x000000)

		new_im = im1.copy()
		new_im.paste(im2, (512, 112))
		new_im.save(r'ы\помянем.jpg', quality=95)
		# new_im.show()

		im1.close()
		im2.close()
		file = r'ы\помянем.jpg'

		await ctx.send(file=discord.File(file))


#		ВЕРОЯТНОСТИ

@bot.command()
async def вероятность(ctx, *, text):
	chance = randint(0,100)
	variable = randint(1,3)
	if variable == 1:
		answer = f'как по мне вероятность примерно {chance}%'
	elif variable == 2:
		answer = f'ну хз, процентов {chance}'
	else:
		answer = f'<:yikes:784100509446569997> наверное {chance}%'
	await ctx.reply(answer)
	await quest(ctx.message, ver=True)

@bot.command()
async def монетка(ctx):
	m = randint(1,2)
	if m == 1:
		await ctx.send('Орёл')
	else:
		await ctx.send('Решка')

@bot.command()
async def мoнетка(ctx):
	await ctx.send('Решка')
	ach_name = 'money_1'
	dbname = 'database/' + ctx.guild.name + '_achivs' + '.db'
	await give_ach(ach_name, ctx.author.id, dbname, ctx.channel.id)

@bot.command()
async def монeтка(ctx):
	await ctx.send('Орёл')
	ach_name = 'money_2'
	dbname = 'database/' + ctx.guild.name + '_achivs' + '.db'
	await give_ach(ach_name, ctx.author.id, dbname, ctx.channel.id)

@bot.command()
async def число(ctx, *, text):
	numbers = str.split(text)
	num1 = numbers[0]
	num2 = numbers[1]
	if randint(1,20) in range(1,19):
		num = randint(int(num1), int(num2))
		await ctx.send(f'Число {num}')
	else:
		num = randint(-999999, 9999999)
		await ctx.send(f'Число {num}')


@bot.command()
async def статмана(ctx):
	user_id = ctx.author.id
	up_mp_2(user_id)
	await ctx.send(file = discord.File('mp_stats/finish_time.jpg'))
	#await ctx.send(file = discord.File('mp_stats/finish.jpg'))



users_mp = {}


@bot.command()
async def мана(ctx):
	global users_mp
	gin = await bot.fetch_channel(896752165899616257)
	await gin.send(f'mp {ctx.author.id}')
	async with ctx.channel.typing():
		none = False
		ruid = 0
		try:
			while True:
				try:
					msg = await bot.wait_for('message', check=lambda m: m.channel.id == 896752165899616257 and m.author.id == 971839492245819433, timeout=5)
					ruid = int(msg.content.split(':')[0])
					break
				except ValueError: continue

			while ruid != ctx.author.id:
				msg = await bot.wait_for('message', check=lambda m: m.channel.id == 896752165899616257 and m.author.id == 971839492245819433, timeout=5)
				try:
					ruid = int(msg.content.split(':')[0])
					break
				except ValueError:
					continue
		except asyncio.TimeoutError:
			none = True

		#print(ruid)
		#print(msg.content.split(':')[1])

		if none is True or (msg.content.split(':')[1] == 'None'):
			try:
				um = users_mp[ctx.author.id]
			except KeyError:
				um = None
			if um:
				if um >= 5 and um <= 95:
					mp = up_mp_1(ctx.author.id, [um - 5, um + 5])
				elif um <= 5 and um > -1:
					mp = up_mp_1(ctx.author.id, [um, um + 5])
				elif um >= 95:
					mp = up_mp_1(ctx.author.id, [um - 5, um])
			else:
				mp = up_mp_1(ctx.author.id, [0, 100])
		else:
			a = int(msg.content.split(':')[1]) - 10
			b = int(msg.content.split(':')[1]) + 10
			mp = up_mp_1(ctx.author.id, [a, b])

		mana_msg = [f'{ctx.author.mention}у тебя {mp}% маны', f'{ctx.author.mention} примерно {mp}%']

	await ctx.send(choice(mana_msg))
	if int(mp) <= 40 and randint(1, 4) != 1:
		if randint(1, 2) == 1:
			await ctx.send('<:crazytrollface:813440618780426300>')
		else:
			await  ctx.send('<:fck_u_cat:784100508620423219>')

	if int(mp) >= 75:
		c = randint(1, 3)
		if c == 1:
			await ctx.send('<:hehe_buoy:784100424524890162>')
		elif c == 2:
			await ctx.send('<:Nu_a_xule_nam:815966514821595207>')
		else:
			await ctx.send('<:pogchamp:771762939228717056>')

	users_mp[ctx.author.id] = mp
	await asyncio.sleep(120)
	try: del users_mp[ctx.author.id]
	except: pass

#		РОФЕЛЬНАЯ ХЕРНЯ

@bot.command()																#команда "ы"
async def ы(ctx):
	count_in_mes = randint(1,4)
	i = 1
	mes = str()
	for i in range(count_in_mes):
		c = randint(1,len(em_list))
		dob = em_list[c]
		if em_list[c] == 'https://cdn.discordapp.com/emojis/810658496977829908.gif?v=1':
			mes = ''
			await ctx.send(em_list[c])
			break
		mes = mes + dob

	try:
		msg = await ctx.send(mes)
		if 'хочу печеньку' in msg.content:
			msg1 = await bot.wait_for('message', check=lambda m: m.channel == ctx.channel and m.author != bot.user)
			if '🍪' in msg1.content:
				print('кто-то печенюхо собрал')
				await give_ach('cookie', ctx.author.id, 'database/' + ctx.guild.name + '_achivs.db', ctx.channel.id)
			elif msg.content.lower() == 'перехочешь' and randint(1, 3) == 1:
				await ctx.send('че какой злой')
	except: pass


@bot.command()
async def забань(ctx, *, text):
	print(text)
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

@commands.has_permissions(administrator=True)
@bot.command()
async def all(ctx):
	for i in range(15):
		await ctx.send('@everyone лохи')

@commands.has_permissions(administrator=True)
@bot.command()
async def ебанаты(ctx):
	os.startfile(r'C:\Users\user\Desktop\питон\Дазай\piggy.py')
	os.startfile(r'C:\Users\user\Desktop\питон\Дазай\piggy2.py')

@bot.command()
async def моя(ctx, *, text=None):
	if text == 'смерть':
		i = randint(1,2)
		month = randint(1, 12)
		mon_name = name_month[month]
		interval = int()
		if randint(1, 4) == 1:
			interval = 2100
		else:
			interval = 2030

		yeare = randint(2022, interval)
		days = day_in_month[month]
		day = randint(1, days)
		date_deth = f'{day} {mon_name} {yeare} года'
		if i == 1:
			p = choice(deth_info)
			answer = f'ты {p} {date_deth}'
			await ctx.send(answer)
		elif i == 2:
			p = choice(deth_info2)
			answer = f'тебя {p} {date_deth}'
			await ctx.send(answer)

	else:
		await ctx.send('моя твоя не понимать')
		await give_ach('gop', ctx.author.id, 'database/' + ctx.guild.name + '_achivs.db', ctx.channel.id)




@commands.has_role(889842559487189002)
@bot.command()
async def добарт(ctx, *, content):
	with sqlite3.connect('anime_img.db') as db:
		cursorA = db.cursor()

		cursorA.execute("""CREATE TABLE IF NOT EXISTS imges(id INTEGER, url TEXT)""")
		cursorA.execute("""SELECT id FROM imges""")

		id = cursorA.fetchall()
		idc = []
		for i in id:
			idc.append(int(i[0]))

		id = max(idc) + 1
		cursorA.execute("""INSERT INTO imges(id, url) VALUES(?, ?)""", (id, content,))
		await ctx.send('Арт добавлен')


@bot.command()
async def арты(ctx):
	with sqlite3.connect('anime_img.db') as db:
		cursorA = db.cursor()

		cursorA.execute("""CREATE TABLE IF NOT EXISTS imges(id INTEGER, url TEXT)""")
		cursorA.execute("""SELECT id FROM imges""")

		id = cursorA.fetchall()
		idc = []
		for i in id:
			idc.append(int(i[0]))

		m1 = min(idc)
		m2 = max(idc)
		a = randint(m1, m2)
		cursorA.execute("""SELECT url FROM imges WHERE id = ? """, (a,))
		t = cursorA.fetchone()
		text = t[0]
		emb = discord.Embed(color = 0xff9900, title = 'Рандомный арт')
		emb.set_image(url = str(text))
		await ctx.send(embed = emb)


@bot.command()
async def манга(ctx):
	async with ctx.channel.typing():
		types = [0, 2]
		manhv = []

		for i in types:
			for p in range(1, 20):
				cont = mangaclient.get_user_bookmarks(type=i, page=p)["content"]
				for n in cont:
					manhv.append({
						"name": n["title"]["rus_name"],
						"img": "https://api.remanga.org" + n["title"]["img"]["high"],
						"total-votes": n["title"]["total_votes"],
						"rated": n['rated']
					})

		manhva = choice(manhv)

		p = requests.get(manhva["img"])
		out = open("ы/manhva.jpg", "wb")
		out.write(p.content)
		out.close()

		file = discord.File("ы/manhva.jpg")

		rate = manhva["rated"] if manhva["rated"] is not None else "пока нет оценки"
		print(len(manhv))
		emb = discord.Embed(title=f'{manhva["name"]}', description=f'оценка разраба: {rate}')
		emb.set_image(url="attachment://manhva.jpg")
		emb.set_footer(text=f'голосов {manhva["total-votes"]}')

	await ctx.send(file=file, embed=emb)



@bot.command()
async def добавь(ctx, p, text):
    if ctx.channel.type != discord.ChannelType.private: return
    dev = await bot.fetch_user(578526838025093124)
    if p == 'обои':
        await dev.send(f'добавь обои: {text}')
    if p == 'аниме':
        await dev.send(f'добавь аниме: {text}')
    if p == 'арт':
        await dev.send(f'добавь арт: {text}')


@commands.has_role(889842559487189002)
@bot.command()
async def добобои(ctx, *, content):
	with sqlite3.connect('wallpaper.db') as db:
		cursorO = db.cursor()

		cursorO.execute("""CREATE TABLE IF NOT EXISTS imges(id INTEGER, url TEXT)""")
		cursorO.execute("""SELECT id FROM imges""")

		id = cursorO.fetchall()
		idc = []
		for i in id:
			idc.append(int(i[0]))

		id = max(idc) + 1
		cursorO.execute("""INSERT INTO imges(id, url) VALUES(?, ?)""", (id, content,))
		await ctx.send('Новые обои добавлены')


@bot.command()
async def обои(ctx):
	with sqlite3.connect('wallpaper.db') as db:
		cursorO = db.cursor()

		cursorO.execute("""CREATE TABLE IF NOT EXISTS imges(id INTEGER, url TEXT)""")
		cursorO.execute("""SELECT id FROM imges""")

		id = cursorO.fetchall()
		idc = []
		for i in id:
			idc.append(int(i[0]))

		m1 = min(idc)
		m2 = max(idc)
		a = randint(m1, m2)
		cursorO.execute("""SELECT url FROM imges WHERE id = ? """, (a,))
		t = cursorO.fetchone()
		text = t[0]
		emb = discord.Embed(color = 0xff9900, title = 'Рандомные обои')
		emb.set_image(url = str(text))
		await ctx.send(embed = emb)


@commands.has_role(889842559487189002)
@bot.command()
async def добаниме(ctx, *, name: str):
	with sqlite3.connect('anime.db') as db:
		cursora = db.cursor()

		cursora.execute("""SELECT id FROM anime WHERE name = ?""", (name,) )
		if cursora.fetchone() is None:

			cursora.execute("""SELECT id FROM anime""")
			id = cursora.fetchall()
			idc = []
			for i in id:
				idc.append(int(i[0]))
			id = max(idc) + 1

			cursora.execute("""INSERT INTO anime(id, name) VALUES (?, ?)""", (id, name))
			await ctx.send(f'Запись данных об {name}')
			await ctx.send(f'Введите url превьюшки')
			msg = await bot.wait_for('message', check = lambda m: m.channel == ctx.channel and m.author.id == ctx.author.id)
			url = msg.content
			cursora.execute("""UPDATE anime SET image = ? WHERE id = ? """, (url, id,))

			await ctx.send('Введите теги')
			msg1 = await bot.wait_for('message', check = lambda m: m.channel == ctx.channel and m.author.id == ctx.author.id)
			tags = msg1.content
			cursora.execute("""UPDATE anime SET tags = ? WHERE id = ? """, (tags, id,))

			await ctx.send('Введите количество серий')
			msg2 = await bot.wait_for('message', check = lambda m: m.channel == ctx.channel and m.author.id == ctx.author.id)
			count = msg2.content
			cursora.execute("""UPDATE anime SET count = ? WHERE id = ? """, (count, id,))

			await ctx.send('Введите оценку')
			msg3 = await bot.wait_for('message', check = lambda m: m.channel == ctx.channel and m.author.id == ctx.author.id)
			est = msg3.content
			cursora.execute("""UPDATE anime SET est = ? WHERE id = ? """, (est, id,))

			await ctx.send('Введите дату релиза')
			msg4 = await bot.wait_for('message', check = lambda m: m.channel == ctx.channel and m.author.id == ctx.author.id)
			dat = msg4.content
			cursora.execute("""UPDATE anime SET dat = ? WHERE id = ? """, (dat, id,))

			await ctx.send(f'Информация об аниме {name} занесена')
		else:
			await ctx.send('Это аниме уже есть в базе данных, используйте функцию редактирования')


@bot.command()
async def раниме(ctx):
	with sqlite3.connect('anime.db') as db:
		cursora = db.cursor()

		cursora.execute("""SELECT id FROM anime""")

		id = cursora.fetchall()
		idc = []
		for i in id:
			idc.append(int(i[0]))

		m1 = min(idc)
		m2 = max(idc)
		a = randint(m1, m2)

		cursora.execute("""SELECT name FROM anime WHERE id = ? """, (a,))
		name = cursora.fetchone()[0]

		cursora.execute("""SELECT image FROM anime WHERE id = ? """, (a,))
		image_url = cursora.fetchone()[0]

		cursora.execute("""SELECT tags FROM anime WHERE id = ? """, (a,))
		tags = cursora.fetchone()[0]

		cursora.execute("""SELECT count FROM anime WHERE id = ? """, (a,))
		count = cursora.fetchone()[0]

		cursora.execute("""SELECT est FROM anime WHERE id = ? """, (a,))
		est = cursora.fetchone()[0]

		cursora.execute("""SELECT dat FROM anime WHERE id = ? """, (a,))
		date = cursora.fetchone()[0]


		emb = discord.Embed(color = 0x07ff00, title = name)
		emb.add_field(name = f'{count} серий', value = tags, inline=True)
		emb.add_field(name = 'оценка', value = est, inline = True)
		emb.set_image(url = image_url)
		emb.set_footer(text = f'дата релиза {date}')

		await ctx.send(embed = emb)

@bot.command()
async def редактинфо(ctx):
	emb = discord.Embed(color = 0x07ff00, title = 'Информация о параметрах редактирования')
	emb.add_field(name = 'image', value='редактирование превью аниме', inline = False)
	emb.add_field(name = 'tags', value='редактирование тегов аниме', inline=  False)
	emb.add_field(name = 'count', value='редактирование количества серий аниме', inline=  False)
	emb.add_field(name = 'est', value='редактирование оценки аниме', inline=  False)
	await ctx.send(embed = emb)

@commands.has_role(889842559487189002)
@bot.command()
async def редактаниме(ctx, *, text):
	with sqlite3.connect('anime.db') as db:
		cursora = db.cursor()
		parametr = text.split(' п: ')[1]
		name = text.split(' п: ')[0]
		cursora.execute("""SELECT id FROM anime WHERE name = ?""", (name,))
		if cursora.fetchone() is None:
			await ctx.send('Аниме не обнаружено, возможно вы не правильно указали имя или его еще не добавили')
		else:
			await ctx.send('введите новое значение параметра')
			msg = await bot.wait_for('message', check = lambda m: m.channel == ctx.channel and m.author.id == ctx.author.id)
			meaning = msg.content
			if parametr == 'image':
				cursora.execute("""UPDATE anime SET image = ? WHERE name = ?""", (msg, name))
			elif parametr == 'tags':
				cursora.execute("""UPDATE anime SET tags = ? WHERE name = ?""", (msg, name))
			elif parametr == 'count':
				cursora.execute("""UPDATE anime SET count = ? WHERE name = ?""", (msg, name))
			elif parametr == 'est':
				cursora.execute("""UPDATE anime SET est = ? WHERE name = ?""", (msg, name))
		await ctx.send('По идее данные обновлены')


@bot.command()
async def переведи(ctx, lang, *, text: str):
	trans = Translator()
	a = randint(1,8)
	user_id = ctx.author.id
	channel = ctx.channel.id
	dbname = 'database/' + ctx.guild.name + '_achivs.db'
	if text.lower() == 'я из россии':
		await ctx.send('RUSSIA RUSSIA VODKA PUTIN FUCK U PICE OF SHIT')
		await give_ach('russia_vp', user_id, dbname, channel)
	elif a == 1:
		await ctx.send(bad_translator[a])
	elif a == 2:
		await ctx.send(bad_translator[a])
	elif a == 3:
		await ctx.send(bad_translator[a])

	if lang == 'ru':
		result = trans.translate(str(text), dest='ru')
		await ctx.send(f'перевод: {result.text}')
	else:
		if lang in googletrans.LANGUAGES:
			result = trans.translate(str(text), dest=lang)
			await ctx.send(f'перевод: {result.text}, произношение: {result.pronunciation}')
		else:
			await ctx.send('не ебу че за язык')

@bot.command()
async def языки(ctx):
	emb = discord.Embed(title='доступные обозначения языков', color=0xffffff)
	emb1 = discord.Embed(title='доступные обозначения языков 2', color=0xffffff)
	emb2 = discord.Embed(title='доступные обозначения языков 3', color=0xffffff)
	emb3 = discord.Embed(title='доступные обозначения языков 4', color=0xffffff)

	n = 0
	count = 0
	for i in googletrans.LANGUAGES:
		znach = bool()
		if n == 2:
			znach = False
			n = 0
		else:
			znach = True
			n += 1
		if count <= 30:
			emb.add_field(name=f'{i} : {googletrans.LANGUAGES[i]}', value='доступен', inline=znach)
		elif count <= 60 and count > 30:
			emb1.add_field(name=f'{i} : {googletrans.LANGUAGES[i]}', value='доступен', inline=znach)
		elif count <= 100 and count > 60:
			emb2.add_field(name=f'{i} : {googletrans.LANGUAGES[i]}', value='доступен', inline=znach)
		else:
			emb3.add_field(name=f'{i} : {googletrans.LANGUAGES[i]}', value='доступен', inline=znach)

		count += 1

	await ctx.send(embed=emb)
	await ctx.send(embed=emb1)
	await ctx.send(embed=emb2)
	await ctx.send(embed=emb3)

@bot.command()
async def язык(ctx, znach):
	trans = Translator()
	if znach in googletrans.LANGUAGES:
		result = trans.translate(str(googletrans.LANGUAGES[znach]), dest='ru')
		await ctx.send(result.text)
	else:
		lang_in_list = trans.translate(znach, dest='en').text.lower()
		n = False
		for i in googletrans.LANGUAGES:
			# print(googletrans.LANGUAGES[i] + ' <<>> ' + lang_in_list)
			if googletrans.LANGUAGES[i] == lang_in_list:
				await ctx.send(i)
				n = True
				break

		if n == False:
			await ctx.send('ошибка')




@bot.command()
async def кто(ctx, *, user):
	user = user.replace('?', '')
	if user == 'я':
		if ctx.author.nick == None:
			await ctx.send(f'{ctx.author.name} ты {choice(nicknames)}')
		else:
			await ctx.send(f'{ctx.author.nick} ты {choice(nicknames)}')
	else:
		if user == 'ты':
			user = 'я'
			var = choice(nicknames)
			answer = str()
			if var == ', вам надо умереть':
				answer = 'мне надо умереть'
			else:
				answer = f'{user} {var}'

			await ctx.send(answer)
		else:
			await ctx.send(f'{user} {choice(nicknames)}')



@bot.command()
async def iq(ctx, user: discord.Member = None):
	chance = randint(1, 100)
	mem = ctx.author if user is None else user
	db = f'database/{ctx.guild.name}_achivs.db'
	if chance == 1:
		iq = randint(-5, 30)

	elif chance > 95:
		iq = randint(140, 200)
	else:
		iq = randint(70, 140)

	if not user:
		await ctx.send(f'По моим подсчетам у тебя {iq} iq')
	else:
		if user == bot.user:
			await ctx.send('А ты не прихуел мой iq спрашивать? Ты ска таких чисел не знаешь чмо ты тупое')
		else:
			await ctx.send(f'{user.mention} по моим подсчетам у тебя {iq} iq')

	if chance == 1:
		await give_ach('low_iq1', mem.id, db, ctx.channel.id)
		if iq == 0:
			await give_ach('low_iq2', mem.id, db, ctx.channel.id)
	await quest(ctx.message)



async def ili(chan, text):
	channel = bot.get_channel(chan)
	a = text.split('или')
	i = len(a)
	variables = {1: 'первое', 2: 'второе', 3: 'третье', 4: 'четвертое', 5: 'пятое'}
	await channel.send(f'я думаю {variables[randint(1, i)]}')


@bot.command()
async def стоит(ctx, *, text):
	await ili(ctx.channel.id, text)
	await quest(ctx.message)

@bot.command()
async def будет(ctx, *, text):
	await ili(ctx.channel.id, text)
	await quest(ctx.message)


@bot.command()
async def выбери(ctx, *, text):
	variabels = text.split(' или ')
	await ctx.send(f'я выбираю {choice(variabels)}')
	await quest(ctx.message)

@bot.command()
async def оцени(ctx, *, text):
	chance = randint(1, 100) / 10
	answers = [f'хуй знает, где {chance} / 10', f'мб {chance} / 10', f'ебать че за вопросы {chance} / 10']
	if text.lower() == "поднятие уровня в одиночку" or text.lower() == "solo leveling":
		for i in range(15, 40):
			await ctx.send(f"{randint(i, 1000)}/10")

		await ctx.send("блять я хуй знает, я цифр таких не знаю")
	elif randint(1, 100) == 1:
		await ctx.send("11 / 10 нахуй")
	else:
		await ctx.send(choice(answers))

@bot.command()
async def когда(ctx, *, text):
	month = randint(1,12)
	mon_name = name_month[month-1]
	interval = int()
	if randint(1,4) == 1:
		interval = 2100
	else:
		interval = 2030

	yeare = randint(2022, interval)
	days = day_in_month[month]
	day = randint(1,days)
	if randint(1,10) == 1:
		await ctx.send('никогда блять')
	else:
		await ctx.send(f'{day} {mon_name} {yeare} года')

	await quest(ctx.message)


@bot.command()
async def блэкджек(ctx, oper, text = None):
	if oper == 'ставка':
		await ctx.send((randint(10,150) // 5) * 5)
		while True:
			msg = await bot.wait_for('message', check = lambda m: m.channel == ctx.channel and m.author.id == ctx.author.id)
			if msg.content.split()[0] == 'берешь' or msg.content.split()[0] == 'бёрешь':
				num = msg.content.split()[1]
				num = 21 - int(num)
				ans = str
				if num < 5:
					if num == 3:
						a = randint(1, 15)
						if a == 1:
							ans = 'да'
						else:
							ans = 'нет'
					elif num == 2:
						a = randint(1, 15)
						if a == 1:
							ans = 'да'
						else:
							ans = 'нет'
					elif num == 1:
						a = randint(1, 20)
						if a == 1:
							ans = 'да'
						else:
							ans = 'нет'
					elif num == 0:
						ans = 'Ты че ебанулся, нет кшн'
					ans = 'нет'
				elif num <= 6 and num > 4:  # от 15 до 17
					if randint(1, 2) == 2:
						ans = 'да'
					else:
						ans = 'нет'
				else:  # остальное
					if num == 0:
						ans = 'ебанулся? нет кшн'
					else:
						if randint(1, 15) == 15:
							ans = 'нет'
						else:
							ans = 'да'

				await ctx.send(ans)

			elif msg.content.split()[0] == 'результат' or msg.content.split()[0] == 'Результат':
				if msg.content.split()[1] == 'win':
					await ctx.send('Юхууу')
				elif msg.content.split()[1] == 'lose':
					await  ctx.send('Грустно')
				break


@bot.command()
async def монополия(ctx):
	await ctx.send('я хатов')
	while True:
		msg = await bot.wait_for('message', check = lambda m: m.channel == ctx.channel and m.author.id == ctx.author.id)
		if msg.content == 'ходи' or msg.content.split()[0] == 'ходи':
			await ctx.send(randint(2,12))
		elif msg.content == 'покупаешь' or msg.content.split()[0] == 'покупаешь':
			if randint(1,10) in range(1,4):
				await ctx.send('нет')
			else:
				await ctx.send('да')
		elif msg.content == 'стоп игра':
			break

async def stop_casino(channel, dbname, user_id, lose_state, max_wins, all_wins, exp_casino, tryes, bd_try):
	channel = bot.get_channel(channel)
	await channel.send('надеюсь в следующий раз играть будем со ставками')
	emb = discord.Embed(title='Результаты сессии казино', color=0xbbff00)
	emb.add_field(name='рекорд за эту сессию', value=f'{max_wins}', inline=False)
	emb.set_thumbnail(url='https://cdn.discordapp.com/attachments/896752165899616257/933217543521460304/img_557881.png')
	emb.add_field(name='всего побед в сессии', value=f'{all_wins}', inline=False)
	emb.add_field(name='полученый опыт', value=f'{exp_casino}', inline=False)
	lose_state_1 = 0

	for i in lose_state:
		lose_state_1 += i

	if lose_state_1 != 0:
		lose_state_2 = int(lose_state_1 / len(lose_state))
		print(lose_state_2)

	emb.add_field(name='всего попыток', value=f'{tryes}', inline=False)
	await channel.send(embed=emb)

	if all_wins >= 2:
		if round(lose_state_2) >= 17:
			await give_ach('master_lose_2', user_id, dbname, channel)

	if tryes > 10:
		if round(lose_state_2) < 5:
			await give_ach('lucky_player', dbname, user_id, channel)

	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""SELECT user_id FROM achivs WHERE user_id = ?""", (user_id,))
		if cur.fetchone() is None:
			randomC = randint(1, 10)
			cur.execute("""INSERT INTO achivs(user_id, color) VALUES (?, ?)""", (user_id, randomC,))
		cur.execute("""SELECT most_wins_casino FROM achivs WHERE user_id = ?""", (user_id,))
		if cur.fetchone()[0] < max_wins:
			cur.execute("""UPDATE achivs SET most_wins_casino = ? WHERE user_id = ?""", (max_wins, user_id))

		cur.execute("""SELECT tryes FROM permissions_casino WHERE user_id = ?""", (user_id,))
		if cur.fetchone() is None:
			cur.execute("""INSERT INTO permissions_casino(user_id, tryes, perm) VALUES(?, ?, False)""", (user_id, bd_try,))

		cur.execute("""UPDATE permissions_casino SET tryes = ? WHERE user_id = ?""", (bd_try, user_id))

	await give_exp(exp_casino, user_id, channel.guild, channel.id)

	if max_wins >= 5:
		await channel.send(f'{max_wins} побед подряд. Я хуееею блять. Иди лотерейный билетик купи сука везучая')
		await give_ach('luck_casino', user_id, dbname, channel.id)

	global play_casino
	global channel_casino
	play_casino = False
	channel_casino = 0

def tryes_bd(dbname, user_id):
	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""SELECT user_id FROM achivs WHERE user_id = ?""", (user_id,))
		if cur.fetchone() is None:
			randomC = randint(1, 10)
			cur.execute("""INSERT INTO achivs(user_id, color) VALUES (?, ?)""", (user_id, randomC,))
		cur.execute("""SELECT tryes FROM permissions_casino WHERE user_id = ?""", (user_id,))
		a = cur.fetchone()[0]
		return a

casino_channels = []
casino_players = []

@bot.command()
async def казино1(ctx):
	mess_count = 1
	global casino_channels
	global casino_players
	user_id = ctx.author.id
	dbname = 'database/' + ctx.guild.name + '_achivs.db'

	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""CREATE TABLE IF NOT EXISTS permissions_casino(user_id INTEGER, tryes INTEGER, perm BOOL)""")

	channel = ctx.channel.id
	if channel not in casino_channels:
		if await get_perm(user_id, dbname) == True:
			casino_players.append(user_id)
			casino_channels.append(channel)
			exp_casino = 0
			win = 0
			all_wins = 0
			max_wins = 0
			tryes = 0
			lose = 0
			lose_state = []
			stupid = 0
			bd_try = tryes_bd(dbname, user_id)

			global play_casino
			global channel_casino
			play_casino = True
			channel_casino = ctx.channel.id
			emb_c = discord.Embed(title='Правила казино', color=0x008bff, description='попробуй угадать число от 1 до 10. После сообщений бота вводите число')
			await ctx.send(embed = emb_c)
			await ctx.send('Введите число')

			while True:
				try:
					msg = await bot.wait_for('message', check=lambda m: m.channel == ctx.channel and m.author.id == ctx.author.id, timeout=120)
					mess_count += 1
					a = randint(1,10)
					if msg.content.lower() == 'стоп':
						casino_channels.remove(channel)
						casino_players.remove(user_id)
						await ctx.channel.purge(limit=mess_count)
						await stop_casino(channel, dbname, user_id, lose_state, max_wins, all_wins, exp_casino, tryes, bd_try)
						break

					else:
						try:
							if int(msg.content) in range(1,11):
								if int(msg.content) == a:
									win += 1
									lose_state.append(lose)
									lose = 0
									if win > 1:
										exp_casino += 300

									all_wins += 1
									exp_casino += 150
									await ctx.send(f'вы выиграли. число побед подряд: {win}')
									await ctx.send(f'Общее число побед: {all_wins}')
									await ctx.send('го некст')
									mess_count += 3
									if win > max_wins:
										max_wins = win
								else:
									win = 0
									lose += 1
									if lose >= 20:
										await give_ach('master_lose', user_id, dbname, channel)

									await ctx.send(f'лох, было {a}')
									await ctx.send('го некст')
									mess_count += 2

								tryes += 1
								stupid = 0
								bd_try += 1

								if tryes >= 75:
									await give_ach('azart_player', user_id, dbname, channel)

								if bd_try >= 150:
									await ctx.send('Лимит попыток исчерпан')
									mess_count += 1
									casino_channels.remove(channel)
									casino_players.remove(user_id)
									await stop_casino(channel, dbname, user_id, lose_state, max_wins, all_wins, exp_casino,tryes, bd_try)
									break

							else:
								stupid += 1
								if randint(1,2) == 1:
									mess_count += 1
									await ctx.send('число не входит интервал')
								else:
									mess_count += 1
									await ctx.send('Долбаеб? Написано же от 1 до 10 блять')
								if stupid >= 15:
									await give_ach('stupid_player', user_id, dbname, channel)

								elif stupid >= 20:
									await stop_casino(channel, dbname, user_id, lose_state, max_wins, all_wins, exp_casino,tryes, bd_try)

						except ValueError:
							stupid += 1
							if randint(1,2) == 1:
								mess_count += 1
								await ctx.send('Ты написал что-то не относящееся к казино')
							else:
								mess_count += 1
								await ctx.send('Бля пиши плз то что входит в программу казино')
							if stupid >= 15:
								await give_ach('stupid_player', user_id, dbname, channel)

				except asyncio.TimeoutError:
					casino_channels.remove(channel)
					casino_players.remove(user_id)
					await stop_casino(channel, dbname, user_id, lose_state, max_wins, all_wins, exp_casino, tryes, bd_try)
					return
		else:
			await ctx.send('вы исчерпали лимит попыток')

	else: await ctx.send('Похоже в этом канале уже идет сессия казино')


async def stop_casino_2(channel, dbname, user_id, lose_state, max_wins, all_wins, exp_casino, tryes, bd_try):
	channel = bot.get_channel(channel)
	await channel.send('Надеюсь донат скоро завезут')
	emb = discord.Embed(title='Результаты сессии казино', color=0xbbff00)
	emb.add_field(name='рекорд за эту сессию', value=f'{max_wins}', inline=False)
	emb.set_thumbnail(url='https://cdn.discordapp.com/attachments/896752165899616257/933217543521460304/img_557881.png')
	emb.add_field(name='всего побед в сессии', value=f'{all_wins}', inline=False)
	vb = str
	v = str
	if exp_casino >= 0:
		vn = 'получено опыта'
		v = str(exp_casino)
	else:
		vn = 'потеряно опыта'
		v = str(exp_casino).split("-")[1]

	emb.add_field(name=vn, value=f'{v}', inline=False)
	lose_state_1 = 0

	for i in lose_state:
		lose_state_1 += i

	lose_state_2 = 0

	if lose_state_1 != 0:
		lose_state_2 = int(lose_state_1 / len(lose_state))


	emb.add_field(name='всего попыток', value=f'{tryes}', inline=False)
	await channel.send(embed=emb)

	if all_wins >= 2 and round(lose_state_2) >= 17:
		await give_ach('master_lose_2', user_id, dbname, channel.id)

	if tryes > 10 and round(lose_state_2) < 5:
		await give_ach('lucky_player', dbname, user_id, channel.id)

	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""SELECT user_id FROM achivs WHERE user_id = ?""", (user_id,))
		if cur.fetchone() is None:
			randomC = randint(1, 10)
			cur.execute("""INSERT INTO achivs(user_id, color) VALUES (?, ?)""", (user_id, randomC,))
		cur.execute("""SELECT most_wins_casino FROM achivs WHERE user_id = ?""", (user_id,))
		if cur.fetchone()[0] < max_wins:
			cur.execute("""UPDATE achivs SET most_wins_casino = ? WHERE user_id = ?""", (max_wins, user_id))

		cur.execute("""SELECT tryes FROM permissions_casino WHERE user_id = ?""", (user_id,))
		if cur.fetchone() is None:
			cur.execute("""INSERT INTO permissions_casino(user_id, tryes, perm) VALUES(?, ?, False)""", (user_id, bd_try,))

		cur.execute("""UPDATE permissions_casino SET tryes = ? WHERE user_id = ?""", (bd_try, user_id))

	await up_exp(user_id, dbname, exp_casino, channel.id)

	if max_wins >= 5:
		await channel.send(f'{max_wins} побед подряд. Я хуееею блять. Иди лотерейный билетик купи сука везучая')
		await give_ach('luck_casino', user_id, dbname, channel.id)

	global play_casino
	global channel_casino
	play_casino = False
	channel_casino = 0

@bot.command()
async def казино2(ctx):
	mess_count = 1
	user_id = ctx.author.id
	dbname = 'database/' + ctx.guild.name + '_achivs.db'
	global casino_channels
	global casino_players
	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""CREATE TABLE IF NOT EXISTS permissions_casino(user_id INTEGER, tryes INTEGER, perm BOOL)""")

	channel = ctx.channel.id

	if channel not in casino_channels:
		if await get_perm(user_id, dbname) == True:
			casino_players.append(user_id)
			casino_channels.append(channel)
			win = 0
			all_wins = 0
			max_wins = 0
			tryes = 0
			lose = 0
			lose_state = []
			stupid = 0
			bet = 10
			bet_exp = get_exp(user_id, dbname)
			bet_exp_1 = get_exp(user_id, dbname)
			bd_try = tryes_bd(dbname, user_id)

			global play_casino
			global channel_casino
			play_casino = True
			channel_casino = ctx.channel.id
			emb_c = discord.Embed(title='Правила казино', color=0x008bff, description='попробуй угадать число от 1 до 10. После сообщений бота вводите число. Ставка по умолчанию 10 опыта. Для обновления напишите "ставка *ЧИСЛО*". Для выхода напишите стоп')
			await ctx.send(embed = emb_c)
			await ctx.send('Введите число')

			while True:
				try:
					msg = await bot.wait_for('message', check=lambda m: m.channel == ctx.channel and m.author.id == ctx.author.id, timeout=120)
					mess_count+=1
					a = randint(1,10)
					if msg.content.lower() == 'стоп':
						bet_exp -= bet_exp_1
						casino_channels.remove(channel)
						casino_players.remove(user_id)
						await ctx.channel.purge(limit = mess_count)
						await stop_casino_2(channel, dbname, user_id, lose_state, max_wins, all_wins, bet_exp, tryes, bd_try)
						break

					elif msg.content.lower().split()[0] == 'ставка':
						try:
							n = int(msg.content.lower().split()[1])
							if n >= 0:
								bet = n
								await ctx.send(f'Установлено значение ставки {bet}')
							else: await ctx.send('Недопустимое значение ставки')

						except ValueError:
							await ctx.send('Ты какую-то хуйню написал, а не ставку')

						except IndexError:
							await ctx.send(f'Текущая ставка {bet}')

						mess_count += 1

					elif msg.content.lower() == 'баланс':
						mess_count += 1
						await ctx.send(bet_exp)
					else:
						try:
							if int(msg.content) in range(1,11):
								if bet <= bet_exp:
									if int(msg.content) == a:
										win += 1
										lose_state.append(lose)
										lose = 0

										if win == 1:
											bet_exp += bet * 5
										elif win == 2:
											bet_exp += int(round(bet * 7.5))
										elif win == 3:
											bet_exp += bet * 10
										elif win == 4:
											bet_exp += bet * 20
										elif win >= 5:
											bet_exp += bet * 45

										all_wins += 1
										await ctx.send(f'вы выиграли. число побед подряд: {win}')
										await ctx.send(f'Общее число побед: {all_wins}')
										await ctx.send('го некст')
										mess_count += 3
										if win > max_wins:
											max_wins = win
									else:
										win = 0
										lose += 1
										bet_exp -= bet
										if lose >= 20:
											await give_ach('master_lose', user_id, dbname, channel)

										await ctx.send(f'лох, было {a}')
										await ctx.send('го некст')
										mess_count += 2

									tryes += 1
									stupid = 0
									bd_try += 1

									if tryes >= 75:
										await give_ach('azart_player', user_id, dbname, channel)

									if bd_try >= 150:
										await ctx.send('Лимит попыток исчерпан')
										mess_count += 1
										bet_exp -= bet_exp_1
										casino_channels.remove(channel)
										casino_players.remove(user_id)
										await stop_casino_2(channel, dbname, user_id, lose_state, max_wins, all_wins, bet_exp,tryes, bd_try)
										break

								else:
									await ctx.send('недостаточно средств')
									mess_count += 1
							else:
								stupid += 1
								if randint(1,2) == 1:
									await ctx.send('число не входит интервал')
									mess_count += 1
								else:
									await ctx.send('Долбаеб? Написано же от 1 до 10 блять')
									mess_count += 1
								if stupid >= 15:
									await give_ach('stupid_player', user_id, dbname, channel)

								elif stupid >= 20:
									await stop_casino_2(channel, dbname, user_id, lose_state, max_wins, all_wins, bet_exp,tryes, bd_try)
						except ValueError:
							stupid += 1
							if randint(1,2) == 1:
								await ctx.send('Ты написал что-то не относящееся к казино')
								mess_count += 1
							else:
								await ctx.send('Бля пиши плз то что входит в программу казино')
								mess_count += 1
							if stupid >= 15:
								await give_ach('stupid_player', user_id, dbname, channel)
				except asyncio.TimeoutError:
					casino_channels.remove(channel)
					casino_players.remove(user_id)
					await stop_casino_2(channel, dbname, user_id, lose_state, max_wins, all_wins, bet_exp, tryes, bd_try)
					return
		else:
			await ctx.send('вы исчерпали лимит попыток')
			mess_count += 1
	else: await ctx.send('Похоже в этом канале уже идет сессия казино')

@bot.command()
async def статус(ctx, user: discord.Member = None):
	user_id = int
	user_name = str
	dbname = 'database/' + ctx.guild.name + '_achivs' + '.db'
	dbname_2 = 'database/' + ctx.guild.name + '.db'
	channel = ctx.channel.id
	url = str
	play = 0
	warns = 0
	bans = 0
	name = str
	try:
		if user is None:
			user_id = ctx.author.id
			user_name = ctx.author.name
			name = ctx.author.name
			if ctx.author.nick is None:
				user_name = ctx.author.name
			else:
				user_name = ctx.author.nick
			url = ctx.author.avatar_url
		else:
			user_id = user.id
			name = user.name
			if user.nick is None:
				user_name = user.name
			else:
				user_name = user.nick
			url = user.avatar_url

	except AttributeError:
		name = 'хз имя не определяется'
	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""CREATE TABLE IF NOT EXISTS permissions_casino(user_id INTEGER, tryes INTEGER, perm BOOL)""")

	with sqlite3.connect(dbname_2) as db:
		cursor = db.cursor()
		cursor.execute("""SELECT warn FROM members WHERE id = ? """, (user_id,))
		if cursor.fetchone() is None:
			name = user_name
			i = 0
			cursor.execute("""INSERT INTO members (id, name, warn) VALUES(?, ?, ?)""", (user_id, name, i))
		cursor.execute("""SELECT warn FROM members WHERE id = ? """, (user_id,))
		i = cursor.fetchone()
		warns = i[0]

	with sqlite3.connect(dbname_2) as db:
		cur = db.cursor()
		cur.execute("""CREATE TABLE IF NOT EXISTS bans(id INTEGER, name TEXT, ban INTEGER)""")
		cur.execute("""SELECT ban FROM bans WHERE id = ?""", (user_id,))
		if cur.fetchone() is None:
			cur.execute("""INSERT INTO bans(id, name, ban) VALUES (?, ?, 0)""", (user_id, name,))

		cur.execute("""SELECT ban FROM bans WHERE id = ?""", (user_id,))

		bans = cur.fetchone()[0]


	if user is None:
		user_id = ctx.author.id
		user_name = ctx.author.name
		if ctx.author.nick is None:
			user_name = ctx.author.name
		else:
			user_name = ctx.author.nick
		url = ctx.author.avatar_url
	else:
		user_id = user.id
		if user.nick is None:
			user_name = user.name
		else:
			user_name = user.nick
		url = user.avatar_url

	exp = int
	lvl = int
	achiv_count = int
	most_wins = int
	color = str
	voice_t = str
	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""SELECT exp FROM achivs WHERE user_id = ?""", (user_id,))
		if cur.fetchone() is None:
			randomC = randint(1, 10)
			cur.execute("""INSERT INTO achivs(user_id, color) VALUES (?, ?)""", (user_id, randomC,))

		cur.execute("""SELECT exp FROM achivs WHERE user_id = ?""", (user_id,))
		exp = cur.fetchone()[0]
		cur.execute("""SELECT lvl FROM achivs WHERE user_id = ?""", (user_id,))
		lvl = cur.fetchone()[0]
		cur.execute("""SELECT most_wins_casino FROM achivs WHERE user_id = ?""", (user_id,))
		most_wins = cur.fetchone()[0]
		cur.execute("""SELECT color FROM achivs WHERE user_id = ?""", (user_id,))
		c_check = cur.fetchone()[0]

		color = user_colors[int(c_check)]

		cur.execute("""SELECT voice FROM achivs WHERE user_id = ?""", (user_id,))
		v_check = int(cur.fetchone()[0])
		#print(v_check)
		v_check = v_check // 60
		#print(v_check)
		if v_check == 0:
			voice_t = '00:00'
		else:
			hour = v_check // 60
			minut = v_check % 60
			if hour < 10:
				hour = f'0{hour}'
			if minut < 10:
				minut = f'0{minut}'
			voice_t = f'{hour}:{minut}'

		list = []
		cur.execute("""SELECT blm, sus_dance, free_time, ucraine, pupa, biba, cenz, net_pidor, pidor_full, 
					da_pizda, russian_game, hikki, money_1, money_2, bebra, anton, amogus, luck_casino, master_lose,
					master_lose_2, azart_player, lucky_player, stupid_player, russia_vp, lh_daz, motivate, hui_na, cookie, gop 
					FROM achivs
					WHERE user_id = ?""", (user_id,))
		list1 = cur.fetchone()
		for i in list1:
			list.append(i)

		achiv_count = list.count(1)

		cur.execute("""SELECT tryes FROM permissions_casino WHERE user_id = ?""", (user_id,))

		if cur.fetchone() is None:
			cur.execute("""INSERT INTO permissions_casino(user_id, tryes, perm) VALUES (?, 0, True)""", (user_id,) )

		cur.execute("""SELECT tryes FROM permissions_casino WHERE user_id = ?""", (user_id,))
		play = cur.fetchone()[0]

	emb = discord.Embed(title=f'Статус {user_name}', color=color)
	emb.set_thumbnail(url=url)
	emb.add_field(name=f'lvl {lvl}', value=f'Опыт {exp} / {lvls[lvl]} | в воисе {voice_t}', inline=False)
	emb.add_field(name='Рекорд в казино', value=most_wins, inline=True)
	# emb.add_field(name=r'\u200', value='\u200', inline=True)
	emb.add_field(name='Игр в казино', value=f'{play}/150', inline=True)
	emb.add_field(name='Собранные достижения', value=f'{achiv_count}/29', inline=False)
	emb.add_field(name='Предупреждения: ', value=warns, inline=True)
	emb.add_field(name='Баны: ', value=bans, inline=True)

	await ctx.send(embed=emb)


@bot.command()
async def лидеры(ctx):
	top_emoji_list = {
		1: '🥇',
		2: '🥈',
		3: '🥉',
	}
	async with ctx.channel.typing():
		dbname = 'database/' + ctx.guild.name + '_achivs.db'
		members_exp = []
		members = {}
		lvls_1 = {}
		with sqlite3.connect(dbname) as db:
			cur = db.cursor()
			cur.execute("""SELECT user_id FROM achivs""")
			users = cur.fetchall()
			#print(users)
			cur.execute("""SELECT exp FROM achivs""")
			exp_fetch = cur.fetchall()
			#print(exp_fetch)
			cur.execute("""SELECT lvl FROM achivs""")
			lvls_0 = cur.fetchall()
			#print(lvls_0)
			n = 0
			for i in users:
				if n == 40:
					break
				user_id = i[0]
				exp_0 = 0
				for a in range(2, lvls_0[n][0] + 1):
					exp_0 += lvls[a - 1]

				exp_0 += exp_fetch[n][0]
				members_exp.append(exp_0)
				members[exp_0] = user_id
				lvls_1[user_id] = lvls_0[n][0]
				n += 1
				#print(user_id, ' ', exp_0)

			#print(members)
			members_exp.sort(reverse=True)
			emb = discord.Embed(title=f'Лидеры {ctx.guild.name}', color = 0xff5800)
			n = 0
			n2 = 0
			for i in members_exp:
				n2 += 1
				if n2 == 12:
					break
				#print(f'{members[i]} : {i} exp')
				try:
					n += 1
					mem = await ctx.guild.fetch_member(members[i])
					if mem.nick is None:
						mem = mem.name
					else:
						mem = mem.nick

					if n < 4:
						emb.add_field(name=f'{top_emoji_list[n]} #{mem}', value=f'уровень {lvls_1[members[i]]} | суммарный опыт {i}', inline=False)
					else:
						emb.add_field(name=f'{n}. {mem}', value=f'уровень {lvls_1[members[i]]} | суммарный опыт {i}', inline=False)
				except discord.errors.NotFound:
					n -= 1
					continue

			await ctx.send(embed = emb)


@bot.command()
async def напомни(ctx, tm, *, text):
	h = int(tm.split(':')[0])
	m = int(tm.split(':')[1])
	nh = int(datetime.datetime.now().strftime('%H'))
	nm = int(datetime.datetime.now().strftime('%M'))
	#print(f'nh: {nh}; nm: {nm}')
	if h < nh or (h == nh and m <= nm) or h > 23:
		await ctx.send('пидорское время')
	else:
		minuts1 = m-nm
		all_minuts = minuts1 + (h-nh)*60
		#print(f'время ожидания: {all_minuts} мин')
		await ctx.reply('ок')
		await asyncio.sleep(all_minuts*60)
		await ctx.reply('Ало ебать')


with sqlite3.connect('games/game.db') as db:
	cur = db.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS main(id INTEGER, game TEXT)""")

def get_games(user_id):
	dbname = 'games/game.db'
	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""SELECT game FROM main WHERE id = ?""", (user_id,))
		a = cur.fetchall()
		gameList = []
		for i in a:
			gameList.append(i[0])

		return gameList

def get_party_games(ctx):
	voice = ctx.author.voice
	if voice is None:
		return 'проблемка с воисом'
	else:
		members0 = voice.channel.members
		members = []
		for i in members0:
			members.append(i.id)

		mem_count = len(members)

		#print(mem_count)
		members_games = []
		for i in members:
			members_games.append(get_games(i))

		gama_count = {}

		for i in members_games:
			for c in i:
				try: gama_count[c] += 1
				except KeyError: gama_count[c] = 1

		games = []
		game_ignore = ['Sims', 'MINECRAFT']
		for i in gama_count:
			n = gama_count[i]
			per = n/mem_count*100
			if per <= 70 or i in game_ignore: pass
			else: games.append(i)

		return games

@bot.command()
async def во(ctx, *, text):
	if text == 'что играть':
		games = get_games(ctx.author.id)
		party_games = get_party_games(ctx)
		if party_games == 'проблемка с воисом' or ctx.author.voice is None:
			l = len(games)-1
			await ctx.send(f'хз, может в {games[randint(0, l)]}')

		else:
			await ctx.send(f'хз, может {choice(party_games)}')


bot.run(settings['token'])

a = input()
