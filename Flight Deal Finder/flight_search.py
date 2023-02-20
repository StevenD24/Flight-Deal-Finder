import requests
from flight_data import FlightData

TEQUILA_ENDP = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "ENTER YOUR TEQUILA API KEY HERE"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city):
        location_endp = f"{TEQUILA_ENDP}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city, "location_types": "city"}
        response = requests.get(url=location_endp, headers=headers, params=query)
        results = response.json()["locations"]
        IATA_code = results[0]["code"]
        return IATA_code

    def check_flights(self, origin_city_code, dest_city_code, start_time, end_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": dest_city_code,
            "date_from": start_time.strftime("%d/%m/%Y"),
            "date_to": end_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "CAD"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDP}/v2/search",
            headers=headers,
            params=query
        )

        try:
            data = response.json()["data"][0]
        except:
            print(f"No flights found for {dest_city_code}")
            return None

        flight_data = FlightData(
            price=data["price"],
            start_city=data["route"][0]["cityFrom"],
            start_airport=data["route"][0]["flyFrom"],
            dest_city=data["route"][0]["cityTo"],
            dest_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.dest_city}: ${flight_data.price}")
        return flight_data
