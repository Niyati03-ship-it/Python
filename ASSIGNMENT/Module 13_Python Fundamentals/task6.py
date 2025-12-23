# Write a generator function that generates the first 10 even numbers.

def numbers():
    for i in range(1, 11):
        yield i * 2

# Using the generator
for num in numbers():
    print(num)