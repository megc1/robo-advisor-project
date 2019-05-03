import pytest

from app.robo_advisor import to usd()

def test_to_usd():
    assert to_usd(12312312) == "$123,123.12"