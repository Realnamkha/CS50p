from plates import is_valid

def test_len():
    is_valid("A") == False
    is_valid("AA") == True
    is_valid("CCCCCC") == False
    is_valid("AAAAAAAAA") == False

def test_alnumber():
    is_valid("CS50") == True
    is_valid("CS05") == False