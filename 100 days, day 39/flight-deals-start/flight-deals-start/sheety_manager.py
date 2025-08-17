#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_PASSWORD = os.environ["SHEETY_PASSWORD"]
SHEETY_PUT_ENDPOINT = os.environ["SHEETY_PUT_ENDPOINT"]

# print(SHEETY_ENDPOINT)

sheety_headers = {
    "Authorization" : f"Basic {SHEETY_USERNAME}:{SHEETY_PASSWORD}"
}

response = (requests.get(url=SHEETY_ENDPOINT,auth=HTTPBasicAuth(SHEETY_USERNAME,SHEETY_PASSWORD))).json()

response = (response["sheet1"])

cities = []
iata_codes = []
low_prices = []

for i in range(len(response)):
    cities.append(response[i]['city'])
    iata_codes.append(response[i]['iataCode'])
    low_prices.append(response[i]['lowestPrice'])

# print(cities)
# print(iata_codes)
# print(low_prices)
sheet_data = low_prices

sheety_put_header = {
    "Content-Type" : "application/json"
}

city_iata_map = {
    "Paris": "PAR",
    "Frankfurt": "FRA",
    "Tokyo": "TYO",
    "Hong Kong": "HKG",
    "Istanbul": "IST",
    "Kuala Lumpur": "KUL",
    "New York": "NYC",
    "San Francisco": "SFO",
    "Dublin": "DUB"
}

# Get data from sheet
resp1 = requests.get(SHEETY_ENDPOINT, auth=HTTPBasicAuth(SHEETY_USERNAME, SHEETY_PASSWORD)).json()
rows = resp1["sheet1"] 

def update_iata():
    for row in rows:
        city = row["city"]
        row_id = row["id"]  # use the actual row ID from Sheety response

        iata_code = city_iata_map.get(city)
        if iata_code:
            update_data = {
                "sheet1": {
                    "iataCode": iata_code
                }
            }
            put_url = f"{SHEETY_PUT_ENDPOINT}/{row_id}"
            resp = requests.put(
                url=put_url,
                auth=HTTPBasicAuth(SHEETY_USERNAME, SHEETY_PASSWORD),
                headers=sheety_put_header,
                json=update_data
            )
            print(f"Updated {city} (Row {row_id}): {resp.status_code} {resp.text}")


# update_iata()


print(response)