import sqlite3
import pandas as pd

DB_PATH = "db/transport.db"
OUTPUT_DIR = "data/processed"

def main():
    conn = sqlite3.connect(DB_PATH)

    print("Exporting: stops per road...")
    stops_per_road = pd.read_sql_query("""
        SELECT RoadName, COUNT(*) as stop_count
        FROM bus_stops
        GROUP BY RoadName
        ORDER BY stop_count DESC
        LIMIT 20
    """, conn)
    stops_per_road.to_csv(f"{OUTPUT_DIR}/stops_per_road.csv", index=False)
    print(f"Saved {len(stops_per_road)} rows to stops_per_road.csv")

    print("Exporting: services per operator...")
    services_per_operator = pd.read_sql_query("""
        SELECT Operator, COUNT(*) as service_count
        FROM bus_services
        GROUP BY Operator
        ORDER BY service_count DESC
    """, conn)
    services_per_operator.to_csv(f"{OUTPUT_DIR}/services_per_operator.csv", index=False)
    print(f"Saved {len(services_per_operator)} rows to services_per_operator.csv")

    print("Exporting: live bus arrivals (all records so far)...")
    bus_arrivals = pd.read_sql_query("SELECT * FROM bus_arrivals", conn)
    bus_arrivals.to_csv(f"{OUTPUT_DIR}/bus_arrivals.csv", index=False)
    print(f"Saved {len(bus_arrivals)} rows to bus_arrivals.csv")

    conn.close()
    print("Done.")

if __name__ == "__main__":
    main()