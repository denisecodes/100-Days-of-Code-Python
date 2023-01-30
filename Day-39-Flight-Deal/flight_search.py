import requests
import os
import json
from pprint import pprint
from flight_data import FlightData

TEQUILA_LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")

tequila_headers = {
    "Content-Type": "application/json",
    "apikey": TEQUILA_API_KEY,
    "Content-Encoding": "gzip",
}

TEQUILA_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"

class FlightSearch:

    def get_destination_code(self, city_name):
        tequila_params = {
            "term": city_name,
            "location_types": "city"
        }
        city_airport_data = requests.get(url=TEQUILA_LOCATION_ENDPOINT, params=tequila_params, headers=tequila_headers)
        city_airport_data = json.loads(city_airport_data.text)
        code = city_airport_data['locations'][0]['code']
        return code

    def check_flights(self, origin_city_code, destination_city_code, date_from, date_to):
        booking_token = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "dateFrom": date_from,
            "dateTo": date_to,
            "curr": "GBP",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
        }
        response = requests.get(url=TEQUILA_SEARCH_ENDPOINT, params=booking_token, headers=tequila_headers)
        data = response.json()['data'][0]
        #departure_iata_code = (data['flyFrom'])
        #print(departure_iata_code)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        else:
            flight_data = FlightData(
                price=data['price'],
                departure_city_name=data['route'][0]['cityFrom'],
                departure_airport_code=data['route'][0]['flyFrom'],
                arrival_city_name=data['route'][0]['cityTo'],
                arrival_airport_code=data['route'][0]['flyTo'],
                outbound_date=data['route'][0]['local_departure'].split("T")[0],
                inbound_date=data['route'][1]['local_departure'].split("T")[0]
            )
            return flight_data













