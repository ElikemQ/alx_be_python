def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        return print("Error: Please enter numeric values only.")
    except TypeError:
        return print("Error: Please enter numeric values only.")

    try:
        if denominator == 0:

            return print("Error: Cannot divide by zero.")
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return print(f"Error: Cannot divide by zero.")
    