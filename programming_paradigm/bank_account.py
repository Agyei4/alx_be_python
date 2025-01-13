class BankAccount:
    def __init__(self, amount=0):
        self.__amount = float(amount)


    # Deposit method
    def deposit(self,amount):
        self.__amount = self.__amount + amount
        return self.__amount
    
    #withdraw method
    def withdraw(self,amount):
        self.__amount = self.__amount - amount
        return self.__amount
    
    # display_info method
    def display_balance(self):
        print(f"Current Balance: ${self.__amount}")
        return self.__amount


account1= BankAccount(9)
account1.display_balance()
print(account1.withdraw(60))
print(account1.deposit(41))
        