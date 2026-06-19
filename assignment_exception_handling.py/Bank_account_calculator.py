class InsufficientFundsError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive!")

        self.balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive!")

        if amount > self.balance:
            raise InsufficientFundsError("Insufficient balance!")

        self.balance -= amount
        print(f"Withdrawn ₹{amount}")

    def show_balance(self):
        print(f"Current Balance: ₹{self.balance}")


account = BankAccount(1000)

transactions = [
    ("deposit", 500),
    ("withdraw", 200),
    ("withdraw", 2000),
    ("deposit", -100),
    ("withdraw", 100)
]

for action, amount in transactions:
    try:
        if action == "deposit":
            account.deposit(amount)

        elif action == "withdraw":
            account.withdraw(amount)

        account.show_balance()

    except (InsufficientFundsError, InvalidAmountError) as e:
        print("Error:", e)