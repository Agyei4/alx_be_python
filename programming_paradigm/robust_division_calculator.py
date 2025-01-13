def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
    except ZeroDivisionError:
           print("Error: Cannot divide by zero.")
    except ValueError:
         result ="Error: Please enter numeric values only."
    else:
         result = f"The result of the division is {result}"