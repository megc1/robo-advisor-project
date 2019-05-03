#REFERENCE: used Prof. Rossetti's screencast
import requests
import json
from datetime import datetime
import csv
import os
from dotenv import load_dotenv

#function adapted from previous projects/Prof.Rossetti's screencast
#Basic Challenge: formatting prices (done)
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

url_lookup = ""
#Basic Challenge: Compiling request URLs
def compile_url(ticker_input):
    url_lookup = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker_input}&apikey={api_key}"
    return url_lookup

#Intermediate Challenge: Issuing API Requests
def get_response(ticker):
    this_url = compile_url(ticker)
    response = requests.get(this_url)
    parsed_response = json.loads(response.text)
    return parsed_response

#USER INPUT VALIDATION:
while True:
    ticker_symbol = input("Which stock would you like to evaluate? Please enter its ticker symbol here: ")
    #Makes sure input values are alphabetical
    #referenced Geeks for Geeks: https://www.geeksforgeeks.org/python-string-isalpha-application/
    if not ticker_symbol.isalpha():
        print("That doesn't seem to be a valid stock symbol. Please check its formatting and try again. ")
    else:
        #Referenced os module notes: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/7b43ab256e6b79f231f56c0bbf29025325a9414d/notes/python/modules/os.md
        get_response(ticker_symbol)
        #Referenced: http://docs.python-requests.org/en/master/user/quickstart/
        #adapted Error checking from Hiep's solution: https://github.com/hiepnguyen034/robo-stock/blob/master/robo_advisor.py 
    if "error" in get_response(ticker_symbol).text:
        print("Uh oh! Looks like that stock isn't here. Please restart the program and try another if you'd like.")
    else:
        break
while True:
    acceptable_risk = input("How much risk are you willing to accept? Please enter a number between one and ten, with one being very low risk and ten being very high risk. ")
    if 1<= float(acceptable_risk) <= 10 :
       break 
    else:
        print("Sorry, that is not a valid level of risk. Please try again.")  

#Intermediate Challenge: Processing API Responses
#TODO: write out function
def transform_response(parsed_response):
    tsd = parsed_response["Time Series (Daily)"]
    rows = []
    # adapted from Prof. Rossetti's example solution:
    for date, daily_prices in tsd.items():
        row = {
            "timestamp" : date,
            "open": float(daily_prices["1. open"]),
            "high": float(daily_prices["2. high"]),
            "low": float(daily_prices["3. low"]),
            "close": float(daily_prices["4. close"]),
            "volume": int(daily_prices["5. volume"])
        }
        rows.append(row)
    return rows

#Intermediate Challenge: Writing to CSV
#TODO: write out function
#Referenced csv notes: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/e2d64e2d74621f3ff070175954878ba3f1562388/notes/python/modules/csv.md
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

def write_to_csv(rows, csv_file_path):
    csv_headers = ["timestamp", "open", "high", "low", "close", "volume" ]
    with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    


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

dates = list(tsd.keys()) 
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



print("-----------------------")
print("STOCK SYMBOL: " + ticker_symbol)
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
recommend = " "
risk_percentage = float(acceptable_risk)/20
if (float(latest_close) - float(recent_low))/float(recent_low) > risk_percentage:
    recommend = "Do not buy. Stock risk as calculated based on latest closing price and recent lowest price is higher than desired."
else:
    recommend = "Buy! Risk as calculated based on latest closing price and recent lowest price is within preferred range."

print("RECOMMENDATION: " + recommend)
print("-----------------------")




print("WRITING DATA TO CSV: " + str(csv_file_path))
print("-----------------------")
while True:
     show_graph = input("Would you like to view a graphical representation of this stock's price activity? Enter Y or N.")
     if show_graph != "Y" and show_graph != "N":
         print("Sorry, that's not a valid response. Please enter Y or N.")
     else:
         if show_graph == "N":
                break
         if show_graph == "Y":
                print("Note: Once you have viewed your results, please close the graph window to end the program.") #show() function presents script from continuing until window is closed -- haven't found a workaround for that so adapted user behavior for now
                #REFERENCED: https://matplotlib.org/users/pyplot_tutorial.html
                import matplotlib
                import matplotlib.pyplot as plt
                import matplotlib.ticker as ticker

                plotprices = []
                #Referenced: https://www.programiz.com/python-programming/methods/built-in/sorted
                plotdates = sorted(dates)

                for d in dates:
                    close_price = tsd[d]['4. close']
                    plotprices.append(float(close_price))

                fig, ax = plt.subplots()

                #Axis formatting adapted from: https://matplotlib.org/gallery/ticks_and_spines/major_minor_demo.html
                #Partly adapted from https://www.programcreek.com/python/example/100917/matplotlib.ticker.LinearLocator
                ax.xaxis.set_major_locator(plt.LinearLocator(8))
                
 
                #Adapted from: https://matplotlib.org/gallery/pyplots/dollar_ticks.html
                formatter = ticker.FormatStrFormatter('$%1.2f')
                ax.yaxis.set_major_formatter(formatter)
                
                
                plt.plot(plotdates, plotprices)
                #REFERENCED: https://matplotlib.org/gallery/subplots_axes_and_figures/figure_title.html
                plt.xlabel('Date')
                plt.ylabel('Close Price')
                plt.title('Closing Stock Prices: ' + ticker_symbol)
                plt.show()
                print("Happy investing!")
                print("-----------------------")
                break
 
