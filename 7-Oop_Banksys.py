class Bank:
    def __init__(self, balance, Account):
        self.bal = balance
        self.acc = Account

    def Debit(self, amount):
        self.bal -= amount
        print("Your Debitted", amount, "amount is")

    def Credit(self, amount):
        self.bal += amount
        print(f"your Crdit {amount} amount is ")
        print("your total balnce", self.getBalance())

    def getBalance(self):
        return self.bal


faseeh = Bank(12000, 12345)

print(faseeh.bal, faseeh.acc)

faseeh.Credit(2000)
