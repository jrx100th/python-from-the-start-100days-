import requests
from datetime import datetime, timedelta
import random

USERNAME = "******"
TOKEN = "q**************h"
GRAPH_ID = "g****1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Active Coding",
    "unit" : "File Count",
    "type" : "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config,headers=headers)
# print(response.text)

today = datetime(year=2025, month=8, day=4)
# print(today.strftime("%Y%m%d"))


pixel_creation_endpoint = "https://pixe.la/v1/users/*****/graphs/******"
pixel_creation_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "5",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_params, headers=headers)
# print(response.status_code)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pix_put = {
    "quantity" : "3"
}


# response = requests.put(url=update_endpoint,json=pix_put,headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

def pixel_shitpostin(days : int):
    for i in range(days):
        prev_day = today - timedelta(days=i)
        prev_day = prev_day.strftime('%Y%m%d')
        pixel_creation_params_func = {
            "date" : prev_day,
            "quantity" : str(random.randint(0,100)*30),
        }
        response = requests.post(url=pixel_creation_endpoint,json=pixel_creation_params_func,headers=headers)
        print(response.text)

pixel_shitpostin(300)