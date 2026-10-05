class InsufficientFundsError(Exception):
    pass


class NegativeAmountError(Exception):
    pass


class BankAccount:
    def __init__(self, account_id, initial_balance):
        self.account_id = account_id
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise NegativeAmountError("Amount must be positive")

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise NegativeAmountError("Amount must be positive")

        if amount > self.__balance:
            raise InsufficientFundsError("Insufficient balance")

        self.__balance -= amount

    def get_balance(self):
        return self.__balance


acc = BankAccount("ACC1001", 500.0)

acc.deposit(200.0)
acc.withdraw(300.0)

print(acc.get_balance())