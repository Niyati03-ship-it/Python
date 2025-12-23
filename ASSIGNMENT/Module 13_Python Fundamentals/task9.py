# Write a Python program to demonstrate string slicing.
# Define a string
text = "Python Programming"

# Various slicing examples
print("Original string:", text)
print("1. From index 0 to 5:", text[0:6])           # 'Python'
print("2. From index 7 to end:", text[7:])          # 'Programming'
print("3. Full string using [:]:", text[:])         # Entire string
print("4. Last 5 characters:", text[-5:])           # 'mming'
print("5. Every 2nd character:", text[::2])         # Skips every other character
print("6. String in reverse:", text[::-1])          # Reversed string




# Write a Python program that manipulates and prints strings using various string methods.
#string
s = "python programming"
print(s)
print(s.capitalize()) #capitalize first letter of first word
print(s.upper())   #all words print in capital
print(s.lower())   #all words print in small
print(s.swapcase())  #all words print in capital
print(s.index("t"))   #index number start from 0 so t = 2
print(s.count("p"))   #count that how many "p" in sentence
print(s.title())      #print a "s"
print(s.isalpha())   #boolean (true or false) "s" is alpha or not
print(len(s))       #length of "s"
print(s.center(26,"*"))   #print star before and after sentence
