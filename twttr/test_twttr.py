from twttr import shorten
def test_str():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("bcdz") == "bcdz"