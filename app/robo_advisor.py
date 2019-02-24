# app/robo_advisor.py
#REFERENCE: used Prof. Rossetti's screencast

import requests
import json
from datetime import datetime
import csv
import os

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
tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys()) #assuming first day is in 0 position, may need to sort if not
latest_day = dates[0]
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
latest_close = parsed_response["Time Series (Daily)"][latest_day]["4. close"]
#Referenced notes on dictionaries: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/datatypes/dictionaries.md
high_prices = []
low_prices = []
for date in dates:
    high_price = float(tsd[date]["2. high"])
    high_prices.append(high_price)
    low_price = float(tsd[date]["3. low"])
    low_prices.append(low_price)

recent_high = max(high_prices)
recent_low = min(low_prices)


    
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
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-----------------------")
print("RECOMMENDATION: BUY!")
print("-----------------------")
print("BECAUSE: TODO")
print("-----------------------")

#Referenced csv notes: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/e2d64e2d74621f3ff070175954878ba3f1562388/notes/python/modules/csv.md
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")
csv_headers = ["timestamp", "open", "high", "low", "close", "volume" ]
with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()
    for date in dates: 
        prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": prices["1. open"],
            "high": prices["2. high"],
            "low": prices["3. low"],
            "close": prices["4. close"],
            "volume": prices["5. volume"]
    })

print("WRITING DATA TO CSV: " + str(csv_file_path))
print("-----------------------")
print("HAPPY INVESTING!")
print("-----------------------")
 
# ... etc.
