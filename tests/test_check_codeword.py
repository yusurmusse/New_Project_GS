# The line below means importing everything (*) from lib greet to the test_greet file.
# Now you want to test out the code so you would put test_...()
# What do you want from the fucntion 
# assert result == (what is the outcome the code is supposed to give)

from lib.check_codeword import check_codeword
def test_checking_the_right_codewords():
    result = check_codeword('horse')
    assert result == 'Correct! Come in.'

def test_checking_if_codewords_close():
    result = check_codeword('hose')
    assert result == 'Close, but nope.'

def test_checking_the_wrong_codewords():
    result = check_codeword('donkey')
    assert result == 'WRONG'
