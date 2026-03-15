import sqlite3

conn = sqlite3.connect("health.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
password TEXT,
health_condition TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")
