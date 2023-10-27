from fuel import convert, gauge
import pytest
def test_value():
    with pytest.raises(ValueError):
        convert("cats/dogs")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

# def test_greater():
#     with pytest.raises(e):
#         convert("3/1")
def test_convert():
    assert convert("0/4") == 0
    assert convert("1/2") == 50
    assert convert("4/4") == 100

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(10) == "10%"
    assert gauge(90) == "90%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
