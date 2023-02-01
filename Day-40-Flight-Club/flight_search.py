import requests
import os
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

    def __init__(self):
        self.city_codes = []

    def get_destination_code(self, city_names):
        for city in city_names:
            tequila_params = {
                "term": city,
                "location_types": "city"
            }
            response = requests.get(url=TEQUILA_LOCATION_ENDPOINT, params=tequila_params, headers=tequila_headers)
            results = response.json()['locations']
            code = results[0]['code']
            self.city_codes.append(code)

        return self.city_codes

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
            "max_stopovers": 0
        }
        response = requests.get(url=TEQUILA_SEARCH_ENDPOINT, params=booking_token, headers=tequila_headers)
        try:
            data = response.json()["data"][0]
        except IndexError:
            booking_token["max_stopovers"] = 2
            response = requests.get(url=TEQUILA_SEARCH_ENDPOINT, params=booking_token, headers=tequila_headers)
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data['price'],
                departure_city_name=data['route'][0]['cityFrom'],
                departure_airport_code=data['route'][0]['flyFrom'],
                arrival_city_name=data['route'][1]['cityTo'],
                arrival_airport_code=data['route'][1]['cityCodeTo'],
                outbound_date=data['route'][0]['local_departure'].split("T")[0],
                inbound_date=data['route'][2]['local_departure'].split("T")[0],
                stop_overs=2,
                via_city=data['route'][0]['cityTo']
            )
            return flight_data
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













