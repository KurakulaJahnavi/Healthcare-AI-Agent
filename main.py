from login import login
from tracking import track_daily
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    name TEXT,
    health_conditions TEXT
)
""")

# create daily health table
cursor.execute("""
CREATE TABLE IF NOT EXISTS daily_health(
    name TEXT,
    steps INTEGER,
    sleep_hours REAL,
    water_liters REAL,
    medicine_taken TEXT
)
""")

conn.commit()


def health_check():
    print("\nSelect your health conditions (comma separated)")
    print("1. BP")
    print("2. Diabetes")
    print("3. PCOS/PCOD")
    print("4. Thyroid")
    print("5. Cancer")
    print("6. None")

    choices = input("Enter your choices: ").split(",")

    conditions = []

    for choice in choices:
        choice = choice.strip()

        if choice == "1":
            conditions.append("BP")
        elif choice == "2":
            conditions.append("Diabetes")
        elif choice == "3":
            conditions.append("PCOS")
        elif choice == "4":
            conditions.append("Thyroid")
        elif choice == "5":
            conditions.append("Cancer")
        elif choice == "6":
            conditions.append("None")

    return conditions


def store_data(name, conditions):
    condition_text = ",".join(conditions)

    cursor.execute(
        "INSERT INTO users (name, health_conditions) VALUES (?, ?)",
        (name, condition_text)
    )

    conn.commit()


# program start
name = login()

conditions = health_check()

store_data(name, conditions)

print("\nYour health conditions are saved:", conditions)

track_daily(name, conn, cursor)
cursor.execute("SELECT * FROM daily_health")
print("Saved Data:", cursor.fetchall())