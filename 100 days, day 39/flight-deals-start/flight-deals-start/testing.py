from datetime import datetime, timedelta

delta = timedelta(days=180)
delta_1_day = timedelta(days=1)
now = datetime.now()
now = (now+delta_1_day)
after_6_months = (now+delta)

now = now.strftime("%Y-%m-%d")
after_6_months = after_6_months.strftime("%Y-%m-%d")

# print(now)
# print(after_6_months)



duration = timedelta(days=7)
return_date = datetime.now()+duration
return_date = return_date.strftime("%Y-%m-%d")
# print(return_date)




prices = []
dates = []
departure_airports = []
arrival_airports = []
out = []

json_data ={
  'meta': {
    'count': 4,
    'links': {
      'self': 'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=LON&destinationLocationCode=PAR&departureDate=2025-08-17&returnDate=2025-08-23&adults=1&children=0&infants=0&travelClass=ECONOMY&excludedAirlineCodes=FR,RR&nonStop=true&currencyCode=EUR&maxPrice=800&max=4'
    }
  },
  'data': [
    {
      'type': 'flight-offer',
      'id': '1',
      'source': 'GDS',
      'instantTicketingRequired': False,
      'nonHomogeneous': False,
      'oneWay': False,
      'isUpsellOffer': False,
      'lastTicketingDate': '2025-08-16',
      'lastTicketingDateTime': '2025-08-16',
      'numberOfBookableSeats': 4,
      'itineraries': [
        {
          'duration': 'PT1H25M',
          'segments': [
            {
              'departure': {
                'iataCode': 'LGW',
                'terminal': 'S',
                'at': '2025-08-17T19:40:00'
              },
              'arrival': {
                'iataCode': 'ORY',
                'terminal': '3',
                'at': '2025-08-17T22:05:00'
              },
              'carrierCode': 'VY',
              'number': '8945',
              'aircraft': {
                'code': '320'
              },
              'operating': {
                'carrierCode': 'VY'
              },
              'duration': 'PT1H25M',
              'id': '1',
              'numberOfStops': 0,
              'blacklistedInEU': False
            }
          ]
        },
        {
          'duration': 'PT1H35M',
          'segments': [
            {
              'departure': {
                'iataCode': 'ORY',
                'terminal': '1',
                'at': '2025-08-23T13:40:00'
              },
              'arrival': {
                'iataCode': 'LHR',
                'terminal': '4',
                'at': '2025-08-23T14:15:00'
              },
              'carrierCode': 'VY',
              'number': '8960',
              'aircraft': {
                'code': '320'
              },
              'operating': {
                'carrierCode': 'VY'
              },
              'duration': 'PT1H35M',
              'id': '5',
              'numberOfStops': 0,
              'blacklistedInEU': False
            }
          ]
        }
      ],
      'price': {
        'currency': 'EUR',
        'total': '156.65',
        'base': '79.00',
        'fees': [
          {
            'amount': '0.00',
            'type': 'SUPPLIER'
          },
          {
            'amount': '0.00',
            'type': 'TICKETING'
          }
        ],
        'grandTotal': '156.65'
      },
      'pricingOptions': {
        'fareType': [
          'PUBLISHED'
        ],
        'includedCheckedBagsOnly': True
      },
      'validatingAirlineCodes': [
        'VY'
      ],
      'travelerPricings': [
        {
          'travelerId': '1',
          'fareOption': 'STANDARD',
          'travelerType': 'ADULT',
          'price': {
            'currency': 'EUR',
            'total': '156.65',
            'base': '79.00'
          },
          'fareDetailsBySegment': [
            {
              'segmentId': '1',
              'cabin': 'ECONOMY',
              'fareBasis': 'PROPLVY',
              'class': 'P',
              'includedCheckedBags': {
                'weight': 25,
                'weightUnit': 'KG'
              },
              'includedCabinBags': {
                'quantity': 1
              }
            },
            {
              'segmentId': '5',
              'cabin': 'ECONOMY',
              'fareBasis': 'DROPL2VY',
              'class': 'D',
              'includedCheckedBags': {
                'weight': 25,
                'weightUnit': 'KG'
              },
              'includedCabinBags': {
                'quantity': 1
              }
            }
          ]
        }
      ]
    },
    {
      'type': 'flight-offer',
      'id': '2',
      'source': 'GDS',
      'instantTicketingRequired': False,
      'nonHomogeneous': False,
      'oneWay': False,
      'isUpsellOffer': False,
      'lastTicketingDate': '2025-08-16',
      'lastTicketingDateTime': '2025-08-16',
      'numberOfBookableSeats': 4,
      'itineraries': [
        {
          'duration': 'PT1H30M',
          'segments': [
            {
              'departure': {
                'iataCode': 'LGW',
                'terminal': 'S',
                'at': '2025-08-17T07:40:00'
              },
              'arrival': {
                'iataCode': 'ORY',
                'terminal': '3',
                'at': '2025-08-17T10:10:00'
              },
              'carrierCode': 'VY',
              'number': '8943',
              'aircraft': {
                'code': '320'
              },
              'operating': {
                'carrierCode': 'VY'
              },
              'duration': 'PT1H30M',
              'id': '2',
              'numberOfStops': 0,
              'blacklistedInEU': False
            }
          ]
        },
        {
          'duration': 'PT1H35M',
          'segments': [
            {
              'departure': {
                'iataCode': 'ORY',
                'terminal': '1',
                'at': '2025-08-23T13:40:00'
              },
              'arrival': {
                'iataCode': 'LHR',
                'terminal': '4',
                'at': '2025-08-23T14:15:00'
              },
              'carrierCode': 'VY',
              'number': '8960',
              'aircraft': {
                'code': '320'
              },
              'operating': {
                'carrierCode': 'VY'
              },
              'duration': 'PT1H35M',
              'id': '5',
              'numberOfStops': 0,
              'blacklistedInEU': False
            }
          ]
        }
      ],
      'price': {
        'currency': 'EUR',
        'total': '156.65',
        'base': '79.00',
        'fees': [
          {
            'amount': '0.00',
            'type': 'SUPPLIER'
          },
          {
            'amount': '0.00',
            'type': 'TICKETING'
          }
        ],
        'grandTotal': '156.65'
      },
      'pricingOptions': {
        'fareType': [
          'PUBLISHED'
        ],
        'includedCheckedBagsOnly': True
      },
      'validatingAirlineCodes': [
        'VY'
      ],
      'travelerPricings': [
        {
          'travelerId': '1',
          'fareOption': 'STANDARD',
          'travelerType': 'ADULT',
          'price': {
            'currency': 'EUR',
            'total': '156.65',
            'base': '79.00'
          },
          'fareDetailsBySegment': [
            {
              'segmentId': '2',
              'cabin': 'ECONOMY',
              'fareBasis': 'PROPLVY',
              'class': 'P',
              'includedCheckedBags': {
                'weight': 25,
                'weightUnit': 'KG'
              },
              'includedCabinBags': {
                'quantity': 1
              }
            },
            {
              'segmentId': '5',
              'cabin': 'ECONOMY',
              'fareBasis': 'DROPL2VY',
              'class': 'D',
              'includedCheckedBags': {
                'weight': 25,
                'weightUnit': 'KG'
              },
              'includedCabinBags': {
                'quantity': 1
              }
            }
          ]
        }
      ]
    },
    {
      'type': 'flight-offer',
      'id': '3',
      'source': 'GDS',
      'instantTicketingRequired': False,
      'nonHomogeneous': False,
      'oneWay': False,
      'isUpsellOffer': False,
      'lastTicketingDate': '2025-08-16',
      'lastTicketingDateTime': '2025-08-16',
      'numberOfBookableSeats': 4,
      'itineraries': [
        {
          'duration': 'PT1H35M',
          'segments': [
            {
              'departure': {
                'iataCode': 'LHR',
                'terminal': '4',
                'at': '2025-08-17T15:05:00'
              },
              'arrival': {
                'iataCode': 'ORY',
                'terminal': '3',
                'at': '2025-08-17T17:40:00'
              },
              'carrierCode': 'VY',
              'number': '8961',
              'aircraft': {
                'code': '320'
              },
              'operating': {
                'carrierCode': 'VY'
              },
              'duration': 'PT1H35M',
              'id': '3',
              'numberOfStops': 0,
              'blacklistedInEU': False
            }
          ]
        },
        {
          'duration': 'PT1H35M',
          'segments': [
            {
              'departure': {
                'iataCode': 'ORY',
                'terminal': '1',
                'at': '2025-08-23T13:40:00'
              },
              'arrival': {
                'iataCode': 'LHR',
                'terminal': '4',
                'at': '2025-08-23T14:15:00'
              },
              'carrierCode': 'VY',
              'number': '8960',
              'aircraft': {
                'code': '320'
              },
              'operating': {
                'carrierCode': 'VY'
              },
              'duration': 'PT1H35M',
              'id': '5',
              'numberOfStops': 0,
              'blacklistedInEU': False
            }
          ]
        }
      ],
      'price': {
        'currency': 'EUR',
        'total': '169.03',
        'base': '88.00',
        'fees': [
          {
            'amount': '0.00',
            'type': 'SUPPLIER'
          },
          {
            'amount': '0.00',
            'type': 'TICKETING'
          }
        ],
        'grandTotal': '169.03'
      },
      'pricingOptions': {
        'fareType': [
          'PUBLISHED'
        ],
        'includedCheckedBagsOnly': True
      },
      'validatingAirlineCodes': [
        'VY'
      ],
      'travelerPricings': [
        {
          'travelerId': '1',
          'fareOption': 'STANDARD',
          'travelerType': 'ADULT',
          'price': {
            'currency': 'EUR',
            'total': '169.03',
            'base': '88.00'
          },
          'fareDetailsBySegment': [
            {
              'segmentId': '3',
              'cabin': 'ECONOMY',
              'fareBasis': 'PROPL2VY',
              'class': 'P',
              'includedCheckedBags': {
                'weight': 25,
                'weightUnit': 'KG'
              },
              'includedCabinBags': {
                'quantity': 1
              }
            },
            {
              'segmentId': '5',
              'cabin': 'ECONOMY',
              'fareBasis': 'DROPL2VY',
              'class': 'D',
              'includedCheckedBags': {
                'weight': 25,
                'weightUnit': 'KG'
              },
              'includedCabinBags': {
                'quantity': 1
              }
            }
          ]
        }
      ]
    },
    {
      'type': 'flight-offer',
      'id': '4',
      'source': 'GDS',
      'instantTicketingRequired': False,
      'nonHomogeneous': False,
      'oneWay': False,
      'isUpsellOffer': False,
      'lastTicketingDate': '2025-08-16',
      'lastTicketingDateTime': '2025-08-16',
      'numberOfBookableSeats': 4,
      'itineraries': [
        {
          'duration': 'PT1H25M',
          'segments': [
            {
              'departure': {
                'iataCode': 'LGW',
                'terminal': 'S',
                'at': '2025-08-17T19:40:00'
              },
              'arrival': {
                'iataCode': 'ORY',
                'terminal': '3',
                'at': '2025-08-17T22:05:00'
              },
              'carrierCode': 'VY',
              'number': '8945',
              'aircraft': {
                'code': '320'
              },
              'operating': {
                'carrierCode': 'VY'
              },
              'duration': 'PT1H25M',
              'id': '1',
              'numberOfStops': 0,
              'blacklistedInEU': False
            }
          ]
        },
        {
          'duration': 'PT1H15M',
          'segments': [
            {
              'departure': {
                'iataCode': 'ORY',
                'terminal': '1',
                'at': '2025-08-23T19:15:00'
              },
              'arrival': {
                'iataCode': 'LGW',
                'terminal': 'S',
                'at': '2025-08-23T19:30:00'
              },
              'carrierCode': 'VY',
              'number': '8946',
              'aircraft': {
                'code': '320'
              },
              'operating': {
                'carrierCode': 'VY'
              },
              'duration': 'PT1H15M',
              'id': '4',
              'numberOfStops': 0,
              'blacklistedInEU': False
            }
          ]
        }
      ],
      'price': {
        'currency': 'EUR',
        'total': '183.65',
        'base': '106.00',
        'fees': [
          {
            'amount': '0.00',
            'type': 'SUPPLIER'
          },
          {
            'amount': '0.00',
            'type': 'TICKETING'
          }
        ],
        'grandTotal': '183.65'
      },
      'pricingOptions': {
        'fareType': [
          'PUBLISHED'
        ],
        'includedCheckedBagsOnly': True
      },
      'validatingAirlineCodes': [
        'VY'
      ],
      'travelerPricings': [
        {
          'travelerId': '1',
          'fareOption': 'STANDARD',
          'travelerType': 'ADULT',
          'price': {
            'currency': 'EUR',
            'total': '183.65',
            'base': '106.00'
          },
          'fareDetailsBySegment': [
            {
              'segmentId': '1',
              'cabin': 'ECONOMY',
              'fareBasis': 'PROPLVY',
              'class': 'P',
              'includedCheckedBags': {
                'weight': 25,
                'weightUnit': 'KG'
              },
              'includedCabinBags': {
                'quantity': 1
              }
            },
            {
              'segmentId': '4',
              'cabin': 'ECONOMY',
              'fareBasis': 'AROPLVY',
              'class': 'A',
              'includedCheckedBags': {
                'weight': 25,
                'weightUnit': 'KG'
              },
              'includedCabinBags': {
                'quantity': 1
              }
            }
          ]
        }
      ]
    }
  ],
  'dictionaries': {
    'locations': {
      'ORY': {
        'cityCode': 'PAR',
        'countryCode': 'FR'
      },
      'LHR': {
        'cityCode': 'LON',
        'countryCode': 'GB'
      },
      'LGW': {
        'cityCode': 'LON',
        'countryCode': 'GB'
      }
    },
    'aircraft': {
      '320': 'AIRBUS A320'
    },
    'currencies': {
      'EUR': 'EURO'
    },
    'carriers': {
      'VY': 'VUELING AIRLINES'
    }
  }
}


