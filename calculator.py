# Welcome to the Fun Calculator!
# We're going to add, subtract, multiply, and divide two numbers like a boss! 

# Input the first number
num1 = float(input("Enter the first number: "))

# Input the second number
num2 = float(input("Enter the second number: "))

# Operation
operation = input("Enter the operation (+, -, *, /): ")

# Calculate based on operation
if operation == '+':
    answer = num1 + num2
    print(f"Sum: {num1} + {num2} = {answer}")  # ➕
elif operation == '-':
    answer = num1 - num2
    print(f"Difference: {num1} - {num2} = {answer}")  # ➖
elif operation == '*':
    answer = num1 * num2
    print(f"Product: {num1} × {num2} = {answer}")  # ✖️
elif operation == '/':
    if num2 == 0:
        print("Error! Division by zero is not allowed!")  # ➗
    else:
        answer = num1 / num2
        print(f"Quotient: {num1} / {num2} = {answer}")  # ➗
else:
    print("Invalid operation! Please use +, -, *, or /")
