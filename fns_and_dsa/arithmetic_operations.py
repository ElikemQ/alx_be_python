def perform_operation(num1, num2, operation):
    if operation == 'add':
        return f"Result: {num1 + num2}" 
    elif operation == 'subtract':
        return f"Result: {num1 - num2}"
    elif operation == 'multiply':
        return f"Result: {num1 * num2}"
    elif operation == 'divide':
        if num2 != 0:
            return f"Result: {num1 / num2}"
        else:
            return('Can not divide by zero')
    else:
        return('Operation not found')

