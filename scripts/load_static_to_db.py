import sqlite3
import pandas as pd

DB_PATH = "db/transport.db"

def main():
    conn = sqlite3.connect(DB_PATH)

    print("Loading bus_stops.csv...")
    bus_stops = pd.read_csv("data/raw/bus_stops.csv")
    bus_stops.to_sql("bus_stops", conn, if_exists="replace", index=False)
    print(f"Loaded {len(bus_stops)} rows into bus_stops table")

    print("Loading bus_services.csv...")
    bus_services = pd.read_csv("data/raw/bus_services.csv")
    bus_services.to_sql("bus_services", conn, if_exists="replace", index=False)
    print(f"Loaded {len(bus_services)} rows into bus_services table")

    conn.close()
    print("Done.")

if __name__ == "__main__":
    main()