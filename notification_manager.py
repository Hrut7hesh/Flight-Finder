import os
import smtplib
from dotenv import load_dotenv
from twilio.rest import Client
from sheety import get_data

emails = get_data()

load_dotenv()
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.environ["TWILLIO_SID"]
        self.auth_token = os.environ["TWILLIO_AUTH"]
        self.twilio_no = os.environ["TWILLIO_NO"]
        self.verified_no = os.environ["MY_NO"]
        self.MY_EMAIL = os.environ["MY_EMAIL"]
        self.PASSWORD = os.environ["PASSWORD"]

    def send_message(self, price, origin_airport, destination_airport, out_date, return_date):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
            body=f"Low Price Alert! Only £{price} to  fly from {origin_airport} to {destination_airport}, on {out_date} until {return_date}",
            from_='+13256665950',
            to='+919949853122'
        )
        print(message.sid)

    def send_emails(self, price, origin_airport, destination_airport, out_date, return_date):
        for email in emails:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=self.MY_EMAIL, password=self.PASSWORD)
                connection.sendmail(
                    from_addr=self.MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:Low Price Flights for {destination_airport} \n\nLow Price Alert! Only {price} euros to fly from {origin_airport} to {destination_airport}, on {out_date} until {return_date}"
                )

