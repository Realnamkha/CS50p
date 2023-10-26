from fuel import convert, gauge

def test_input():
    assert convert("1/3") == "33"
    assert convert("1/2") == "50"
    
