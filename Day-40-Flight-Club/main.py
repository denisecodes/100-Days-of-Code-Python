from data_manager import DataManager
from pprint import pprint
import datetime as dt
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

today = dt.date.today()
tomorrow = today + dt.timedelta(days=1)
tomorrow = tomorrow.strftime(f"%d/%m/%Y")
six_months_from_now = today + dt.timedelta(days=(6 * 30))
six_months_from_now = six_months_from_now.strftime(f"%d/%m/%Y")

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        data_manager.update_destination_codes()
        data_manager.destination_data = sheet_data
        print(sheet_data)

for destination in sheet_data:
    flight_data = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        tomorrow,
        six_months_from_now
    )
    if flight_data is None:
        continue
    if flight_data.price < destination['lowestPrice']:
        if flight_data.stop_overs > 0:
            notification_manager = NotificationManager(flight_data)
            notification_manager.send_stop_over_text()
        notification_manager = NotificationManager(flight_data)
        notification_manager.send_low_price_text()




