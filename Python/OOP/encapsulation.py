class Bank:
    def __init__(self, account , balance):
        self.__balance = balance
        self.account = account

    def desposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount")

    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid amount")

    def get_balance(self):
        return self.__balance

account1 = Bank("123456", 1000)
print(account1.get_balance())
account1.desposit(100)
print(account1.get_balance())
account1.withdraw(500)
print(account1.get_balance())

# print(account1.balance)
# print(account1.account)