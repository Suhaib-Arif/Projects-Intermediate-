#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

sheet=DataManager()
sheet_data=sheet.acquire_sheet_data()

for data in sheet_data:
    flightsearch=FlightSearch(data['city'])
    data['iataCode']=flightsearch.iata_code()
    flight_data_dict=flightsearch.flight_information(data['iataCode'])
    if flight_data_dict["price"] < data['lowestPrice']:
        send_msg = NotificationManager(flight_data_dict)
    print(data)

sheet.update_data(sheet_data)


