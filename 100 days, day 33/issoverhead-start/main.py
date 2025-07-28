import requests
from datetime import datetime
import smtplib
import time 


MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

user = "chn"
pwd = "jsvp"

response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
response1.raise_for_status()
data = response1.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response2 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response2.raise_for_status()
data = response2.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if (sunset < time_now.hour < sunrise) and (((MY_LAT)-5) < iss_latitude <((MY_LAT)+5) and ((MY_LONG)-5) < iss_longitude <((MY_LONG)+5)):
        connection = smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login(user=user, password=pwd)
        connection.sendmail(from_addr=user,to_addrs=user,msg="Subject:ISS is heading towards you\n\nSo now go look up since it is dark outside")

## now the code is running in the background and this is going to be executed every 60 seconds

