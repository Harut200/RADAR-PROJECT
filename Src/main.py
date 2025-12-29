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

           
