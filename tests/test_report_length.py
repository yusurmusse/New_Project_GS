from lib.report_length import *

def test_report_length_of_string():
    result = report_length("supercalifragilistic")
    assert result == "This string was 20 characters long."

# what do you want to get out of the report_length.py
# first import it (from lib.~~~ import *)
# what are you trying to define. In this case the report length of string. (dont forget to add test)
# result is the string you test it out with 
# assert result is the output that should come from the length of result you inputed. 