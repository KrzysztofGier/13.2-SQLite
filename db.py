import sqlite3

db = sqlite3.connect("database.db")

print("opened database successfully")

db.execute(
    "CREATE TABLE movies(movie_id INTEGER PRIMARY KEY AUTOINCREMENT,movie_title TEXT,genres TEXT)")

print("table created successfully")

db.close()