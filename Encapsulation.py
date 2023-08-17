#It resists access to certain attributes and
#methods to prevent direct modification
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if amount > 0 and amount <= 1000000:
            self.__balance+=amount
    def get_balance(self):
        return self.__balance
account=BankAccount(2500)
account.deposit(350)
print("Balance", account.get_balance())