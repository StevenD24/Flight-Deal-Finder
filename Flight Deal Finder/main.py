from notification_manager import NotificationManager
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY = "YYC"

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch

    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.dest_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_months_time = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY,
        destination["iataCode"],
        start_time=tomorrow,
        end_time=six_months_time
    )

    try:
        if flight.price < destination['lowestPrice']:
            notification_manager.send_sms(
                msg=f"Flight deal update! Only ${flight.price} to fly from {flight.start_city}-"
                    f"{flight.start_airport} to "
                    f"{flight.dest_city}-{flight.dest_airport}, from {flight.out_date} to "
                    f"{flight.return_date} :)"
            )
    except:
        continue
