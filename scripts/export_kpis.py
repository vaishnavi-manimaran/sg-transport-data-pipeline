import sqlite3
import pandas as pd

DB_PATH = "db/transport.db"
OUTPUT_DIR = "data/processed"

def main():
    conn = sqlite3.connect(DB_PATH)

    total_stops = conn.execute("SELECT COUNT(*) FROM bus_stops").fetchone()[0]
    total_services = conn.execute("SELECT COUNT(*) FROM bus_services").fetchone()[0]
    total_live_records = conn.execute("SELECT COUNT(*) FROM bus_arrivals").fetchone()[0]
    stops_monitored_live = conn.execute("SELECT COUNT(DISTINCT bus_stop_code) FROM bus_arrivals").fetchone()[0]

    kpis = pd.DataFrame([{
        "total_bus_stops": total_stops,
        "total_bus_services": total_services,
        "total_live_records": total_live_records,
        "stops_monitored_live": stops_monitored_live
    }])

    kpis.to_csv(f"{OUTPUT_DIR}/kpis.csv", index=False)
    print(kpis.to_string(index=False))
    print("Saved to data/processed/kpis.csv")

    conn.close()

if __name__ == "__main__":
    main()