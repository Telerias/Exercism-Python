'''
Use String methods
str.lower() to convert to lowercase

After solving, reviewed solutions and Tahnan's solution using sets is more elegant:
---
from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)

def is_pangram(string):
    return ALPHABET.issubset(string.lower())
---

So, on the right path with strings and sets, but more to learn

'''
from string import ascii_lowercase as asc_lower

def is_pangram(sentence):
    sentence = sentence.lower() # convert to lower case
    return set(asc_lower) - set(sentence) == set([])





