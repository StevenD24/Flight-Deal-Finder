import requests

SHEETY_DATA = "https://api.sheety.co/d1c0fe79995aafd54f20df2bc2457864/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.dest_data = {}

    def get_destination_data(self):
        # The Sheety API gets all the data in the sheet
        response = requests.get(url=SHEETY_DATA)
        data = response.json()
        self.dest_data = data["prices"]
        return self.dest_data

    def update_destination_codes(self):

        for city in self.dest_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_DATA}/{city['id']}",
                json=new_data
            )
            print(response.text)
