# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user for an operation
operation = input("Enter an operation (+, -, *, /): ")

# Perform the operation and print the result
if operation == "+":
    print(f"The result of {num1} + {num2} is: {num1 + num2}")
elif operation == "-":
    print(f"The result of {num1} - {num2} is: {num1 - num2}")
elif operation == "*":
    print(f"The result of {num1} * {num2} is: {num1 * num2}")
elif operation == "/":
    if num2 != 0:
        print(f"The result of {num1} / {num2} is: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, or /.")
