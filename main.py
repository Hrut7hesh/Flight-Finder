import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"
for row in sheet_data:
    if row['iataCode'] == "":
        row['iataCode'] = flight_search.get_destination_code(row['city'])
        time.sleep(2)
data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
for destination in sheet_data:
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination['lowestPrice']:
        notification_manager.send_emails(cheapest_flight.price, cheapest_flight.origin_airport, cheapest_flight.destination_airport, cheapest_flight.out_date, cheapest_flight.return_date)
        notification_manager.send_message(cheapest_flight.price, cheapest_flight.origin_airport, cheapest_flight.destination_airport, cheapest_flight.out_date, cheapest_flight.return_date)
    time.sleep(2)