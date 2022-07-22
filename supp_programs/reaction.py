from discord.ext import commands
from config import settings
import sys
import sqlite3
import time
import asyncio
from discord import utils
from random import randint

pref = ['daz ', '!']
bot = commands.Bot(command_prefix=pref)

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
	print('Дополнительная программа raw_reaction запущена')
	print('')
	print('')


@bot.event
async def on_command_error(ctx, error): pass

import supp_config, test_config


async def add_game(user_id, game):
	dbname = 'C:/Users/user/Desktop/питон/Дазай/games/game.db'
	while True:
		try:
			with sqlite3.connect(dbname) as db:
				cur = db.cursor()
				cur.execute("""SELECT game FROM main WHERE id = ? AND game = ?""", (user_id, game,))
				if cur.fetchone() is None:
					cur.execute("""INSERT INTO main(id, game) VALUES(?, ?)""", (user_id, game,))
					user = await bot.fetch_user(user_id)
					print(f'game {game} added to {user}')
					await user.send(f'добалена игра {game}')

		except:
			print('Error add_game')
			await asyncio.sleep(randint(1, 5))
			continue

		break

async def dell_game(user_id, game):
	dbname = 'C:/Users/user/Desktop/питон/Дазай/games/game.db'
	while True:
		try:
			with sqlite3.connect(dbname) as db:
				cur = db.cursor()
				try:
					cur.execute("""DELETE FROM main WHERE game = ? AND id = ?""", (game, user_id,))
					user = await bot.fetch_user(user_id)
					print(f'game {game} was deleted from {user}')
					await user.send(f'удалена игра {game}')
				except: print(f'Error remove {game} from {user_id}')

		except:
			print('Error dell_game')
			await asyncio.sleep(randint(1, 5))
			continue

		break


@bot.event
async def on_raw_reaction_add(payload):
	channel = bot.get_channel(payload.channel_id)  # получаем объект канала
	message = await channel.fetch_message(payload.message_id)  # получаем объект сообщения
	member = payload.member  # получаем объект пользователя который поставил реакцию
	emoji = str(payload.emoji)
	if payload.message_id == test_config.POST_ID:

		try:
			role = utils.get(message.guild.roles, id=test_config.ROLES[emoji])  # объект выбранной роли (если есть)
			await member.add_roles(role)
			print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))

		except KeyError as e:
			print('[ERROR] KeyError, no role found for ' + emoji)
		except Exception as e:
			print(repr(e))

	elif payload.message_id == test_config.POST_ID_G:
		try:
			# эмоджик который выбрал юзер
			role = utils.get(message.guild.roles, id=test_config.ROLES_G[emoji])  # объект выбранной роли (если есть)

			await member.add_roles(role)
			print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))

		except KeyError as e:
			print('[ERROR] KeyError, no role found for ' + emoji)
		except Exception as e:
			print(repr(e))

	elif payload.message_id == test_config.POST_ID_SH:
		try:
			emoji = str(payload.emoji)  # эмоджик который выбрал юзер
			role = utils.get(message.guild.roles, id=test_config.ROLES_SH[emoji])  # объект выбранной роли (если есть)

			await member.add_roles(role)
			#print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))

		except KeyError as e:
			print('[ERROR] KeyError, no role found for ' + emoji)
		except Exception as e:
			print(repr(e))

	elif payload.message_id == supp_config.POST_ID:
		member = payload.member  # получаем объект пользователя который поставил реакцию
		emoji = str(payload.emoji)
		#print(member)
		#print(emoji)
		user_id = member.id
		if emoji in supp_config.GAMES:
			#print('выдача')
			await add_game(user_id, supp_config.GAMES[emoji])

@bot.event
async def on_raw_reaction_remove(payload):
	channel = bot.get_channel(payload.channel_id)  # получаем id канала
	message = await channel.fetch_message(payload.message_id)  # получаем id сообщения
	user_id = payload.user_id  # по сути эта херня не нужна, но на всякий случай не трож
	member = await (await bot.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
	emoji = str(payload.emoji)
	if payload.message_id == test_config.POST_ID:
		try:
			# эмоджик который выбрал юзер
			role = utils.get(message.guild.roles, id=test_config.ROLES[emoji])  # объект выбранной роли (если есть)

			await member.remove_roles(role)
			#print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))

		except KeyError as e:
			print('[ERROR] KeyError, no role found for ' + emoji)

		except Exception as e:
			print(repr(e))

	elif payload.message_id == test_config.POST_ID_G:
		try:
			emoji = str(payload.emoji)  # эмоджик который выбрал юзер
			role = utils.get(message.guild.roles, id=test_config.ROLES_G[emoji])  # объект выбранной роли (если есть)

			await member.remove_roles(role)
			#print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))


		except KeyError as e:
			print('[ERROR] KeyError, no role found for ' + emoji)

		except Exception as e:
			print(repr(e))

	elif payload.message_id == test_config.POST_ID_SH:
		try:
			emoji = str(payload.emoji)  # эмоджик который выбрал юзер
			role = utils.get(message.guild.roles, id=test_config.ROLES_SH[emoji])  # объект выбранной роли (если есть)

			await member.remove_roles(role)
			#print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))


		except KeyError as e:
			print('[ERROR] KeyError, no role found for ' + emoji)

		except Exception as e:
			print(repr(e))


	if payload.message_id == supp_config.POST_ID:
		member = await (await bot.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)  # получаем объект пользователя который поставил реакцию
		#print(member)
		user_id = member.id
		if str(payload.emoji) in supp_config.GAMES:
			await dell_game(user_id, supp_config.GAMES[str(payload.emoji)])



bot.run(settings['token'])
a = input()
