import sqlite3
connection =  sqlite3.connect('data.db')

cursor = connection.cursor()
create_table = 'CREATE TABLE users(id int, username text, password text)'
cursor.execute(create_table)

user = (1,'brian','password')
insert_query = 'INSERT INTO users VALUES(?, ?, ?)'
cursor.execute(insert_query,user)

#inserting many

_users = [
    (2,'Caleb','123'),
    (3,'Zoe','456')
]

cursor.executemany(insert_query,_users)

select_query = 'SELECT * from users'
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()