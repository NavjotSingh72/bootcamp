class pnb:
    def __init__(self, pin, balance, owner):
        self.__pin = pin
        self.__balance = balance
        self._owner = owner
        self.__authenticated = False

    def authenticate(self, pin):
        if pin == self.__pin:
            self.__authenticated = True
            print("Authentication Successful")
        else:
            print("Wrong PIN")

    @property
    def balance(self):
        return self.__balance

    def deposit(self, pnb):
        if not self.__authenticated:
            print("Please authenticate first")
            return
        self.__balance += pnb
        print("Deposited:", pnb)

    def withdraw(self, pnb):
        if not self.__authenticated:
            print("Please authenticate first")
            return
        if pnb > 20000:
            print("Maximum withdrawal limit is ₹20,000")
        if pnb > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= pnb
            print("Withdrawn:", pnb)

    
    
pnb = pnb(172813, 40000, "Navjot") 

pnb.authenticate(172813)
pnb.deposit(5000)
pnb.withdraw(10000)

print("Current Balance:", pnb.balance)