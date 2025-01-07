# function with basic arithmetic operations

def perform_operation(num1,num2,operation):
    """performs basic arithmetic operations 
    between number1 and number2"""

    match operation:
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

    return result