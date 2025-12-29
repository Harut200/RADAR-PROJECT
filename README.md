# Urban Radar – London Transport Data Pipeline

## Overview
Urban Radar is a backend data engineering project that builds an end-to-end pipeline using real-time public transport data from the Transport for London (TfL) Open API. The project focuses on API ingestion, data normalization, relational storage, and analytical querying using Python, SQLite, and Pandas.

No API key or external services are required.

---

## Data Source
- **API**: Transport for London (TfL) StopPoint Arrivals API  
- **Type**: Real-time JSON data  
- **Access**: Public (no authentication)

### Monitored Locations
- Waterloo Station  
- Oxford Circus  
- Victoria Station  
- King’s Cross  
- London Bridge  

---

## Tech Stack
- Python  
- Requests  
- Pandas  
- NumPy  
- SQLite  
- SQL  

---

## Pipeline Workflow
1. Fetch live arrival predictions for selected London stations  
2. Validate and clean nested JSON responses  
3. Normalize data into structured records  
4. Enrich data with peak-hour detection  
5. Store results in a SQLite database  
6. Load data into Pandas for analysis  

---

## Database Schema
Table: `bus_arrivals`

| Column | Description |
|------|------------|
| stop_name | Station name |
| stop_id | Stop identifier |
| line_id | Transport line |
| destination | Destination name |
| expected_arrival | Arrival timestamp |
| time_to_station | Seconds until arrival |
| is_peak | Peak hour flag (1 or 0) |

Peak hours:
- Morning: 07:00–10:00  
- Evening: 16:00–19:00  

---

## Analysis Performed
- Station with the highest number of peak-hour arrivals  
- Station with the longest average waiting time  
- Overall average waiting time (minutes)  

---

## Purpose
This project demonstrates practical backend and data engineering skills, including API integration, SQL-based persistence, time-based feature engineering, and analytical querying with Pandas. It is designed to be simple, readable, and suitable for academic exams or junior data portfolios.
