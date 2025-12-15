import sqlite3

conn = sqlite3.connect("../healthcare.db")
cursor = conn.cursor()

tables = cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table';"
).fetchall()

print("Tables:", tables)

for table in ["patients", "appointments", "tests", "billing"]:
    count = cursor.execute(f"SELECT COUNT(*) FROM {table};").fetchone()[0]
    print(f"{table}: {count} rows")

conn.close()
