import os
import requests
from dotenv import load_dotenv

load_dotenv()
sheety_endpoint = "https://api.sheety.co/b617313573a68162f1cb7569fa994f2c/flightDeals/users"
user = os.environ["SHEETY_USERNAME"]
password = os.environ["SHEETY_PASSWORD"]
authorization = os.environ["SHEETY_AUTH"]
# print('Welcome to Flight Club.')
# print('We find the best flight deals and email you')
# first_name = input('What is your first name?')
# last_name = input('What is your last name?')
# email = input('What is your email?')
# remail = input('Type your email again.')
# if email == remail:
#     params = {
#         'user': {
#             'firstName': first_name,
#             'lastName': last_name,
#             'email': email
#         }
#     }
#     header = {
#         "Authorization": authorization
#     }
#     response = requests.post(url=sheety_endpoint, headers=header, json=params)
#     print(response.text)
#     print('You are in the Club!')

def get_data():
    emails = []
    header = {
        "Authorization": authorization
    }
    response = requests.get(url=sheety_endpoint, headers=header)
    data = response.json()['users']
    for user in data:
        emails.append(user['email'])
    return emails
