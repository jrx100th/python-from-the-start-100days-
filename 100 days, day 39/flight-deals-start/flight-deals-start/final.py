import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import smtplib

load_dotenv()

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_PASSWORD = os.environ["SHEETY_PASSWORD"]
SHEETY_PUT_ENDPOINT = os.environ["SHEETY_PUT_ENDPOINT"]

GMAIL_APP_PASSWORD = os.environ["gmail_app_password"]
GMAIL_SENDER_MAIL = os.environ["sender_email"]


# print(SHEETY_ENDPOINT)

sheety_headers = {
    "Authorization" : f"Basic {SHEETY_USERNAME}:{SHEETY_PASSWORD}"
}

response = (requests.get(url=SHEETY_ENDPOINT,auth=HTTPBasicAuth(SHEETY_USERNAME,SHEETY_PASSWORD))).json()
# print(response)
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




import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta


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
# print(response)
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




our_req = {}

for i in range(len(cities)):
    our_req[iata_codes[i]] = [low_prices[i],cities[i]]

AMADEUS_API_KEY = os.environ["AMADEUS_API_KEY"]
AMADEUS_SECRET_KEY = os.environ["AMADEUS_SECRET_KEY"]
TOKEN_ENDPOINT = os.environ["TOKEN_ENDPOINT"]
ORIGINAL_LOCATION = "LON"
AMADEUS_GET_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"  # Amadeus test endpoint

delta = timedelta(days=180)
delta_1_day = timedelta(days=1)
now = datetime.now()
now = (now+delta_1_day)
after_6_months = (now+delta)
now = now.strftime("%Y-%m-%d")
after_6_months = after_6_months.strftime("%Y-%m-%d")
duration = timedelta(days=7)
return_date = datetime.now()+duration
return_date = return_date.strftime("%Y-%m-%d")

def get_new_token():
    amadeus_token_header = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    body = {
        'grant_type': 'client_credentials',
        'client_id': AMADEUS_API_KEY,
        'client_secret': AMADEUS_SECRET_KEY
    }
    token_response = requests.post(url=TOKEN_ENDPOINT,data=body, headers=amadeus_token_header)
    return (token_response.json()["access_token"])

def get_and_parse_data(inp_iata_code):
    amadeus_token = get_new_token()
    # print(amadeus_token)

    amadeus_get_headers = {
        "Authorization" : f"Bearer {amadeus_token}"
    }

    parameters = {
        "originLocationCode" : ORIGINAL_LOCATION,
        "destinationLocationCode" : inp_iata_code,
        "departureDate" : now,
        "returnDate" : return_date,
        "adults" : 1,
        "children" : 0,
        "infants" : 0,
        "travelClass" : "ECONOMY",
        "excludedAirlineCodes" : "FR,RR",
        "nonStop" : "true", # not boolean as they said
        "currencyCode" : "EUR",
        "maxPrice" : 800,
        "max" : 250
    }

    get_response = requests.get(
        url=AMADEUS_GET_ENDPOINT, 
        params=parameters,
        headers=amadeus_get_headers
    )

    json_data = get_response.json()
    prices = []
    in_dates = []
    departure_airports = []
    arrival_airports = []
    out_dates = []

    for i in range(len(json_data['data'])):
        in_dates.append(json_data['data'][i]['itineraries'][0]['segments'][0]['departure']['at'])
        departure_airports.append(json_data['data'][i]['itineraries'][0]['segments'][0]['departure']['iataCode'])
        prices.append(json_data['data'][i]['price']['total'])
        arrival_airports.append(json_data['data'][i]['itineraries'][0]['segments'][0]['arrival']['iataCode'])
        out_dates.append((json_data['data'][i]['itineraries'][0]['segments'][0]['arrival']['at']))
        
    return [in_dates,out_dates,departure_airports,arrival_airports,prices]

def run_for_each():
    for key in our_req:
        values = get_and_parse_data(key)
        if float(min(values[5])) < float(our_req[key][0]):
            ind = values[4].index(min(values[4]))
            departure_time = values[0][ind]
            arrival_time = values[1][ind]
            departure_airport = values[2][ind]
            arrival_airport = values[3][ind]
            price = values[4][ind]
            final_msg = f"Departure Time :{departure_time}\nArrival Time : {arrival_time}\nDeparture Airport: {departure_airport}\nArrival Airport : {arrival_airport}\nFinal Ticket Price :{price}"
            connection = smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login(user=GMAIL_SENDER_MAIL,password=GMAIL_APP_PASSWORD)
            connection.sendmail(
                to_addrs=GMAIL_SENDER_MAIL,
                from_addr=GMAIL_SENDER_MAIL,
                msg=f"Subject:Found a cheaper flight ticket\n\n{
                    final_msg
                }"
            )

run_for_each()
