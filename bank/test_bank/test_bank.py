from bank import value

def test_value():
    assert value("What's up?") == "$100"

def test_case_insensitivity():
    assert value("HELLO") == "$0"
    assert value("hello") == "$0"


def test_all():
    assert value("Hello, Namkha") == 0
    assert value("Greetings, Namkha") == 100
    assert value("Hi, Namkha") == 20

