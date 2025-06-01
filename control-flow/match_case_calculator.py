# Get user input for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

# Perform the calculation using match-case
match operation:
    case '+':
        result = num1 + num2
        print(f"Result: {num1} + {num2} is {result}.")
    case '-':
        result = num1 - num2
        print(f"Result: {num1} - {num2} is {result}.")
    case '*':
        result = num1 * num2
        print(f"Result: {num1} * {num2} is {result}.")
    case '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed")
        else:
            result = num1 / num2
            print(f"Reuslt: {num1} / {num2} = {result}")
    case _:
        print("Invalid opearation! Please choose from +, -, *, or /.")