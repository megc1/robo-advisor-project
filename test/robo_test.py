import pytest
import os

from app.robo_advisor import to usd(), compile_url()



def test_to_usd():
    assert to_usd(12312312) == "$123,123.12"

def test_compile_url():
    assert 'AMZN' in compile_url(AMZN)
    assert 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' in compile_url(AMZN)
    