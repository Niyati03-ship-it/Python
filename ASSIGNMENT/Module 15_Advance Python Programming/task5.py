# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid integers.")

except Exception as e:
    print("Unexpected error:", e)



#  Write a Python program to demonstrate handling multiple exceptions.
try:
    numbers = [10, 20, 30]
    index = int(input("Enter index: "))
    value = int(input("Enter value: "))
  
    print(numbers[index] / value)

except IndexError:
    print("Error: Index out of range.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input type.")

except Exception as e:
    print("Unexpected error:", e)
