'''
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

#store monthly savings into a variable
monthly_saving = int(monthly_income - monthly_expenses)

simple_annual_rate = 0.05

#projected annual savings 
projected_savings = int((monthly_saving * 12) + (monthly_saving * 12 * 0.05))

#displaying results
print("Your monthly savings are $" + str(monthly_saving))
print("Projected savings after one year, with interest, is: $" + str(projected_savings))'''

value = input("Enter a value (number or string): ")

match value:
    case int():
        print("You entered an integer:", value)
    case str():
        print("You entered a string:", value)
    case _:
        print("Invalid data type entered.")