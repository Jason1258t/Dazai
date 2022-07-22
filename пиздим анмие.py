import sqlite3

dbn1 = 'Дазай/animePizdim.db' #новая бд из которой берешь новые аниме
dbn2 = 'Дазай/anime.db'

animes = {}


with sqlite3.connect(dbn1) as db:
    c1 = db.cursor()

    c1.execute("""SELECT name FROM anime WHERE id > 54""")

    names = c1.fetchall()

    for name in names:
        c1.execute("""SELECT id FROM anime WHERE name = ?""", (name[0],))
        id = c1.fetchone()[0] + 4

        c1.execute("""SELECT image FROM anime WHERE name = ?""", (name[0],))
        image = c1.fetchone()[0]

        c1.execute("""SELECT tags FROM anime WHERE name = ?""", (name[0],))
        tags = c1.fetchone()[0]

        c1.execute("""SELECT count FROM anime WHERE name = ?""", (name[0],))
        count = c1.fetchone()[0]

        c1.execute("""SELECT est FROM anime WHERE name = ?""", (name[0],))
        est = c1.fetchone()[0]

        c1.execute("""SELECT dat FROM anime WHERE name = ?""", (name[0],))
        dat = c1.fetchone()[0]

        animes[name[0]] = {}
        animes[name[0]]['id'] = id
        animes[name[0]]['name'] = name[0]
        animes[name[0]]['image'] = image
        animes[name[0]]['tags'] = tags
        animes[name[0]]['count'] = count
        animes[name[0]]['est'] = est
        animes[name[0]]['dat'] = dat


print(animes)

with sqlite3.connect(dbn2) as db:
    cur = db.cursor()
    for i in animes:
        cur.execute("""INSERT INTO anime(id, name, image, tags, count, est, dat) VALUES(?, ?, ?, ?, ?, ?, ?)""", (animes[i]['id'],  animes[i]['name'], animes[i]['image'], animes[i]['tags'], animes[i]['count'], animes[i]['est'], animes[i]['dat']))
