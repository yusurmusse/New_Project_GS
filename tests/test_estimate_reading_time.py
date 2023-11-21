# Given a expmty string
# It returns a text with estimated 0 minutes to read test

from lib.estimate_reading_time import *

def test_estimate_reading_time_for_an_empty_string():
    result = estimate_reading_time("")
    assert result == 0

# Given a a text with 200 words
# It returns a text with estimated 1 minutes to read test

def test_estimate_reading_time_for_200_words():
    text = "word " * 200
    result = estimate_reading_time(text)
    assert result == 1 


def test_estimate_reading_time_for_100_words():
    text = "word " * 100
    result = estimate_reading_time(text)
    assert result == 0.5

def test_estimate_reading_time_for_400_words():
    text = "word " * 400
    result = estimate_reading_time(text)
    assert result == 2 
    