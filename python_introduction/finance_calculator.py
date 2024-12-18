
monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your monthly expenses: ")

#store monthly savings into a variable
monthly_savings = float(monthly_income) - float(monthly_expenses)

simple_annual_rate = 0.05

#projected annual savings 
projected_savings = int((monthly_savings * 12) + (monthly_savings * 12 * 0.05))

#displaying results
print("Your monthly savings are $" + str(monthly_savings))
print("Projected savings after one year, with interest, is: $" + str(projected_savings))

#value = input("Enter a value (number or string): ")

#match value:
 #   case int():
  #      print("You entered an integer:", value)
   # case str():
    #    print("You entered a string:", value)
    #case _:
 #   print("Invalid data type entered.")
'''/tmp/correction/7846408885091857796125801896665235067311_5/100739/780490/python_introduction/finance_calculator.py doesn't contain 
     monthly_savings\s*=\s*(monthly_income\s*-\s*monthly_expenses|float\s*\(\s*monthly_income\s*\)\s*-\s*float\s*\(\s*monthly_expenses\s*\))'''
