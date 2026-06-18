import os
import sqlite3
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("LTA_API_KEY")

HEADERS = {
    "AccountKey": API_KEY,
    "accept": "application/json"
}

BUS_STOPS = {
    "9023": "Orchard (Opp Orchard Stn/ION)",
    "28009": "Jurong East Interchange",
    "75009": "Tampines Interchange",
    "46008": "Woodlands Interchange"
}

DB_PATH = "db/transport.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bus_arrivals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pulled_at TEXT,
            bus_stop_code TEXT,
            bus_stop_name TEXT,
            service_no TEXT,
            estimated_arrival TEXT,
            load_status TEXT
        )
    """)
    conn.commit()
    return conn

def fetch_arrival(bus_stop_code):
    url = "https://datamall2.mytransport.sg/ltaodataservice/v3/BusArrival"
    params = {"BusStopCode": bus_stop_code}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()

def main():
    if not API_KEY:
        print("ERROR: LTA_API_KEY not found. Check your .env file.")
        return

    conn = init_db()
    cursor = conn.cursor()
    pulled_at = datetime.now().isoformat()

    for stop_code, stop_name in BUS_STOPS.items():
        try:
            data = fetch_arrival(stop_code)
            services = data.get("Services", [])
            for service in services:
                service_no = service.get("ServiceNo")
                next_bus = service.get("NextBus", {})
                arrival_time = next_bus.get("EstimatedArrival")
                load = next_bus.get("Load")
                cursor.execute("""
                    INSERT INTO bus_arrivals (pulled_at, bus_stop_code, bus_stop_name, service_no, estimated_arrival, load_status)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (pulled_at, stop_code, stop_name, service_no, arrival_time, load))
            print(f"{stop_name}: saved {len(services)} services")
        except Exception as e:
            print(f"Error fetching {stop_name} ({stop_code}): {e}")

    conn.commit()
    conn.close()
    print(f"Done. Pull timestamp: {pulled_at}")

if __name__ == "__main__":
    main()