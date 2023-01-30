import requests
import os

sheety_get_endpoint = os.environ.get("SHEETY_GET_ENDPOINT")
sheety_put_endpoint = os.environ.get("SHEETY_POST_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": SHEETY_TOKEN
}

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_get_endpoint, headers=sheety_headers)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_put_endpoint}/{city['id']}", json=new_data,
                                        headers=sheety_headers)
            print(response.text)

