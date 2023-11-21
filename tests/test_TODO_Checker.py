import pytest
from lib.TODO_Checker import TODO_checker

# Given "#TODO" is present in string
# It returns True
# """
# TODO_checker("#TODO: task is to complete challenge one in chapter one.") 
# => return True
def test_check_if_TODO_is_present_in_string():
    result = TODO_checker("#TODO: task is to complete challenge one in chapter one.")
    assert result == True

# Given "#TODO" is not present in string
# It returns False
# """
# TODO_checker("task is to complete challenge one in chapter one.") 
# => return False
def test_check_if_TODO_is_not_present_in_string():
    result = TODO_checker("task is to complete challenge one in chapter one.")
    assert result == False

# Given "#TODO" is present in string more than once
# It returns True
# """
# TODO_checker("#TODO: task is to complete challenge one in chapter one. #TODO: second task is to complete challenge two in chapter two.") 
# => return True
def test_check_if_TODO_is_present_in_string_more_than_once():
    result = TODO_checker("#TODO: task is to complete challenge one in chapter one. #TODO: second task is to complete challenge two in chapter two.") 
    assert result == True

# Given "#todo" is present in string as lowercase
# It returns False
# """
# TODO_checker("#todo: task is to complete challenge one in chapter one.") 
# => return False
def test_check_if_TODO_is_present_in_string_as_lowercase():
    result = TODO_checker("#todo: task is to complete challenge one in chapter one.")
    assert result == False

# Given "TODO" is present in string without the hashtag
# It returns False
# """
# TODO_checker("TODO: task is to complete challenge one in chapter one.") 
# => return False
def test_check_if_TODO_is_present_in_string_without_hashtag():
    result = TODO_checker("TODO: task is to complete challenge one in chapter one.")
    assert result == False

# Given an empty string
# It returns error message "There are no #TODO tasks"
# """
# TODO_checker("") 
# => "There are no #TODO tasks"
def test_check_if_string_is_empty():
    with pytest.raises(Exception) as e:
        TODO_checker("")
    error_message = str(e.value)
    assert error_message == "There are no #TODO tasks."
    

