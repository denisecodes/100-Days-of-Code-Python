import requests
from datetime import datetime as dt
import os

USERNAME = "denisecodes"
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph2"

# Create a pixela account

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
#see if ressponse is successful
# print(response.text)

# Create a graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph2",
    "name": "Badminton Graph",
    "unit": "kcal",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
#print(response.text)

post_a_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = dt.now()
today_date = today.strftime("%Y%m%d")

pixel_params = {
    "date": today_date,
    "quantity": input("How many calories did you burn from badminton today? ")
}

response = requests.post(url=post_a_pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

# Update data using put method

update_pixel_endpoint = f"{post_a_pixel_endpoint}/{today.strftime('%Y%m%d')}"

update_data = {
    "quantity": "7.5"
}

#response = requests.put(url=update_pixel_endpoint, json=update_data, headers=headers)
#print(response.text)

# Delete data using delete method

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

#response = requests.delete(url=delete_pixel_endpoint, headers=headers)
#print(response.text)