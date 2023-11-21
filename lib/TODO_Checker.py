# As a user
# So that I can keep track of my tasks
# I want to check if a text includes the string #TODO
# Only check for the string #TODO in uppercase.

def TODO_checker(text):
    if "#TODO" in text:
        return True
    elif text == "":
        raise ValueError("There are no #TODO tasks.")
    else:
        return False