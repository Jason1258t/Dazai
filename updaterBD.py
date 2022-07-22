import sqlite3


def update_sql(dbname):
    with sqlite3.connect(dbname) as db:
        cur = db.cursor()
        cur.execute("""ALTER TABLE achivs ADD column pasol_nahui BOOL DEFAULT False""")
        print('Изменения внесены в {0}'.format(dbname))

#update_sql('database/Комната дазая_achivs.db')
#update_sql('database/Шрекотопия_achivs.db')
#update_sql('database/GhostSquad_achivs.db')
