# Write a Python program to update a value in a dictionary.

# Dictionary
dict = {
    "id": 101,
    "name": "Niyati",
    "age": 19
}

dict["age"] = 20

print(dict)



# Write a Python program to merge two lists into one dictionary using a loop.

keys = ["id", "name", "age"]
values = [101, "Niyati", 20]
dict = {}

for i in range(len(keys)):
    dict[keys[i]] = values[i]

print(dict)
