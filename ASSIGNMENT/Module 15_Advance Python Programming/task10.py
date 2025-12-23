#  Write a Python program to search for a word in a string using re.search().

import re

text = "Python is a powerful programming language."
word = "powerful"

match = re.search(word, text)

if match:
    print(f"'{word}' found in the text!")
else:
    print(f"'{word}' not found in the text.")



#  Write a Python program to match a word in a string using re.match().


import re

text = "Python is a powerful programming language."
word = "Python"


match = re.match(word, text)

if match:
    print(f"'{word}' matched at the beginning of the text!")
else:
    print(f"'{word}' did not match at the beginning.")
