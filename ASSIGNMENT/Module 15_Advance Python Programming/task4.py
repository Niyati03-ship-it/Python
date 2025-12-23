# Write a Python program to read the contents of a file and print them on the console.

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

#  Write a Python program to write multiple strings into a file

file = open("lines.txt", "w")

file.write("Hello World\n")
file.write("Welcome to Python\n")
file.write("File handling example\n")

file.close()
print("Multiple strings written successfully.")
