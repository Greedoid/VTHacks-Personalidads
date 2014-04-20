import sqlite3
import json

def insert_mapping(genre, mapping): 
	conn = sqlite3.connect('genres.db')
	conn.execute("INSERT INTO genre(Subgenre, Mapped_Genre) VALUES (?, ?)", (genre, mapping),)
	conn.commit()
	if conn:
		conn.close()

def get_mapped_genre(subgenre):
	conn = sqlite3.connect('genres.db')
	cur = conn.cursor()
	cur.execute("SELECT Mapped_Genre FROM genre WHERE Subgenre = ?", (subgenre,))
	classified = cur.fetchone()
	if conn: 
		conn.close()
	return (classified)

