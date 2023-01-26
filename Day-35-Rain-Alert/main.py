import requests
import os
from twilio.rest import Client

account_sid = "AC4ddd0868bf10e1c086383096c8a12cf6"
auth_token = os.environ.get("AUTH_TOKEN")
twilio_phone_number = os.environ.get("TWILIO_NUM")
api_key = os.environ.get("API_KEY")

parameters = {
    "lat": "51.507351",
    "lon": "-0.127758",
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour in weather_slice:
    condition_code = hour["weather"][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an ☔️",
        from_= twilio_phone_number,
        to='+447706371382'
    )
    print(message.status)


