from working import convert

def test_extreme():
    assert("12:00 AM to 5:00 PM") == "00:00 to 17:00"
    assert("12:00 AM to 5:00 PM") == "17:00 to 00:00"
    assert("12 AM to 5 PM") == "00:00 to 17:00"
    assert("12:00 AM to 5:00 PM") != "12:00 to 17:00"

def test_input():
    assert("12:00AM to 5:00PM") == raise ValueError
