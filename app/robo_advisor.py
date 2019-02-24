# app/robo_advisor.py
#REFERENCE: used Prof. Rossetti's screencast

import requests
import json
from datetime import datetime

#function adapted from previous projects/Prof.Rossetti's screencast

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response = requests.get(request_url)
# print(type(response)) # <class 'requests.models.Response'>
# print(response.status_code) #>200
# print(response.text)
# TODO: write some Python code here to produce the desired functionality...

parsed_response = json.loads(response.text)
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
latest_close = parsed_response["Time Series (Daily)"]["2019-02-20"]["4. close"]
#breakpoint()


print("-----------------------")
print("STOCK SYMBOL: AMZN")
print("-----------------------")
print("REQUESTING STOCK MARKET DATA...")
#Referenced datetime documentation: https://docs.python.org/3/library/datetime.html
#Referenced datetime strftime behavior documentation: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
print("REQUEST AT: ", datetime.now().strftime('%m-%d-%Y %H:%M:%S'))
print("-----------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print("RECENT HIGH: $1,222.00")
print("RECENT LOW: $999.00")
print("-----------------------")
print("RECOMMENDATION: BUY!")
print("BECAUSE: TODO")
print("-----------------------")
print("HAPPY INVESTING!")
print("-----------------------")


# ... etc.
