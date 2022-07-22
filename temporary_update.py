import os
import sqlite3, shutil

print('Программа копиравания')
dbname = input('Введите имя бд для копироваиня: ')
try: os.remove(f'new_bd/{dbname}')
except: pass
columns = ['lvl', 'exp', 'voice', 'color', 'most_wins_casino', 'blm', 'sus_dance', 'free_time', 'ucraine', 'pupa', 'biba', 'cenz', 'net_pidor', 'pidor_full', 'da_pizda', 'russian_game', 'hikki', 'money_1', 'money_2', 'bebra', 'anton', 'amogus', 'luck_casino', 'master_lose', 'master_lose_2', 'azart_player', 'lucky_player', 'stupid_player', 'russia_vp', 'lh_daz', 'motivate']
new_columns = ['hui_na', 'gop', 'cookie']
new_columns2 = {
    'hui_na': 'BOOL DEFAULT False',
    'gop': 'BOOL DEFAULT False',
    'cookie': 'BOOL DEFAULT False'
}
unical_column = {
    'lvl': 'INTEGER DEFAULT 1',
    'exp': 'INTEGER DEFAULT 0',
    'most_wins_casino': 'INTEGER DEFAULT 0',
    'voice': 'INTEGER DEFAULT 0',
    'color': 'INTEGER DEFAULT 1'
}

users_achiv = {}
shutil.copyfile(dbname, f'new_bd/{dbname}')
dbname = f'new_bd/{dbname}'
with sqlite3.connect(dbname) as db:
    cur = db.cursor()
    cur.execute("""SELECT user_id FROM achivs""")
    users = cur.fetchall()
    print(users)
    for id in users:
        id = id[0]
        users_achiv[id] = {}
        for box in columns:
            cur.execute("""SELECT CASE ? 
            WHEN 'lvl' THEN lvl 
            WHEN 'exp' THEN exp 
            WHEN 'most_wins_casino' THEN most_wins_casino 
            WHEN 'blm' THEN blm 
            WHEN 'sus_dance' THEN sus_dance 
            WHEN 'free_time' THEN free_time 
            WHEN 'ucraine' THEN ucraine 
            WHEN 'pupa' THEN pupa 
            WHEN 'biba' THEN biba 
            WHEN 'cenz' THEN cenz 
            WHEN 'net_pidor' THEN net_pidor 
            WHEN 'pidor_full' THEN pidor_full 
            WHEN 'da_pizda' THEN da_pizda 
            WHEN 'russian_game' THEN russian_game 
            WHEN 'hikki' THEN hikki 
            WHEN 'money_1' THEN money_1 
            WHEN 'money_2' THEN money_2 
            WHEN 'bebra' THEN bebra 
            WHEN 'anton' THEN anton 
            WHEN 'amogus' THEN amogus 
            WHEN 'luck_casino' THEN luck_casino 
            WHEN 'master_lose' THEN master_lose 
            WHEN 'master_lose_2' THEN master_lose_2 
            WHEN 'azart_player' THEN azart_player 
            WHEN 'lucky_player' THEN lucky_player 
            WHEN 'stupid_player' THEN stupid_player 
            WHEN 'russia_vp' THEN russia_vp 
            WHEN 'lh_daz' THEN lh_daz 
            WHEN 'motivate' THEN motivate 
            WHEN 'color' THEN color 
            WHEN 'voice' THEN voice 
            END FROM achivs WHERE user_id = ?""", (box, id,))
            a = cur.fetchone()[0]
            users_achiv[id][box] = a
    print(f'users_achiv: {users_achiv}' )
    cur.execute("""DROP TABLE achivs""")
    creat_command = """CREATE TABLE IF NOT EXISTS achivs(user_id INTEGER, """
    for i in columns:
        try: typeI = unical_column[i]
        except KeyError: typeI = 'BOOL DEFAULT False'

        creat_command = creat_command + f'{i} ' + typeI + ', '

    for i in new_columns:
        print(f'{new_columns.index(i)} : {len(new_columns)}')
        if new_columns.index(i) < len(new_columns)-1:
            creat_command = creat_command + f'{i} ' + new_columns2[i] + ', '
        else:
            creat_command = creat_command + f'{i} ' + new_columns2[i] + ') '
    print(creat_command)

    cur.execute(creat_command)

    for user_id in users:
        user_id = int(user_id[0])
        cur.execute("""INSERT INTO achivs(user_id) VALUES(?)""", (user_id,))

        for i in users_achiv[user_id]:
            box = users_achiv[user_id][i]
            print(f'box: {box}')
            print(f'i: {i}')
            if i == 'lvl':
                cur.execute("""UPDATE achivs SET lvl = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'exp':
                cur.execute("""UPDATE achivs SET exp = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'most_wins_casino':
                cur.execute("""UPDATE achivs SET most_wins_casino = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'blm':
                cur.execute("""UPDATE achivs SET blm = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'sus_dance':
                cur.execute("""UPDATE achivs SET sus_dance = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'free_time':
                cur.execute("""UPDATE achivs SET free_time = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'ucraine':
                cur.execute("""UPDATE achivs SET ucraine = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'pupa':
                cur.execute("""UPDATE achivs SET pupa = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'biba':
                cur.execute("""UPDATE achivs SET biba = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'cenz':
                cur.execute("""UPDATE achivs SET cenz = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'net_pidor':
                cur.execute("""UPDATE achivs SET net_pidor = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'pidor_full':
                cur.execute("""UPDATE achivs SET pidor_full = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'da_pizda':
                cur.execute("""UPDATE achivs SET da_pizda = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'russian_game':
                cur.execute("""UPDATE achivs SET russian_game = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'hikki':
                cur.execute("""UPDATE achivs SET hikki = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'money_1':
                cur.execute("""UPDATE achivs SET money_1 = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'money_2':
                cur.execute("""UPDATE achivs SET money_2 = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'bebra':
                cur.execute("""UPDATE achivs SET bebra = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'anton':
                cur.execute("""UPDATE achivs SET anton = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'amogus':
                cur.execute("""UPDATE achivs SET amogus = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'luck_casino':
                cur.execute("""UPDATE achivs SET luck_casino = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'master_lose':
                cur.execute("""UPDATE achivs SET master_lose = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'master_lose_2':
                cur.execute("""UPDATE achivs SET master_lose_2 = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'azart_player':
                cur.execute("""UPDATE achivs SET azart_player = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'lucky_player':
                cur.execute("""UPDATE achivs SET lucky_player = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'stupid_player':
                cur.execute("""UPDATE achivs SET stupid_player = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'russia_vp':
                cur.execute("""UPDATE achivs SET russia_vp = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'lh_daz':
                cur.execute("""UPDATE achivs SET lh_daz = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'motivate':
                cur.execute("""UPDATE achivs SET motivate = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'color':
                cur.execute("""UPDATE achivs SET color = ? WHERE user_id = ?""", (box, user_id,))
            elif i == 'voice':
                cur.execute("""UPDATE achivs SET voice = ? WHERE user_id = ?""", (box, user_id,))



print(users_achiv)
print(creat_command)
