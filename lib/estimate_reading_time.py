# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, 
# assuming that I can read 200 words a minute.

def estimate_reading_time(text):
    words = text.split()
    word_count = len(words)
    return word_count / 200
