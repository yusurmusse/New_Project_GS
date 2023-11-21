import pytest
from lib.check_grammar import check_grammar

# Given a string of text with no uppercases or punctuation 
# It returns a False
def test_check_grammar_in_sentence_with_no_capital_letter_at_start_and_no_punctuation_at_end():
    result = check_grammar("hi there i am writing my paragraph with no grammar and it needs fixing immediately")
    assert result == False

# Given a string of text starts with capital letters and ends with a full stop.
# It returns a True
def test_check_grammar_in_sentence_with_capital_letter_at_start_and_fullstop_at_end():
    result = check_grammar("Hi there i am writing my paragraph with no grammar and it needs fixing immediately.")
    assert result == True

# Given a string of text starts with capital letters and ends with a question mark.
# It returns a True
def test_check_grammar_in_sentence_with_capital_letter_at_start_and_question_mark_at_end():
    result = check_grammar("Hi there i am writing my paragraph with no grammar and i need some help, could you help me fix it?")
    assert result == True

# Given a string of text starts with capital letters and ends with a exclamation mark.
# It returns a True
def test_check_grammar_in_sentence_with_capital_letter_at_start_and_punctuation_at_end():
    result = check_grammar("Hi there i am writing my paragraph with no grammar and it needs fixing immediately!")
    assert result == True

# Given a string of text starts with capital letters and no punctuation.
# It returns a False
def test_check_grammar_in_sentence_with_capital_letter_at_start_and_no_punctuation_at_end():
    result = check_grammar("Hi there i am writing my paragraph with no grammar and it needs fixing immediately")
    assert result == False


# Given a string that has a full stop oer any ending punctuation but does not start with a capital letter
# It returns a False
def test_check_grammar_in_sentence_with_no_capital_letter_at_start_and_fullstop_at_end():
    result = check_grammar("hi there i am writing my paragraph with no grammar and it needs fixing immediately.")
    assert result == False

# Given a empty string of text 
# It returns a error
def test_check_grammar_for_empty_string():
    with pytest.raises(ValueError) as e:
        check_grammar("")
    error_message = str(e.value)
    assert error_message == "Cannot check grammar of an empty string."

