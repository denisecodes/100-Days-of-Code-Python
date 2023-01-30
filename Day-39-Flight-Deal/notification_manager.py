from twilio.rest import Client
import os
from flight_data import FlightData

account_sid = "AC4ddd0868bf10e1c086383096c8a12cf6"
auth_token = os.environ.get("AUTH_TOKEN")
twilio_phone_number = os.environ.get("TWILIO_NUM")

class NotificationManager:

    def __init__(self, flight_data: FlightData):
        self.flight_info = flight_data

    def send_low_price_text(self):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Low price alert! Only £{self.flight_info.price} to fly from {self.flight_info.departure_city_name[0]}-"
                 f"{self.flight_info.departure_airport_code[0]} to {self.flight_info.arrival_city_name[0]}-"
                 f"{self.flight_info.arrival_airport_code[0]}, from {self.flight_info.outbound_date} to "
                 f"{self.flight_info.inbound_date}.",
            from_=twilio_phone_number,
            to='+447706371382'
        )
        print(message.status)