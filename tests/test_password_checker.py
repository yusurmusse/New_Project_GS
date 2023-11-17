import pytest
from lib.password_checker import PasswordChecker

def test_checking_if_password_is_longer_than_8_letters():
    password_checker = PasswordChecker()
    password_choice = password_checker.check("Pinapple")
    assert password_choice == True

def test_checking_if_password_is_shorter_than_8_letter():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_choice = password_checker.check("Oranges")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

#You want to check that the method tests if the password is longer than 8 letters
#If not then, you want it to return the error message. 
#Create an instance.
#Then using .check see if a password longer than 8 returns the outcome.
#Now create another mehtod that checks to see if the password is shorter. 
#if so, print the error message. Input the error code needed to test for error messages in pytest. 
