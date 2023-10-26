from twttr import shorten
def test_str():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("bcdz") == "bcdz"
    assert shorten("1230") =="1230"
    assert shorten("a,yui") == ",y"