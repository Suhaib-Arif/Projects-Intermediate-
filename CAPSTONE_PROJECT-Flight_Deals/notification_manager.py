import os
import requests
from pprint import pprint


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self,Flight_data):
        self.telegram_api_id=os.environ.get("APP API_KEY")
        self.telegram_api_hash=os.environ.get("APP API_HASH")
        self.telegram_api_bot=os.environ.get("TELEGRAM_API_BOT_KEY")
        response = requests.get(url=f"https://api.telegram.org/bot{self.telegram_api_bot}/getMe")
        parameters={
            "chat_id":os.environ.get("USER_ID"),
            "text" : f"Hello\n\nWe have identified a flight for {Flight_data['price']}"
                     f" to fly from {Flight_data['Departure_city_name']} - {Flight_data['Departure_airport_code']}"
                     f" to {Flight_data['Arrival_city_name']} - {Flight_data['Arrival_airport_code']} from "
                     f"{Flight_data['Outbound_date']} to {Flight_data['Inbound_date']} "
        }
        send_message = requests.post(
            url=f"https://api.telegram.org/bot{self.telegram_api_bot}/sendMessage",
            params=parameters
        )



