import pytest

from app.robo_advisor import to usd(), compile_url()

def test_to_usd():
    assert to_usd(12312312) == "$123,123.12"

def test_compile_url():
    assert compile_url(AMZN) == f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker_input}&apikey={api_key}"