# sql.py - Create a SQLite3 table and populate it with data
import sqlite3

with sqlite3.connect("blog.db") as dbconn:
	#get a cursor object used to execute SQL commands
	curs = dbconn.cursor()
	
	# lets create a table name posts
	curs.execute(""" 
					CREATE TABLE IF NOT EXISTS posts
					(title TEXT, post TEXT)
				
				""")

	# insert dummy data into the table
	curs.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
	curs.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
	curs.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
	curs.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')