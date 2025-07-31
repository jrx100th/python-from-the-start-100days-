import os

api_key = os.environ.get("api_key")


site = "https://api.openweathermap.org/data/2.5/weather?ppid=1e74ab307cc85"

twilio_auth_token = os.environ.get("twilio_auth_token")
twilio_account_sid = os.environ.get("twilio_account_sid")
twilio_phone_number = os.environ.get("twilio_phone_number")
my_ph_no = os.environ.get("my_ph_no")







import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

site = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "appid": api_key,
    "lat": 2848,
    "lon": 8***37,
    "cnt": 4
}

response = requests.get(url=site, params=parameters)
data = response.json()

ids = []

rain = False  # Initialize the rain flag

for i in range(4):
    _id = data["list"][i]["weather"][0]["id"]
    ids.append(_id)
    if _id < 800:
        rain = True

if rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(twilio_account_sid, twilio_auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="There is a high probability of raining\nSo take the required precautions, (Umbrella ☔☔☔)",
        from_=twilio_phone_number,
        to=my_ph_no
    )
    print(f"SMS sent. Status: {message.status}")
else:
    print("No rain predicted in the next forecast periods.")

print(ids)