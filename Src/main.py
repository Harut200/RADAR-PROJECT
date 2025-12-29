import json
import sqlite3
import requests
import numpy as np
import pandas as pd
from pathlib import Path

DB_PATH = Path("../Data/DB/URBAN_RADAR.db")
BASE_URL = "https://api.tfl.gov.uk/StopPoint/"
STP_CNT = {"Waterloo Station": "490008660N", "Oxford Circus": "490000091W", 
           "Victoria Station": "490008660S", "King's Cross": "490000092K", "London Bridge": "490000093L"}

           
data_ = []

for stp in STP_CNT.values():
    resp = requests.get(f"{BASE_URL}{stp}/Arrivals").json()
    data_.append(resp)

data_


data1 = [pred_list for pred_list in data_ if isinstance(pred_list, list)]
data1


data = []
peak_hrs = [7,8,9,10,16,17,18,19]

for pred_list in data1:
    for pred in pred_list:
        if isinstance(pred, dict):
            dic = {}
            dic["stop_name"] = pred.get("stationName", "")
            dic["stop_id"] = pred.get("naptanId", "")
            dic["line_id"] = pred.get("lineId", "")
            dic["destination"] = pred.get("destinationName", "")
            dic["expected_arrival"] = pred.get("expectedArrival", "")
            dic["time_to_station"] = pred.get("timeToStation", 0)
            h_t = int(pred.get("expectedArrival", "00:00:00").split("T")[1].split(":")[0])
            dic["is_peak"] = 1 if h_t in peak_hrs else 0
            data.append(dic)

data


conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# cur.execute(
#     """
#     DROP TABLE IF EXISTS bus_arrivals;
#     """
# )

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS bus_arrivals(
    id INTEGER PRIMARY KEY,
    stop_name TEXT,
    stop_id TEXT,
    line_id TEXT,
    destination TEXT,
    expected_arrival TEXT,
    time_to_station INTEGER,
    is_peak INTEGER
    );
    """
)

com_for_insert = """
    INSERT OR REPLACE INTO bus_arrivals(stop_name, stop_id, line_id, destination, expected_arrival, time_to_station, is_peak)
    VALUES(:stop_name, :stop_id, :line_id, :destination, :expected_arrival, :time_to_station, :is_peak)
    """

cur.executemany(com_for_insert, data)

conn.commit()
conn.close()


conn = sqlite3.connect(DB_PATH)
df = pd.read_sql("""SELECT * FROM bus_arrivals""", conn)
conn.close()

df


df["wait_time_min"] = df["time_to_station"] // 60

df


df.groupby("stop_name")["is_peak"].sum().idxmax()

df.groupby("stop_name")["time_to_station"].mean().idxmax()

df["wait_time_min"].mean()

