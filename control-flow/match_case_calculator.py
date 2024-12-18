#script to perform basic calculations using the match_case in python

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+,-,*,/): ")

match operation:
    case "+":
        print(f"The results {num1 + num2}.")
    case "-":
        print(f"The results {num1 - num2}.")
    case "*":
        print(f"The results {num1 * num2}.")
    case "/":
        if num2 !=0:
            print(f"The results {num1 / num2}.")
        else:
            print("Cannot divide by zero")
    case _:
        print("nvalid operation")