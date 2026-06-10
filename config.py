import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Token
TELEGRAM_TOKEN = "8921633484:AAFGKVcrOcyk7RqSowU0-6Udq3WMi2CSesM"

# Cat API Token
CAT_API_TOKEN = "live_6ROlQvVZ9tYGa2qd7wQmRC6GErrZbp9FOY0L0dLZklkDC9moAWwVnovGfevw90IS"

# Dog API Token
DOG_TOKEN = "live_8hhF71zER09iJyQKHrjysvJVyHmA0QeKO4ywWcVMNwDf4kV8gF6JkkK20PCbQwAK"

pass

import requests
class CardClient:
    def __init__(self):
        self.base_url = "https://randommer.io"

    def get_card(self):
        url = f"{self.base_url}/api/Card/"

        headers = {
            "X-Api-Key": "27ed4274794b4b8f970d384778f42752"
        }
        query_params = {
            "type": "Visa",
        }

        response = requests.get(url, headers=headers, params=query_params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None


    def get_get_card_types(self):
        url = f"{self.base_url}/api/Card/Types"

        headers = {
            "X-Api-Key": "27ed4274794b4b8f970d384778f42752"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None


client = CardClient()
print(client.get_card())
print(client.get_get_card_types())