try:
    # Taking input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    # Checking operator and performing operation
    if operator == '+':
        result = num1 + num2

    elif operator == '-':
        result = num1 - num2

    elif operator == '*':
        result = num1 * num2

    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError
        result = num1 / num2

    else:
        raise ValueError("Invalid Operator")

    print("Result:", result)

except ValueError as ve:
    print("Error: Invalid number or operator entered")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

except Exception:
    print("Error: Something went wrong")
