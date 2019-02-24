# app/robo_advisor.py
#REFERENCE: used Prof. Rossetti's screencast

import requests
import json



request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response = requests.get(request_url)
# print(type(response)) # <class 'requests.models.Response'>
# print(response.status_code) #>200
# print(response.text)
# TODO: write some Python code here to produce the desired functionality...

parsed_response = json.loads(response.text)
breakpoint()


print("-----------------------")
print("STOCK SYMBOL: AMZN")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("LATEST CLOSING PRICE: $1,259.19")

# ... etc.
