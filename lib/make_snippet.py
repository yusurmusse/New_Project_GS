#Make a string as an argument 
#and returns the first five words and then a '...' 
#if there are more than that.

def make_snippet(word):
    split_words = word.split()
    if len(split_words) > 5:
        first_five_words = split_words[:5]
        words_joined = " ".join(first_five_words)
        return words_joined + "..."
    else:
        return word
    
    