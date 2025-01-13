class BankAccount:
    def __init__(self, amount):
        self.__amount = amount


    # Deposit method
    def deposit(self,amount):
        self.amount = self.amount + amount
        return amount
    
    #withdraw method
    def withdraw(self, amount):
        self.amount = self.amount - amount
        return amount
    
    # display_info method
    def display_balance(self):
        print(f"Current Balance: ${self.amount}")
        return self.amount



        