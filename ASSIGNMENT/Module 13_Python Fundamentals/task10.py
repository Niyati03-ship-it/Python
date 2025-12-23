# Write a Python program to apply the map() function to square a list of numbers.


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)


# Write a Python program that uses reduce() to find the product of a list of numbers.

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)

print("Product of the list:", product)



# Write a Python program that filters out even numbers using the filter() function.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Original numbers:", numbers)
print("Even numbers:", even_numbers)


