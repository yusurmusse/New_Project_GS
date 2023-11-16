from lib.string_builder import *

def test__empty_string_building():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

def test_add_to_string_building():
    string_builder = StringBuilder()
    string_builder.add("This")
    string_builder.add(" string")
    string_builder.add(" is")
    string_builder.add(" long")
    assert string_builder.output() == "This string is long"

def test_size_of_string_building():
    string_builder = StringBuilder()
    string_builder.add("This")
    string_builder.add(" string")
    string_builder.add(" is")
    string_builder.add(" long")
    assert string_builder.size() == 19




