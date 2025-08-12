import requests
import datetime
from requests.auth import HTTPBasicAuth
import base64

# CONSTANTS

APP_ID = "f******6"
API_KEY = "b******************************7"

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")


user_input = str(input("Tell me which exercises you did : "))



headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY, 
    "Content-Type":"application/json"
}

parameters = {
    "query" : user_input,
    "gender" : "male",
    "weight_kg" : 83,
    "height_cm" : 179,
    "age" : 26
}

result = (requests.post(url=nutri_endpoint,json=parameters, headers=headers)).json()


SHEETY_ENDPOINT = "https://api.sheety.co/e7*****************************9/workoutTracker/workouts"

credentials = f"{"JRX"}:{"your_password"}"
encoded = base64.b64encode(credentials.encode()).decode()

headers = {
    "Authorization": f"Basic {encoded}"
}



for exercises in result["exercises"]:
    parameters2 = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercises["name"].title(),
            "duration": exercises["duration_min"],
            "calories": exercises["nf_calories"]
        }
    }
    into_sheet = requests.post(url=SHEETY_ENDPOINT, json=parameters2, headers=headers)

print(into_sheet.json())