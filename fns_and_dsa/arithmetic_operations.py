# function with basic arithmetic operations
from pluggy import Result
from scipy.special import result


def perform_operation(num1,num2,operation):
    """performs basic arithmetic operations 
    between number1 and number2"""

# ["num1, num2, operation"]
    if operation == "add":
        result = num1 + num2
    
    elif operation == "subtract":
        result = num1 - num2
    
    elif operation == "multiply":
        result = num1 * num2
    
    elif operation == "divide":
        if num2 == 0:
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("Cannot divide by zero.")
        else:
            result = num1 / num2




  
    return result


# Test
print(perform_operation(2,1,"divide"))

""" match operation:
        case "add":      
            result = num1 + num2
        case "subtract": 
            result = num1 - num2
        case "multiply": 
            result = num1 * num2
        case "divide":   
            result = num1 / num2
        case _: 
            result = "invalid operation"
"""