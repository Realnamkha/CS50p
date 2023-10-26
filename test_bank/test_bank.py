from bank import value

def test_value():
    assert value("hello Namkha") == "$0"
    assert value("h Namkha") == "$20"
    assert shorten("HELLO NAMKHA") == "$0"
    assert shorten("1230") =="$100"
    assert shorten("a,yui") == "$100"