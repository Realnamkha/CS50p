from fuel import convert, gauge

def test_input():
    assert convert("cats/dogs") == "X or Y is not an integer"
    assert convert("1/0") == "Y cannot be zero"
    assert convert("2/1") == 

