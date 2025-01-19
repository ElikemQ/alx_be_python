def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        print("Error: Please enter numeric values only.")

    try:
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        return f"The result of the division is {numerator/denominator}"
    except ZeroDivisionError as e:
        print(f"Error: {e}")