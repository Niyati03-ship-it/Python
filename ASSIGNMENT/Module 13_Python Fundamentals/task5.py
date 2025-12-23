#program-1
#Write a Python program to print each fruit in a list using a simple for loop
# Define the list of fruits
list1 = ['apple', 'banana', 'mango']

# Use a for loop to print each fruit
for fruit in list1:
    print(fruit)



#program-2
#Write a Python program to find the length of each string in List1.
# Define the list of strings
list1 = ['apple', 'banana', 'mango']

# Use a for loop to find the length of each string
for fruit in list1:
    length = len(fruit)
    print(length)



#program-3
#Write a Python program to find a specific string in the list using a simple for loop and if condition. 
# Define a list of fruits
list1 = ['apple', 'banana', 'mango', 'orange']

# Define the string to search
search_item = 'banana'

# Use a for loop to search
found = False  # flag to check if found

for fruit in list1:
    if fruit == search_item:
        print(search_item, "is found in the list.")
        found = True
        break

if not found:
    print(search_item, "is not found in the list.")



#program-4
# Print pattern using nested for loop:
for i in range(1,6):
    #i=1
    for j in range(1,i+1):
        print("*", end="")
    
    print()