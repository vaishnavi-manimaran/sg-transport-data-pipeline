import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load API key from .env file in the project root
load_dotenv()
API_KEY = os.getenv("LTA_API_KEY")

HEADERS = {
    "AccountKey": API_KEY,
    "accept": "application/json"
}

def fetch_all_records(url):
    """Fetch all records from an LTA DataMall API, handling pagination via $skip."""
    all_records = []
    skip = 0
    while True:
        response = requests.get(url, headers=HEADERS, params={"$skip": skip})
        response.raise_for_status()
        data = response.json().get("value", [])
        if not data:
            break
        all_records.extend(data)
        skip += 500
    return all_records

def main():
    if not API_KEY:
        print("ERROR: LTA_API_KEY not found. Check your .env file.")
        return

    print("Fetching Bus Stops...")
    bus_stops = fetch_all_records("https://datamall2.mytransport.sg/ltaodataservice/BusStops")
    pd.DataFrame(bus_stops).to_csv("data/raw/bus_stops.csv", index=False)
    print(f"Saved {len(bus_stops)} bus stops to data/raw/bus_stops.csv")

    print("Fetching Bus Services...")
    bus_services = fetch_all_records("https://datamall2.mytransport.sg/ltaodataservice/BusServices")
    pd.DataFrame(bus_services).to_csv("data/raw/bus_services.csv", index=False)
    print(f"Saved {len(bus_services)} bus services to data/raw/bus_services.csv")

if __name__ == "__main__":
    main()