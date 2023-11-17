import pytest
from lib.present import Present

def test_wrap_then_unwrap_present():
    present = Present()
    present.wrap("Surprise! Happy Birthday!")
    assert present.unwrap() == "Surprise! Happy Birthday!"

def test_unwrap_then_wrap_present():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_wrap_already_wrapped_present():
    present = Present()
    present.wrap("Surprise! Happy Birthday!")
    with pytest.raises(Exception) as e:
        present.wrap("Surprise! Happy Birthday Again!")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

# test_wrap_then_unwrap_present:
# Creates a Present instance.
# Calls the wrap method to wrap the present with the specified contents.
# Calls the unwrap method to unwrap the present.
# Asserts that the unwrapped contents match the expected string.

# test_unwrap_then_wrap_present:
# Creates a Present instance.
# Attempts to unwrap the present without wrapping it first.
# Uses pytest.raises to capture the exception raised (an instance of Exception).
# Converts the exception to a string to extract the error message.
# Asserts that the error message matches the expected message for unwrapping an empty present.

#test_wrap_already_wrapped_present:
# Creates a Present instance.
# Wraps the present with the first set of contents.
# Attempts to wrap the present again with a different set of contents.
# Uses pytest.raises to capture the exception raised (an instance of Exception).
# Converts the exception to a string to extract the error message.
# Asserts that the error message matches the expected message for attempting to wrap an already wrapped present.
