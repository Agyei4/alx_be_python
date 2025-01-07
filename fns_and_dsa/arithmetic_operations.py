# function with basic arithmetic operations

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
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        
    

  
    return result


# Test

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