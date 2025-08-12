# import datetime
import requests


# response1 = {
#   "exercises": [
#     {
#       "tag_id": 317,
#       "user_input": "ran",
#       "duration_min": 1864.51,
#       "met": 9.8,
#       "nf_calories": 25276.54,
#       "photo": {
#         "highres": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg",
#         "thumb": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg",
#         "is_user_uploaded": False
#       },
#       "compendium_code": 12050,
#       "name": "running",
#       "description": None,
#       "benefits": None
#     }
#   ]
# }


# duration = response1["exercises"][0]["duration_min"]
# calories_burned = response1["exercises"][0]["nf_calories"]
# act = response1["exercises"][0]["name"]



# response2 = {
#   "exercises": [
#     {
#       "name": "push-up",
#       "duration_min": 15.15,
#       "met": 3.8,
#       "calories_burned_kcal": 79.64,
#       "image_url": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/824_highres.jpg"
#     },
#     {
#       "name": "squats",
#       "duration_min": 25.03,
#       "met": 5.0,
#       "calories_burned_kcal": 173.12,
#       "image_url": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/780_highres.jpg"
#     },
#     {
#       "name": "running",
#       "duration_min": 74.58,
#       "met": 9.8,
#       "calories_burned_kcal": 1011.06,
#       "image_url": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg"
#     }
#   ],
#   "total_calories_burned_kcal": 1263.82,
#   "total_duration_min": 114.76
# }




SHEETY_ENDPOINT = "https://api.sheety.co/e******************************9/workoutTracker/workouts"

parameters = {
    "workout": {
        "date": "21/07/2020",
        "time": "15:00:00",
        "exercise": "Running",
        "duration": 22,
        "calories": 130
    }
}

response = requests.post(url=SHEETY_ENDPOINT, json=parameters)
print(response.status_code, response.text)
