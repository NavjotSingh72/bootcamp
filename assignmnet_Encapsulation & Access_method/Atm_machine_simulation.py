class ATM:
    def __init__(self, pin, owner, balance=0):
        self.__pin = pin              
        self.__balance = balance      
        self._owner = owner           
        self.__authenticated = False

    def authenticate(self, pin):
        if pin == self.__pin:
            self.__authenticated = True
            print("Authentication Successful")
        else:
            print("Invalid PIN")

    def deposit(self, amt):
        if not self.__authenticated:
            raise ValueError("Please authenticate first")

        if amt <= 0:
            raise ValueError("Invalid amount")

        self.__balance += amt
        print(f"₹{amt} deposited successfully")

    def withdraw(self, amt):
        if not self.__authenticated:
            raise ValueError("Please authenticate first")

        if amt <= 0:
            raise ValueError("Invalid amount")

        if amt > 20000:
            raise ValueError("Withdrawal limit is ₹20,000 per transaction")

        if amt > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance -= amt
        print(f"₹{amt} withdrawn successfully")

    def mini_statement(self):
        if not self.__authenticated:
            raise ValueError("Please authenticate first")

        print("----- MINI STATEMENT -----")
        print("Owner:", self._owner)
        print("Balance:", self.__balance)

    @property
    def balance(self):
        return self.__balance



atm = ATM(1234, "Navjot", 50000)

atm.authenticate(1234)

atm.deposit(5000)
atm.withdraw(10000)

atm.mini_statement()

print("Current Balance:", atm.balance)