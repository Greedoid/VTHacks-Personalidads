import sqlite3


conn = sqlite3.connect('genres.db')
c = conn.cursor()
c.execute("CREATE TABLE genre(Subgenre VARCHAR NOT NULL PRIMARY KEY, Mapped_Genre VARCHAR)")
if conn:
	conn.close()
