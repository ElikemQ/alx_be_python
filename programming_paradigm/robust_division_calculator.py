def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        print("Error: Please enter numeric values only.")
        return
    except TypeError:
        print("Error: Please enter numeric values only.")
        return

    try:
        if denominator == 0:
            print(ZeroDivisionError("Error: Cannot divide by zero."))
        return f"The result of the division is {numerator/denominator}"
    except ZeroDivisionError as e:
        print(f"Error: Cannot divide by zero. {e}")
        return