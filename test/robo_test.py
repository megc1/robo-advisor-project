import pytest
import os

from app.robo_advisor import to usd(), compile_url(), get_response(), transform_response()

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


