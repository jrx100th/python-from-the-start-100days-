import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta
load_dotenv()

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
def get_and_parse_data():
    amadeus_token = get_new_token()
    # print(amadeus_token)

    amadeus_get_headers = {
        "Authorization" : f"Bearer {amadeus_token}"
    }


    parameters = {
        "originLocationCode" : ORIGINAL_LOCATION,
        "destinationLocationCode" : "PAR",
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

    print(get_response.status_code)
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


# minimal_params = {
#     "originLocationCode": ORIGINAL_LOCATION,
#     "destinationLocationCode": "PAR",
#     "departureDate": now,
#     "adults": 1,
# }

# get_response = requests.get(
#     url=AMADEUS_GET_ENDPOINT,
#     params=minimal_params,
#     headers=amadeus_get_headers
# )

# print(get_response.status_code)
# print(get_response.json())





# damn my code is working now


# all the list are set

# print(in_dates)
# print(out_dates)
# print(departure_airports)
# print(arrival_airports)
# print(prices)