# for i in range(len(json_data['data'])):
    
#     dates.append(json_data['data'][0]['itineraries'][0]['segments'][0]['departure']['at'])
#     departure_airports.append(json_data['data'][i]['itineraries'][0]['segments'][0]['departure']['iataCode'])
#     prices.append(json_data['data'][i]['price']['total'])
#     arrival_airports.append(json_data['data'][i]['itineraries'][0]['segments'][0]['arrival']['iataCode'])
#     out.append((json_data['data'][i]['itineraries'][0]['segments'][0]['arrival']['at']))



# testing = ['156.65', '158.65', '161.65', '165.65', '167.65', '169.03', '178.03', '179.65', '182.65', '182.65', '191.65', '192.03', '211.59', '212.65', '216.59', '216.59', '216.59', '216.59', '233.59', '233.59', '238.59', '238.59', '238.59', '238.59', '238.59', '238.59', '238.59', '238.59', '266.59', '282.59', '282.59', '282.59', '288.59', '288.59', '288.59', '288.59', '288.59', '288.59', '288.59', '288.59', '288.59', '288.59', '288.59', '288.59', '288.59', '288.59', '337.59', '337.59', '337.59', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41', '458.41'] 

# mini = (min(testing))
# print(testing.index(mini))

























































#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


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
print(response)
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


our_req = {}

for i in range(len(cities)):
    our_req[iata_codes[i]] = [low_prices[i],cities[i]]

print(our_req)

for kv in our_req:
    print(kv)