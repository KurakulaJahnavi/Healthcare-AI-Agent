def track_daily(name, conn, cursor):

    print("\n--- Daily Health Tracker ---")

    steps = int(input("Enter today's steps: "))
    sleep = float(input("Enter sleep hours: "))
    water = float(input("Enter water intake (liters): "))
    medicine = input("Did you take medicine? (yes/no): ")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS daily_health(
        name TEXT,
        steps INTEGER,
        sleep_hours REAL,
        water_liters REAL,
        medicine_taken TEXT
    )
    """)

    cursor.execute(
        "INSERT INTO daily_health VALUES (?,?,?,?,?)",
        (name, steps, sleep, water, medicine)
    )

    conn.commit()

    # DEBUG PRINT
    cursor.execute("SELECT * FROM daily_health")
    print("Saved Data:", cursor.fetchall())

    print("\nDaily health data saved successfully!")