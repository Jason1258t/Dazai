import sqlite3

dbname_1 = 'Шрекотопия_achivs.db'
dbname_2 = 'Комната дазая_achivs.db'
dbname_3 = 'GhostSquad_achivs.db'

def add_column(dbname):
	with sqlite3.connect(dbname) as db:
		cur = db.cursor()
		cur.execute("""ALTER TABLE ochko ADD COLUMN ochko INTEGER DEFAULT FALSE""")

add_column(dbname_1)
add_column(dbname_2)
add_column(dbname_3)

a = input('жмякни для завершения')
