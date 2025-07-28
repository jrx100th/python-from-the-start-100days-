# making a request to ISS location API

import requests
from datetime import datetime
iss = "http://api.open-notify.org/iss-now.json"
# response = requests.get(url=iss)
# response.raise_for_status()

# data = response.json()
# print(data["iss_position"])

sun = "https://api.sunrise-sunset.org/json"

MY_LAT = 23.259933
MY_LONG = 77.412613
parameters = { 
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0
}
# the parameter will be in the form of dictionary
response = requests.get(sun, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = (data["results"]["sunrise"]) # in 12 hour format
sunset = (data["results"]["sunset"]) # in 12 hour format

time_now = datetime.now() # in 24 hour format 

sunrise_hour = (sunrise.split("T")[1].split(":")[0])
sunset_hour = (sunset.split("T")[1].split(":")[0])
print(sunrise_hour)
print(sunset_hour)
print(time_now.hour)