import requests
import os
from pprint import pprint
from datetime import datetime,timedelta

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,city_name):
        self.city = city_name
        self.flightapikey = os.environ.get("FLIGHT_API_KEY")
        self.flight_endpoint=os.environ.get("FLIGHT_ENDPOINT")

    def iata_code(self):
        header={
            "apikey":self.flightapikey,
        }
        parameters = {
            "term": self.city
        }

        response=requests.get(url=f"{self.flight_endpoint}locations/query",params=parameters,headers=header)
        response.raise_for_status()
        return response.json()['locations'][0]['code']

    def flight_information(self,FLY_TO):

        datefrom = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        dateto = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")


        return_from = (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y")
        return_to = (datetime.now() + timedelta(days=28)).strftime("%d/%m/%Y")

        header = {
            "apikey":self.flightapikey,
            "Content-Type": "application/json",
            "Content-Encoding":"gzip"

        }

        parameter={
            # "apikey": self.flightapikey,
            "fly_from": "LON",
            "fly_to": FLY_TO,
            "date_from": datefrom,
            "date_to": dateto,
            "curr":"GBP",
            "return_from":return_from,
            "return_to":return_to
        }

        response=requests.get(url=f"{self.flight_endpoint}v2/search",params=parameter,headers=header)

        flight_data=response.json()

        flight_data_dict={
            "price": flight_data['data'][3]['price'],
            "Departure_city_name":flight_data['data'][1]['cityFrom'],
            "Departure_airport_code":flight_data['data'][1]['flyFrom'],
            "Arrival_city_name":flight_data['data'][2]["cityTo"],
            "Arrival_airport_code":flight_data['data'][2]["flyTo"],
            "Outbound_date":str(flight_data['data'][1]["local_arrival"]).split("T")[0],
            "Inbound_date":str(flight_data['data'][1]["local_departure"]).split("T")[0]
        }


        return flight_data_dict



