import requests
import jsonify
import random

class Quotes:
    def __init__(self):
        response = requests.get(
            "https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes")
        self.quotes_list = response.json()

    def get_quotes(self) -> dict:
        return self.quotes_list

    def get_quote(self, quote_number: int) -> dict:
        try:
            if quote_number<1:
                raise IndexError()
            return {
                "quote": self.quotes_list["quotes"][quote_number-1]
            }
        except IndexError as e:
            return "indexes must be between 1 and " + str(len(self.quotes_list['quotes']))

    def get_random_quote(self) -> dict:
        quotes_number = len(self.quotes_list["quotes"])
        random_number = random.randint(0,quotes_number-1)
        return {
            "quote": self.quotes_list["quotes"][random_number]
        }
