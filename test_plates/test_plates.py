from plates import is_valid

def test_start():
    assert is_valid("a") == False
    assert is_valid("11") == False
    assert is_valid("1") == False
    assert is_valid("AA") == True
    assert is_valid("CS50") == True


def test_length():
    assert is_valid("AAAAAAAAA") == False
    assert is_valid("AAAA") == True
    assert is_valid("A") == False
    assert is_valid("aaaaaa") == True

def test_numbers():
    assert is_valid("AA11") == True
    assert is_valid("11AA") == False
    assert is_valid("A11AA") == False
    assert is_valid("AA123") == True


def test_zero():
    assert is_valid("00") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


def test_symbols():
    assert is_valid("CS50!") == False
    assert is_valid("3.14") == False
