from fuel import convert, gauge

def test_value():
    with pytest.raises(ValueError):
        convert("cats/dogs")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

