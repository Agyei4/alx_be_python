from tornado.gen import Return


class BankAccount:
    def __init__(self, current_balance=0):
        self.__current_balance = float(current_balance)


    # Deposit method
    def deposit(self,amount):
        self.__current_balance = self.__current_balance + amount
        return self.__current_balance
    
    #withdraw method
    def withdraw(self,amount):
        self.__current_balance = self.__current_balance - amount
        return self.__current_balance
    
    # display_info method
    def display_balance(self):
        print(f"Current Balance: ${self.__current_balance}")
        return self.__current_balance

#
# account1= BankAccount(9)
# account1.display_balance()
# print(account1.withdraw(60))
# print(account1.deposit(41))
#