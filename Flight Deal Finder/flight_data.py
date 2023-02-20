class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self, price, start_city, start_airport, dest_city, dest_airport, out_date, return_date):
        self.price = price
        self.start_city = start_city
        self.start_airport = start_airport
        self.dest_city = dest_city
        self.dest_airport = dest_airport
        self.out_date = out_date
        self.return_date = return_date
