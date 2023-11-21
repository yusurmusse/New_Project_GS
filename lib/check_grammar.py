# So that I can improve my grammar
# I want to verify that a text starts with a capital letter 
# and ends with a suitable sentence-ending punctuation mark.
def check_grammar(text):
    text == ""
    punctuation_list = [".", "?", "!"]
    if len(text) == 0 :
        raise ValueError("Cannot check grammar of an empty string.")
    elif text == text.capitalize() and text[-1] in punctuation_list:
        return True
    else:
        return False

    

