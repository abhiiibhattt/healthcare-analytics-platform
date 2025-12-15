import sqlite3
import pandas as pd

conn = sqlite3.connect("../healthcare.db")

queries = {
    "Appointment Status": """
        SELECT status, COUNT(*) AS count
        FROM appointments
        GROUP BY status;
    """,
    "Avg Turnaround by Test": """
        SELECT test_type, AVG(turnaround_time_hours) AS avg_turnaround
        FROM tests
        GROUP BY test_type;
    """,
    "Revenue by Department": """
        SELECT a.department, SUM(b.amount) AS total_revenue
        FROM billing b
        JOIN appointments a ON b.patient_id = a.patient_id
        GROUP BY a.department;
    """
}

for name, query in queries.items():
    df = pd.read_sql_query(query, conn)
    print(f"\n{name}")
    print(df)

conn.close()
