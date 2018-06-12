import requests
import jsonify

class Quotes:
    def __init__(self):
        response = requests.get("https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes")
        self.quotes_list = response.json()

    def get_quotes(self):
        return self.quotes_list

    def get_quote(self, quote_number):
        if quote_number>=len(self.quotes_list["quotes"]):
            raise IndexError()
        return {
            "quote": self.quotes_list["quotes"][quote_number]
        }
