from lib.make_snippet import make_snippet

def test_to_return_empty_string():
    result = make_snippet("")
    assert result == ""

def test_to_return_one_word():
    result = make_snippet("one two")
    assert result == "one two"

def test_to_return_five_word():
    result = make_snippet("one two three four five")
    assert result == "one two three four five"

def test_return_dots_at_end_of_string_after_five_words():
    result = make_snippet("one two three four five six")
    assert result == "one two three four five..."




