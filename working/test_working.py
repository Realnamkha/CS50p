from working import convert

def test_extreme():
    assert("12:00 AM to 5:00 PM") == "00:00 to 17:00"
    assert("12:00 AM to 5:00 PM") == "17:00 to 00:00"
