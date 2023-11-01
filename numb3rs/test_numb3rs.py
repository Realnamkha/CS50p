from numb3ers import validate

def test_range():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("55.55.55.55") == True
    assert validate("555.55.555.55") == False
    assert validate(" ") == False
    assert validate("12.12.") == False

def test_alpha():
    assert validate ('cats.000.dogs.111') == False
    assert validate ('name') == False
