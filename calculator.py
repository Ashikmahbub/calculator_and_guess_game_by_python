# Simple Calculator Program
# Author: Ashik Mahbub
# Date: 2025-10-05
# Description: A simple calculator that performs basic arithmetic operations.
# Ostad Django React Course Batch 7
# Module 6 - Project 1

# --- Function Definitions ---

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y

def modulus(x, y):
    if y == 0:
        raise ZeroDivisionError("Modulus by zero is not allowed.")
    return x % y

# --- Main Program ---

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

try:
    choice = input("Enter choice (1/2/3/4/5): ").strip()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result:.2f}")
    elif choice == '5':
        result = modulus(num1, num2)
        print(f"{num1} % {num2} = {result}")
    else:
        print("Invalid operation choice. Please select between 1 to 5.")

except ValueError:
    print("Invalid input. Please enter numeric values only.")
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
