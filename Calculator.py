# Basic Calculator Program

# Ask user for two numbers and the operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform calculation based on the operation
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation! Please use +, -, *, or /.")
# Enter the numbers and operation to see the result.
# Number inputs should be valid numbers.
# The program handles division by zero and invalid operations gracefully.   

# Example usage:
# Enter the first number: 10    
# Enter the second number: 5
# Enter the operation (+, -, *, /): /

