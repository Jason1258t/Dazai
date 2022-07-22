from discord.ext import commands
from config import settings
import discord, sqlite3, sys, time
from discord import utils
from class_config import settings as cs

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['daz ', '!'], intents=intents)


@commands.has_role(889842559487189002)
@bot.command()
async def suicide(ctx):
	sys.exit()

@commands.has_role(889842559487189002)
@bot.command()
async def re(ctx):
	print('Сейчас это окно закроется')
	time.sleep(3)
	sys.exit()

@bot.event
async def on_ready( ):
	print('Дополнительная программа backupRoles запущена')
	print('')
	print('')



def save_roles(user_id, roles_list, nick, dbname):
	with sqlite3.connect(dbname) as db: db.cursor().execute("""CREATE TABLE IF NOT EXISTS main(user_id INTEGER, roles TEXT, nick TEXT)""")

	text_roles = ''
	for i in roles_list:
		text_roles = f'{text_roles} {i}'

	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""SELECT user_id FROM main WHERE user_id = ?""", (user_id,))
		if cur.fetchone() is None:
			cur.execute("""INSERT INTO main(user_id) VALUES(?)""", (user_id,))

		cur.execute("""UPDATE main SET roles = ? WHERE user_id = ?""", (text_roles, user_id,))
		cur.execute("""UPDATE main SET nick = ? WHERE user_id = ?""", (nick, user_id,))

def get_roles(user_id, dbname):
	with sqlite3.connect(dbname) as db:
		db.cursor().execute("""CREATE TABLE IF NOT EXISTS main(user_id INTEGER, roles TEXT, nick TEXT)""")

	try:
		with sqlite3.connect(dbname) as db:
			cur = db.cursor()
			cur.execute("""SELECT user_id FROM main WHERE user_id = ?""", (user_id,))
			if cur.fetchone() is None:
				cur.execute("""INSERT INTO main(user_id) VALUES(?)""", (user_id,))

			cur.execute("""SELECT roles FROM main WHERE user_id = ?""", (user_id,))
			roles1 = cur.fetchone()[0]
			roles2 = roles1.split()
			cur.execute("""SELECT nick FROM main WHERE user_id = ?""", (user_id,))
			nick = cur.fetchone()[0]
			return [roles2, nick]
	except: pass

@bot.event
async def on_command_error(ctx, error):
    if type(error) == discord.ext.commands.errors.CommandNotFound: pass
    elif type(error) == discord.ext.commands.errors.MissingRequiredArgument: await ctx.send('что-то в команде пропущено')
    elif type(error) == discord.ext.commands.errors.MissingPermissions: await ctx.send('нет прав')
    else:
        print(error)
        print(type(error))


@bot.event
async def on_member_remove(member):
	channel = await bot.fetch_channel(883306033836068936)
	user_id = member.id
	roles_0 = member.roles
	roles = []
	for i in roles_0:
		roles.append(i.id)
	dbname = r'C:\Users\user\Desktop\питон\Дазай\databsase' + f'\{member.guild.name}Backup.db'
	nick = member.name if member.nick is None else member.nick
	save_roles(user_id, roles, nick, dbname)
	if member.guild. id == 883306033307615293:
		await channel.send(f'{member} сыбався')


@bot.event
async def on_member_join(member):
	user_id = member.id
	guild = member.guild
	conf_db = r'C:\Users\user\Desktop\питон\Дазай\database' + f'\{guild.name}_config.db'
	try:
		dbname = r'C:\Users\user\Desktop\питон\Дазай\database' + f'\{guild.name}Backup.db'
		roles = get_roles(user_id, dbname)[0]
		nick = get_roles(user_id, dbname)[1]
		await member.edit(nick=nick)
		for role_id in roles:
			role = utils.get(guild.roles, id=int(role_id))
			if role.name != '@everyone':
				await member.add_roles(role)

	except: pass

	dbname = r'C:\Users\user\Desktop\питон\Дазай\database' + f'\{guild.name}_config.db'
	conf = cs().get_join_settings(dbname)
	channel = conf['channel']
	if channel is not None:
		text = conf['text']
		if '{' in text and '}' in text:
			t1 = text.split('{')[0]
			t2 = text.split('}')[1]
			text = f'{t1} {member} {t2}'
		embed = conf['embed']
		color = int(conf['color'], 16)
		img = conf['img']
		# print(embed, ' ', type(embed))
		channel = bot.get_channel(int(conf['channel']))
		if embed == '1':
			emb = discord.Embed(title=f'{text} {member}', color=color)
			if img is not None:
				try:
					emb.set_image(url=str(img))
				except:
					pass

			await channel.send(embed=emb)

		else:
			await channel.send(text)

	if conf['role'] is not None:
		try:
			role1 = utils.get(guild.roles, id=int(conf['role']))
			await member.add_roles(role1)
		except: print('проблемы с выдачей роли')



	"""
	if guild.id == 883306033307615293:
		role = discord.utils.get(guild.roles, id=967122251545739406)
		print('user join the servers')
		await member.add_roles(role)
		channel = await bot.fetch_channel(883306033836068936)
		embed = discord.Embed(description=f'@{member} добро пожаловать в секту', color=0xffc238)
		embed.set_image(url='https://cdn.discordapp.com/attachments/973998982630109224/974909913660788779/gif.gif')
		await channel.send(embed=embed)

	elif guild.id == 619203526941343754:
		role = discord.utils.get(guild.roles, id=777936848105242705)
		print('user join the shrekotopy')
		await member.add_roles(role)
		channel = await bot.fetch_channel(619203527406780437)
		await channel.send(embed=discord.Embed(description=f'@{member} готовь очко', color=0xffc238))
	"""


@commands.has_permissions(administrator=True)
@bot.command()
async def set_join_channel(ctx):
	id = ctx.channel.id
	dbname = r'C:\Users\user\Desktop\питон\Дазай\database' + f'\{ctx.guild.name}_config.db'
	answer = cs().set_join_settings(dbname, 'channel', id)
	await ctx.send(answer)

@commands.has_permissions(administrator=True)
@bot.command()
async def set_join_text(ctx, *, text):
	dbname = r'C:\Users\user\Desktop\питон\Дазай\database' + f'\{ctx.guild.name}_config.db'
	answer = cs().set_join_settings(dbname, 'text', text)
	await ctx.send(answer)

@commands.has_permissions(administrator=True)
@bot.command()
async def set_join_embed(ctx, *, text):
	if str(text) != 'True' and str(text) != 'False':
		print(text)
		await ctx.send('не правильный аргумент')
		return
	dbname = r'C:\Users\user\Desktop\питон\Дазай\database' + f'\{ctx.guild.name}_config.db'
	answer = cs().set_join_settings(dbname, 'embed', bool(text))
	await ctx.send(answer)

@commands.has_permissions(administrator=True)
@bot.command()
async def set_join_color(ctx, *, text):
	dbname = r'C:\Users\user\Desktop\питон\Дазай\database' + f'\{ctx.guild.name}_config.db'
	try: a = int(text, 16)
	except:
		await ctx.send('кривое значение цвета')
		return
	answer = cs().set_join_settings(dbname, 'color', text)
	await ctx.send(answer)

@commands.has_permissions(administrator=True)
@bot.command()
async def set_join_role(ctx, *, text):
	dbname = r'C:\Users\user\Desktop\питон\Дазай\database' + f'\{ctx.guild.name}_config.db'
	try:
		a = int(text)
		if len(text) < 18:
			await ctx.send('не правильно указана роль')
			return
	except:
		await ctx.send('не правильно указана роль')
		return
	answer = cs().set_join_settings(dbname, 'role', text)
	await ctx.send(answer)

@commands.has_permissions(administrator=True)
@bot.command()
async def set_join_img(ctx, *, text):
	dbname = r'C:\Users\user\Desktop\питон\Дазай\database' + f'\{ctx.guild.name}_config.db'
	answer = cs().set_join_settings(dbname, 'img', text)
	await ctx.send(answer)

@commands.has_permissions(administrator=True)
@bot.command()
async def join_check(ctx):
	dbname = r'C:\Users\user\Desktop\питон\Дазай\database' + f'\{ctx.guild.name}_config.db'
	conf = cs().get_join_settings(dbname)
	channel = conf['channel']
	if channel is not None:
		text = conf['text']
		if '{' in text and '}' in text:
			t1 = text.split('{')[0]
			t2 = text.split('}')[1]
			text = f'{t1} {ctx.author} {t2}'
		embed = conf['embed']
		color = int(conf['color'], 16)
		img = conf['img']
		#print(embed, ' ', type(embed))

		if embed == '1':
			emb = discord.Embed(title=f'{text}', color=color)
			if img is not None:
				try: emb.set_image(url=str(img))
				except: pass

			await ctx.send(embed=emb)

		else: await ctx.send(text)
	else:
		await ctx.send('Не указан канал для приветствий')

bot.run(settings['token'])
a = input()