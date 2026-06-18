# Singapore Public Transport Data Pipeline & Analytics Dashboard

## Overview
An end-to-end data engineering and analytics project built on real, live Singapore public transport data from LTA DataMall. The project combines static reference data (bus stops, bus services) with a live, automated data ingestion pipeline (bus arrival times), demonstrating both data engineering (API integration, automated scheduling, database design) and data analysis (SQL querying, Power BI visualization) skills.

## Project Goals
This project was built to demonstrate practical, hands-on experience with Python, SQL, and data pipeline design — skills that are foundational to both Data Analyst and Data Engineer roles — using real, publicly available Singapore government data.

## Architecture
LTA DataMall API → Python (ingestion & cleaning) → SQLite (storage) → SQL (transformation/analysis) → Power BI (visualization)

## Key Components

**1. Static Data Pipeline**
- Python script (`fetch_static_data.py`) pulls Bus Stops (5,205 records) and Bus Services (800 records) from LTA's REST API, handling pagination automatically.

**2. Live Data Pipeline**
- Python script (`fetch_bus_arrival.py`) polls live bus arrival data for 4 major Singapore bus interchanges (Orchard, Jurong East, Tampines, Woodlands).
- Automated via Windows Task Scheduler to run every 10 minutes, continuously appending timestamped records to a SQLite database — without manual intervention.

**3. Database**
- SQLite database (`transport.db`) storing three tables: bus_stops, bus_services, and bus_arrivals (the growing live dataset).

**4. SQL Analysis**
- Queries to identify busiest roads by bus stop density, bus service distribution by operator, and most frequently captured bus services in the live data.

**5. Dashboard**
- Interactive Power BI dashboard featuring KPI cards, bar charts, a live time-series chart, and a slicer for filtering by bus stop.

## Tools Used
Python (pandas, requests, sqlite3, python-dotenv), SQL (SQLite), Power BI, Windows Task Scheduler

## Data Source
LTA DataMall (Land Transport Authority, Singapore) — https://datamall.lta.gov.sg

## Screenshots
See `images/dashboard_screenshot.png`