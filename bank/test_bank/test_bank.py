from bank import value

def test_value():
    assert value("hello Namkha") == "$0"
    assert value("h Namkha") == "$20"
    # assert value("HELLO NAMKHA") == "$0"
    assert value("1230") =="$100"
    assert value("a,yui") == "$100"