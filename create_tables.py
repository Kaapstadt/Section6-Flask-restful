import sqlite3

connection =  sqlite3.connect('data.db')
cursor = connection.cursor()

#INTEGER as opposed to int creates an auto increment field
create_table = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)'
cursor.execute(create_table)

create_table = 'CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY ,name text, price real)'
cursor.execute(create_table)


connection.commit()
connection.close()

