import sqlite3

con=sqlite3.connect("finalheartdb.db")
print("database opened successfully")

con.execute('create table reguser(id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL,mailid TEXT NOT NULL,password TEXT NOT NULL)')

print("table created successfully")
con.close()

