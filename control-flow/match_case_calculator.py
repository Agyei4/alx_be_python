#script to perform basic calculations using the match_case in python

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+,-,*,/): ")

match operation:
    case "+":
        print(f"The result is {num1 + num2}.")
    case "-":
        print(f"The result is {num1 - num2}.")
    case "*":
        print(f"The result is {num1 * num2}.")
    case "/":
        if num2 !=0:
            print(f"The result is {num1 / num2}.")
        else:
            print("Cannot divide by zero")
    case _:
        print("nvalid operation")

    # /tmp/correction/0406700595438154161345791944928232116214_5/100740/780490/
    # control-flow/match_case_calculator.py doesn't contain
    # print\(\s*f?['\"]The result is