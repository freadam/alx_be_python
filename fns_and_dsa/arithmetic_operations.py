def perform_operation(num1: float, num2: float, operation: str)-> float:
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
    return result
