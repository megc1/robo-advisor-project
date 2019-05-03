import pytest
import os

from app.robo_advisor import to usd(), compile_url(), get_response(), transform_response(), write_to_csv()

def test_to_usd():
    assert to_usd(12312312) == "$123,123.12"

def test_compile_url():
    assert 'AMZN' in compile_url(AMZN)
    assert 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' in compile_url(AMZN)

def test_get_response():
    ticker = "MSFT"
    parsed_response = get_response(ticker)
    #referenced Prof. Rossetti's example code to get line 19
    assert isinstance(parsed_response, dict)
    assert "Meta Data" in parsed_response.keys()
    assert "Time Series (Daily)" in parsed_response.keys()
    assert parsed_response["Meta Data"]["2. Symbol"] == symbol

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

