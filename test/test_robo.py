import pytest
import os

from app.robo_advisor import to_usd, compile_url, get_response, transform_response, write_to_csv

def test_to_usd():
    assert to_usd(123123) == "$123,123.00"

def test_compile_url():
    ticker = 'AMZN'
    assert ticker in compile_url(ticker)
    assert 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' in compile_url(ticker)

def test_get_response():
    ticker = "MSFT"
    parsed_response = get_response(ticker)
    #referenced Prof. Rossetti's example code to get line 19
    assert isinstance(parsed_response, dict)
    assert "Meta Data" in parsed_response.keys()
    assert "Time Series (Daily)" in parsed_response.keys()
    assert parsed_response["Meta Data"]["2. Symbol"] == ticker

def test_transform_response():
    parsed_response = {
        "Meta Data": {
            "1. Information": "Daily Prices (open, high, low, close) and Volumes",
            "2. Symbol": "MSFT",
            "3. Last Refreshed": "2019-05-01",
            "4. Output Size": "Full size",
            "5. Time Zone": "US/Eastern"
        },
        "Time Series (Daily)": {
            "2019-05-31": {
                "1. open": "123.4500",
                "2. high": "123.8900",
                "3. low": "120.3400",
                "4. close": "123.5600",
                "5. volume": "12345678"
            },
            "2019-05-30": {
                "1. open": "124.5600",
                "2. high": "124.8900",
                "3. low": "123.3400",
                "4. close": "124.5600",
                "5. volume": "22345678"
            },
            "2019-05-29": {
                "1. open": "122.4500",
                "2. high": "122.8900",
                "3. low": "121.3400",
                "4. close": "122.5600",
                "5. volume": "32345678"
            }
        }
    }
    #Referenced Prof. Rossetti's solution
    transformed_response = [
        {"timestamp": "2019-05-31", "open": 123.4500, "high": 123.8900, "low": 120.3400, "close": 123.5600, "volume": 12345678},
        {"timestamp": "2019-05-30", "open": 124.5600, "high": 124.8900, "low": 123.3400, "close": 124.5600, "volume": 22345678},
        {"timestamp": "2019-05-29", "open": 122.4500, "high": 122.8900, "low": 121.3400, "close": 122.5600, "volume": 32345678},
    ]
    assert transform_response(parsed_response) == transformed_response

def test_write_to_csv():
    test_rows = [
        {"timestamp": "2019-06-08", "open": "101.0924", "high": "101.9500", "low": "100.5400", "close": "101.6300", "volume": "22165128"},
        {"timestamp": "2019-06-07", "open": "102.6500", "high": "102.6900", "low": "100.3800", "close": "100.8800", "volume": "28232197"},
        {"timestamp": "2019-06-06", "open": "102.4800", "high": "102.6000", "low": "101.9000", "close": "102.4900", "volume": "21122917"},
        {"timestamp": "2019-06-05", "open": "102.0000", "high": "102.3300", "low": "101.5300", "close": "102.1900", "volume": "23514402"},
        {"timestamp": "2019-06-04", "open": "101.2600", "high": "101.8600", "low": "100.8510", "close": "101.6700", "volume": "27281623"},
        {"timestamp": "2019-06-01", "open": '99.2798',  "high": "100.8600", "low": "99.1700",  "close": "100.7900", "volume": "28655624"}
    ]
    #referenced and adapted row data from Prof. Rossetti's solution
    csv_file_path = os.path.join(os.path.dirname(__file__), "test_prices.csv")
    #TODO: add test_reports and test_prices csv files to test on
    if os.path.isfile(csv_file_path):
        os.remove(csv_file_path)
    result = write_to_csv(test_rows, csv_file_path)
    assert result == True
    assert os.path.isfile(csv_file_path) == True