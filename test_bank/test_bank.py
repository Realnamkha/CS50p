from bank import bank.py

def test_value():
    assert bank.value("hello Namkha") == "$0"
    assert bank.value("h Namkha") == "$20"
    assert bank.value("HELLO NAMKHA") == "$0"
    assert bank.value("1230") =="$100"
    assert bank.value("a,yui") == "$100"