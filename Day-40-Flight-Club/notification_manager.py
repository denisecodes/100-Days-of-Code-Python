from twilio.rest import Client
import os
from flight_data import FlightData
import smtplib
import requests

flight_link = "https://www.google.co.uk/flights?hl=en#flt="

sheety_email_endpoint = os.environ.get("SHEETY_USERS_ENDPOINT")
sheety_token = os.environ.get("SHEETY_TOKEN")

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": sheety_token
}

class NotificationManager:

    def __init__(self, flight_data: FlightData):
        self.flight_info = flight_data
        self.body = ""
        self.user_info = []
        self.flight_link = f"{flight_link}{self.flight_info.departure_airport_code[0]}." \
             f"{self.flight_info.arrival_airport_code[0]}.{self.flight_info.outbound_date}*" \
             f"{self.flight_info.arrival_airport_code[0]}.{self.flight_info.departure_airport_code[0]}." \
             f"{self.flight_info.inbound_date}"

    def send_low_price_text(self):
        #Includes body text and flight link
        self.body = f"Low price alert! Only £{self.flight_info.price} to fly from {self.flight_info.departure_city_name[0]}-" \
             f"{self.flight_info.departure_airport_code[0]} to {self.flight_info.arrival_city_name[0]}-" \
             f"{self.flight_info.arrival_airport_code[0]}, from {self.flight_info.outbound_date} to " \
             f"{self.flight_info.inbound_date}.\n{self.flight_link}"
        self.send_emails(self.body)

    def send_stop_over_text(self):
        self.body = f"Low price alert! Only £{self.flight_info.price} to fly from {self.flight_info.departure_city_name[0]}" \
             f"{self.flight_info.departure_airport_code[0]} to {self.flight_info.arrival_city_name[0]}" \
             f"{self.flight_info.arrival_airport_code[0]}, from {self.flight_info.outbound_date} to" \
             f"{self.flight_info.inbound_date}.\nFlight has 1 stop over, via" \
             f"{self.flight_info.via_city}\n{self.flight_link}"
        self.send_emails(self.body)


    def send_emails(self, body):
        response = requests.get(url=sheety_email_endpoint, headers=sheety_headers)
        data = response.json()
        self.user_info = data['users']
        for row in self.user_info:
            user_email = row['email']
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                my_email = os.environ.get("MY_EMAIL")
                password = os.environ.get("MY_PASSWORD")
                connection.login(user=my_email, password=password)
                connection.sendmail(
                        from_addr=my_email,
                        to_addrs=f"{user_email}",
                        msg=f"Subject:Low flight price alert!\n\n{body}".encode('utf-8')
                )


