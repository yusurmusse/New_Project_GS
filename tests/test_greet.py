# The line below means importing everything (*) from lib greet to the test_greet file.
# Now you want to test out the code so you would put test_...()
# What do you want from the fucntion 
# assert result == (what is the outcome the code is supposed to give)

from lib.greet import greet
def test_greet_by_their_name():
    result = greet("Yusur")
    assert result == "Hello, Yusur!"

