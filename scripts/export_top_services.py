import sqlite3
import pandas as pd

conn = sqlite3.connect("db/transport.db")

top_services = pd.read_sql_query("""
    SELECT service_no, COUNT(*) as times_captured
    FROM bus_arrivals
    GROUP BY service_no
    ORDER BY times_captured DESC
    LIMIT 5
""", conn)

top_services.to_csv("data/processed/top_services.csv", index=False)
print(top_services.to_string(index=False))
conn.close()