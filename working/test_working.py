from working import convert
import pytest
def test_extreme():
    assert convert("12:00 AM to 5:00 PM") == "00:00 to 17:00"
    assert convert("5:00 PM to 12:00 AM") == "17:00 to 00:00"
    assert convert("12 AM to 5 PM") == "00:00 to 17:00"
    assert convert("12:00 AM to 5:00 PM") != "12:00 to 17:00"

def test_input():
    with pytest.raises(ValueError):
         convert('09:00 AM - 7:00 PM')
    with pytest.raises(ValueError):
         convert('9 AM - 5 PM')
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')

def test_range():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
