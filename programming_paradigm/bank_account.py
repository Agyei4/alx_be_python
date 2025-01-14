#from tornado.gen import Return

class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            raise Return(True)
        raise Return(False)

    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")  #["Current Balance:"]
#
# account1= BankAccount(9)
# account1.display_balance()
# print(account1.withdraw(60))
# print(account1.deposit(41))
#
