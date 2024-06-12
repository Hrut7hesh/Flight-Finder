import os
import requests
from dotenv import load_dotenv

load_dotenv()

sheety_endpoint = "https://api.sheety.co/b617313573a68162f1cb7569fa994f2c/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.user = os.environ["SHEETY_USERNAME"]
        self.password = os.environ["SHEETY_PASSWORD"]
        self.authorization = os.environ["SHEETY_AUTH"]
        self.destination_data = {}

    def get_destination_data(self):
        header = {
            "Authorization": self.authorization
        }
        response = requests.get(url=sheety_endpoint, headers=header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        header = {
            "Authorization": self.authorization
        }
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(url=f'{sheety_endpoint}/{city["id"]}', headers=header, json=new_data)


