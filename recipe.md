<!-- estimate_reading_time.py -->
1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, 
assuming that I can read 200 words a minute.

2. Design the Function Signature

Include the name of the function, its parameters, return value, and side effects.


def estimate_reading_time_for_a_text(text):
    """calculates the estimated reading time for given

    Parameters: 
        text: a string containing words (e.g. "I want to find out how long it takes me to read a text in minutes")

    Returns: (state the return value and its type)
        a string that returns the estimated time it takes to read a text 
        (e.g. The estimated time it takes to read this text is: "insert float" minutes.)

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.

3. Create Examples as Tests

Make a list of examples of what the function will take and return.


"""
Given a expmty string
It returns a text with estimated 0 minutes to read test
"""
estimate_readting_time("")
result = 0

"""
Given a a text with 200 words
It returns a text with estimated 1 minutes to read test
"""
estimate_reading_time(text....200 words)
result = 1

"""
Given a text with 100 words 
It returns the estimated time of 0.5 minutes because it takes 1 minute to read 200 words
"""
estimate_readting_time(text....100 words)
result = 0.5
"""
Given a text with 400 words 
It returns the estimated time of 2 minutes because it takes 1 minute to read 200 words
"""
estimate_readting_time(text....400 words)
result = 2
"""


4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.




Ensure all test function names are unique, otherwise pytest will ignore them!









<!-- check_grammar.py -->
1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

- If the sentence is more than one, treat it like one. 

2. Design the Function Signature

Include the name of the function, its parameters, return value, and side effects.


def check_grammar(text):
    """Start sentences with uppercase and ends with a full stop.

    Parameters: (list all parameters and their types)
        text: a string containing words 

    Returns: boolean true or false 

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """

    pass # Test-driving means _not_ writing any code here yet.

3. Create Examples as Tests

Make a list of examples of what the function will take and return.

"""
Given a string of text with no uppercases or punctuation 
It returns a False
"""
check_grammar_in_sentence("hi there i am writing my paragraph with no grammar and it needs fixing immediately")
returns False

"""
Given a string of text starts with capital letters and ends with a full stop.
It returns a True
"""
check_grammar("Hi there i am writing my paragraph with no grammar and it needs fixing immediately.")
returns True

"""
Given a string of text starts with capital letters and no full stop.
It returns a False
"""
check_grammar("Hi there i am writing my paragraph with no grammar and it needs fixing immediately")
returns False

"""
Given a string of text starts with capital letters and ends with a another punctuation mark.
It returns a True
"""
check_grammar("Hi there i am writing my paragraph with no grammar and it needs fixing immediately!")
returns True

"""
Given a string that has a full stop but does not start with a capital letter
It returns a False
"""
check_grammar("hi there i am writing my paragraph with no grammar and it needs fixing immediately.")
returns False

"""
Given a empty string of text 
It returns a error
"""
check_grammar("")
returns error_message("cannot check grammar of an empty string") 

4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.








<!--TODO Challenge-->
1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO..

Only check for the string #TODO in uppercase.

2. Design the Function Signature

Include the name of the function, its parameters, return value, and side effects.

def check_if_string_has_TODO(text):
    """Checks if #TODO is in a text and check if it written in uppercase

    Parameters: (list all parameters and their types)
        text: a string containing words 

    Returns: (state the return value and its type)
        a boolean - True or false 
        True if the text #TODO is in the string 
        False if the text #TODO is not in the string

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.

3. Create Examples as Tests

Make a list of examples of what the function will take and return.


"""
Given "#TODO" is present in string
It returns True
"""
TODO_checker("#TODO: task is to complete challenge one in chapter one.") 
=> return True

"""
Given "#TODO" is not present in string
It returns False
"""
TODO_checker("task is to complete challenge one in chapter one.") 
=> return False

"""
Given "#TODO" is present in string more than once
It returns True
"""
TODO_checker("#TODO: task is to complete challenge one in chapter one. #TODO: second task is to complete challenge two in chapter two.") 
=> return True

"""
Given "#todo" is present in string as lowercase
It returns False
"""
TODO_checker("#todo: task is to complete challenge one in chapter one.") 
=> return False

"""
Given "TODO" is present in string without the hashtag
It returns False
"""
TODO_checker("TODO: task is to complete challenge one in chapter one.") 
=> return False

"""
Given an empty string
It returns error message "There are no #TODO tasks"
"""
TODO_checker("") 
=> "There are no #TODO tasks"


4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.
