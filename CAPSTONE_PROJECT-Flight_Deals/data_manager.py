import os
import requests
from pprint import pprint

class DataManager:
    def __init__(self):
        self.Sheet_get_endpoint=os.environ.get("SHEET_GET")
        self.Sheet_post_endpoint=os.environ.get("SHEET_POST")
        self.Sheet_put_endpoint=os.environ.get("SHEET_PUT")
        self.header={
            "Authorization":os.environ.get("SHEET_AUTHOURIZATION")
        }

    def acquire_sheet_data(self):
        response=requests.get(url=self.Sheet_get_endpoint,headers=self.header)
        response.raise_for_status()
        result=response.json()
        return result['prices']

    def update_data(self,updated_sheet_data):
        for item in updated_sheet_data:
            updated_sheet_put_endpoint=f"{self.Sheet_put_endpoint}/{item['id']}"

            parameter={
                "price":item
            }
            response=requests.put(url=updated_sheet_put_endpoint,json=parameter,headers=self.header)

            response.raise_for_status()

