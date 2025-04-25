class BankAccount:
    def __init__(self):
        self.__balance = 0
    def deposit(self, amount):
        if amount <= 0:
            print("Сумма должна быть больше нуля")
        else:
            self.__balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма должна быть больше нуля")
        elif amount > self.__balance:
            print("Недостаточно средств")
        else:
            self.__balance -= amount
    def get_balance(self):
        return self.__balance
account = BankAccount()
account.deposit(2)
account.withdraw(3)
account.withdraw(-1)
print(account.get_balance())
