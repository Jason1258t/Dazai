import sqlite3

class settings:
    def add_spamignore(self, dbname, channel_id):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS spam_ignore(channel INTEGER)""")
            cur.execute("""SELECT channel FROM spam_ignore WHERE channel = ?""", (channel_id,))
            if cur.fetchone() is None:
                cur.execute("""INSERT INTO spam_ignore(channel) VALUES(?)""", (channel_id,))
                return 'канал добавлен'

            else:
                return 'похоже канал уже есть'

    def remove_spamignore(self, dbname, channel_id):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS spam_ignore(channel INTEGER)""")
            cur.execute("""SELECT channel FROM spam_ignore WHERE channel = ?""", (channel_id,))
            if cur.fetchone() is None:
                return 'кажется этого канал и без того нет'

            else:
                cur.execute("""DELETE FROM spam_ignore WHERE channel = ?""", (channel_id,))
                return 'канал удален'

    def set_spam_limit(self, dbname, value):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS spam_limiter(id INTEGER, lim INTEGER DEFAULT 0, alert INTEGER DEFAULT 0, text TEXT)""")

            cur.execute("""SELECT id FROM spam_limiter WHERE id = 1""")

            if cur.fetchone() is None:
                print('None')
                cur.execute("""INSERT INTO spam_limiter(id, lim, alert) VALUES(1, 0, 0)""")

            cur.execute("""UPDATE spam_limiter SET lim = ?""", (value,))
            return 'лимит спама изменен'

    def set_spam_alert(self, dbname, value):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS spam_limiter(id INTEGER, lim INTEGER DEFAULT 0, alert INTEGER DEFAULT 0, text TEXT)""")

            cur.execute("""SELECT id FROM spam_limiter WHERE id = 1""")

            if cur.fetchone() is None:
                print('None')
                cur.execute("""INSERT INTO spam_limiter(id, lim, alert) VALUES(1, 0, 0)""")

            cur.execute("""UPDATE spam_limiter SET alert = ?""", (value,))
            return 'по идее теперь допустимый предел спама изменен'

    def set_spam_text(self, dbname, text):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS spam_limiter(id INTEGER, lim INTEGER DEFAULT 0, alert INTEGER DEFAULT 0, text TEXT)""")

            cur.execute("""SELECT id FROM spam_limiter WHERE id = 1""")

            if cur.fetchone() is None:
                print('None')
                cur.execute("""INSERT INTO spam_limiter(id, lim, alert) VALUES(1, 0, 0)""")

            cur.execute("""UPDATE spam_limiter SET text = ?""", (text,))
            return 'по идее теперь текст спама изменен'

    def get_spam_limit(self, dbname):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS spam_limiter(id INTEGER, lim INTEGER DEFAULT 0, alert INTEGER DEFAULT 0, text TEXT)""")

            cur.execute("""SELECT id FROM spam_limiter WHERE id = 1""")

            if cur.fetchone() is None:
                print('None')
                cur.execute("""INSERT INTO spam_limiter(id, lim, alert) VALUES(1, 0, 0)""")

            cur.execute("""SELECT lim FROM spam_limiter""")
            limit = cur.fetchone()[0]

            cur.execute("""SELECT alert FROM spam_limiter""")
            alert = cur.fetchone()[0]

            cur.execute("""SELECT text FROM spam_limiter""")
            try: text = cur.fetchone()[0]
            except: text = None

            return {'limit': limit, 'alert': alert, 'text': text}

            

    def get_spamignore(self, dbname):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS spam_ignore(channel INTEGER)""")
            cur.execute("""SELECT channel FROM spam_ignore""")
            f = cur.fetchall()
            l = []
            for i in f:
                l.append(i[0])

            return l

    def add_banwords_ignore(self, dbname, id, usorchan):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS banwords_ignore(channel INTEGER DEFAULT 0, user INTEGER DEFAULT 0)""")
            if usorchan == 'us':
                cur.execute("""SELECT user FROM banwords_ignore WHERE user = ?""", (id,))
                if cur.fetchone() is None:
                    cur.execute("""INSERT INTO banwords_ignore(user) VALUES(?)""", (id,))
                    return 'пользователь добавлен в список игнорирования банвордов'

                else:
                    return 'похоже пользователь уже в списке игнорирования банвордов'

            elif usorchan == 'chan':
                cur.execute("""SELECT channel FROM banwords_ignore WHERE channel = ?""", (id,))
                if cur.fetchone() is None:
                    cur.execute("""INSERT INTO banwords_ignore(channel) VALUES(?)""", (id,))
                    return 'канал добавлен в список игнорирования банвордов'

                else:
                    return 'похоже канал уже в списке игнорирования банвордов'


    def remove_banwords_ignore(self, dbname, id, usorchan):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS banwords_ignore(channel INTEGER DEFAULT 0, user INTEGER DEFAULT 0)""")
            if usorchan == 'us':
                cur.execute("""SELECT user FROM banwords_ignore WHERE user = ?""", (id,))
                if cur.fetchone() is None:
                    return 'похоже пользователя и так нет списке игнорирования банвордов'

                else:
                    cur.execute("""DELETE FROM banwords_ignore WHERE user = ?""", (id,))
                    return 'пользователь удален из списка игнорирования банвордов'


            elif usorchan == 'chan':
                cur.execute("""SELECT channel FROM banwords_ignore WHERE channel = ?""", (id,))
                if cur.fetchone() is None:
                    return 'похоже канал и так нет списке игнорирования банвордов'
                else:
                    cur.execute("""DELETE FROM banwords_ignore WHERE channel = ?""", (id,))
                    return 'канал удален из списка игнорирования банвордов'



    def get_word_ignore(self, dbname):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS banwords_ignore(channel INTEGER DEFAULT 0, user INTEGER DEFAULT 0)""")
            cur.execute("""SELECT channel FROM banwords_ignore WHERE channel <> 0""")
            channels0 = cur.fetchall()
            channels = []
            for i in channels0:
                channels.append(i[0])

            cur.execute("""SELECT user FROM banwords_ignore WHERE user <> 0""")
            users0 = cur.fetchall()
            users = []
            for i in users0:
                users.append(i[0])

            #print({'channels': channels, 'users': users})
            return {'channels': channels, 'users': users}

    def set_join_settings(self, dbname, parametr, value):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            try:
                cur.execute("""SELECT name FROM join_settings""")
            except sqlite3.OperationalError:
                cur.execute("""CREATE TABLE IF NOT EXISTS join_settings(name TEXT, value TEXT DEFAULT NULL)""")
                cur.execute("""INSERT INTO join_settings(name) VALUES(?)""", ('channel',))
                cur.execute("""INSERT INTO join_settings(name) VALUES(?)""", ('text',))
                cur.execute("""INSERT INTO join_settings(name) VALUES(?)""", ('default_role',))
                cur.execute("""INSERT INTO join_settings(name) VALUES(?)""", ('embed',))
                cur.execute("""INSERT INTO join_settings(name, value) VALUES(?, ?)""", ('color', 'FFFFFF',))
                cur.execute("""INSERT INTO join_settings(name) VALUES(?)""", ('img',))

        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            if parametr == 'channel':
                cur.execute("""UPDATE join_settings SET value = ? WHERE name = 'channel'""", (value,))
                return 'канал добавлен как канал для приветствий'
            elif parametr == 'text':
                cur.execute("""UPDATE join_settings SET value = ? WHERE name = 'text'""", (value,))
                return 'текст добавлен в сообщение для приветствий'
            elif parametr == 'embed':
                cur.execute("""UPDATE join_settings SET value = ? WHERE name = 'embed'""", (value,))
                return 'настройка embed изменена'
            elif parametr == 'color':
                cur.execute("""UPDATE join_settings SET value = ? WHERE name = 'color'""", (value,))
                return 'цвет embed установлен'
            elif parametr == 'img':
                cur.execute("""UPDATE join_settings SET value = ? WHERE name = 'img'""", (value,))
                return 'картинка embed установлена'

            elif parametr == 'role':
                cur.execute("""UPDATE join_settings SET value = ? WHERE name = 'default_role'""", (value,))
                return 'роль вроде добавлена как роль по умолчанию для всех кто присоединится к серверу'



    def get_join_settings(self, dbname):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            try:
                cur.execute("""SELECT name FROM join_settings""")
            except sqlite3.OperationalError:
                cur.execute("""CREATE TABLE join_settings(name TEXT, value TEXT DEFAULT NULL)""")
                cur.execute("""INSERT INTO join_settings(name) VALUES(?)""", ('channel',))
                cur.execute("""INSERT INTO join_settings(name) VALUES(?)""", ('text',))
                cur.execute("""INSERT INTO join_settings(name) VALUES(?)""", ('default_role',))
                cur.execute("""INSERT INTO join_settings(name, value) VALUES(?, False)""", ('embed',))
                cur.execute("""INSERT INTO join_settings(name, value) VALUES(?, ?)""", ('color', 'FFFFFF',))
                cur.execute("""INSERT INTO join_settings(name) VALUES(?)""", ('img',))

        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute("""SELECT value FROM join_settings WHERE name = 'channel'""")
            try: channel = cur.fetchone()[0]
            except: channel = None

            cur.execute("""SELECT value FROM join_settings WHERE name = 'text'""")
            try: text = cur.fetchone()[0]
            except: text = None

            cur.execute("""SELECT value FROM join_settings WHERE name = 'default_role'""")
            try: role = cur.fetchone()[0]
            except: role = None

            cur.execute("""SELECT value FROM join_settings WHERE name = 'embed'""")
            emb = cur.fetchone()[0]

            cur.execute("""SELECT value FROM join_settings WHERE name = 'color'""")
            color = cur.fetchone()[0]

            cur.execute("""SELECT value FROM join_settings WHERE name = 'img'""")
            try: img_url = cur.fetchone()[0]
            except: img_url = None

            #print(emb)
            return {'channel': channel, 'text': text, 'role': role, 'embed': emb, 'color': color, 'img': img_url}


    def add_ColorRole(self, dbname, name):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS color_roles(name TEXT)""")
            cur.execute("""SELECT name FROM color_roles WHERE name = ?""", (name,))
            if cur.fetchone() is None:
                cur.execute("""INSERT INTO color_roles(name) VALUES(?)""", (name,))
                return 'роль добавлена'

            else:
                return 'роль уже есть'

    def del_ColorRole(self, dbname, name):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS color_roles(name TEXT)""")
            cur.execute("""SELECT name FROM color_roles WHERE name = ?""", (name,))
            if cur.fetchone() is None:
                return 'роли и так нет'
            else:
                cur.execute("""DELETE FROM color_roles WHERE name = ?""", (name,))
                return 'роль удалена'

    def get_ColorRoles(self, dbname):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS color_roles(name TEXT)""")
            cur.execute("""SELECT name FROM color_roles""")
            fa = cur.fetchall()
            if fa is None:
                return None
            else:
                l = []
                for rolename in fa: l.append(rolename[0])
                return l

    def set_range_role(self, dbname, lvl, role_id, name):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS range_roles(role_id INTEGER, lvl INTEGER)')
            cur.execute(f'SELECT role_id FROM range_roles WHERE role_id = {int(role_id)}')
            if cur.fetchone() is None:
                cur.execute(f'INSERT INTO range_roles(role_id, lvl) VALUES({int(role_id)}, {int(lvl)})')
                return f'роль {name} добавлена как награда за {lvl} уровень'
            else:
                cur.execute(f'UPDATE range_roles SET lvl = {lvl} WHERE role_id = {role_id}')
                return f'роль **{name}** уже занесена. уровень получения роли изменен на {lvl}'

    def del_range_role(self, dbname, role_id, name):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS range_roles(role_id INTEGER, lvl INTEGER)')
            cur.execute(f'SELECT role_id FROM range_roles WHERE role_id = {int(role_id)}')
            if cur.fetchone() is None:
                return f'роль **{name}** не находится в списке автоматических наград'

            else:
                cur.execute(f'DELETE FROM range_roles WHERE role_id = {int(role_id)}')
                return f'роль {name} по идее удалена из списка автоматических наград за этот уровень'

    def get_range_roles(self, dbname):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS range_roles(role_id INTEGER, lvl INTEGER)')
            cur.execute(f'SELECT role_id FROM range_roles')
            cort = []
            for i in cur.fetchall():
                cort.append(i[0])

            dic = {}
            for id in cort:
                cur.execute(f'SELECT lvl FROM range_roles WHERE role_id = {int(id)}')
                dic[id] = cur.fetchone()[0]

            return dic
"""

dbname = 'ща удалю нахуй.db'

a = '0'
while a != 'стоп':
    a = input('введи действие: ')
    if a == 'limit':
        b = input('введите лимит: ')
        print(settings().set_spam_limit(dbname, b))

    elif a == 'alert':
        b = input('введи алёрт: ')
        print(settings().set_spam_alert(dbname, b))

    elif a == 'get':
        print('limit: ', settings().get_spam_limit(dbname)['limit'])
        print('alert: ', settings().get_spam_limit(dbname)['alert'])


print('программа завершена')
"""

