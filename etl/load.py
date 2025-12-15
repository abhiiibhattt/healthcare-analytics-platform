import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("../healthcare.db")
PROCESSED_DATA_PATH = Path("../data/processed")
SCHEMA_PATH = Path("../sql/schema.sql")

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create tables
    with open(SCHEMA_PATH, "r") as f:
        cursor.executescript(f.read())

    # Load cleaned data
    pd.read_csv(PROCESSED_DATA_PATH / "patients_clean.csv").to_sql(
        "patients", conn, if_exists="append", index=False
    )
    pd.read_csv(PROCESSED_DATA_PATH / "appointments_clean.csv").to_sql(
        "appointments", conn, if_exists="append", index=False
    )
    pd.read_csv(PROCESSED_DATA_PATH / "tests_clean.csv").to_sql(
        "tests", conn, if_exists="append", index=False
    )
    pd.read_csv(PROCESSED_DATA_PATH / "billing_clean.csv").to_sql(
        "billing", conn, if_exists="append", index=False
    )

    conn.commit()
    conn.close()

    print("Data successfully loaded into SQLite database.")

if __name__ == "__main__":
    main()
