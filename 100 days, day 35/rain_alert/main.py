import requests
from keys import api_key, twilio_account_sid, twilio_auth_token, twilio_phone_number, my_ph_no
from twilio.rest import Client

site = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "appid": api_key,
    "lat": 15354,
    "lon": 547,
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
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        body="There is a high probability of raining\nSo take the required precautions, (Umbrella ☔☔☔)",
        from_=twilio_phone_number,
        to=my_ph_no
    )
    print(f"SMS sent. Status: {message.status}")
else:
    print("No rain predicted in the next forecast periods.")

# print(ids)