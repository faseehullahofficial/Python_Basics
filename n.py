class Bank:
    def __init__(self, balance, Account):
        self.bal = balance
        self.acc = Account

    def Debit(self, amount):
        self.bal -= amount
        print("Your Debited", amount, "is")
        print("Your Total Balance is", self.getBalance())

    def Credit(self, amount):

        self.bal += amount
        print("Your Credited", amount, "amount is")
        print("Your Total Balance is", self.getBalance())

    def getBalance(self):
        return self.bal


# Initial Balance Set
faseeh = Bank(10000, 12345)

print("===== Welcome To Bank =====")
print("Account Number:", faseeh.acc)
print("Initial Balance:", faseeh.bal)

# Loop
while True:

    print("\n1. Credit")
    print("2. Debit")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        amount = int(input("Enter Credit Amount: "))
        faseeh.Credit(amount)

    elif choice == 2:
        amount = int(input("Enter Debit Amount: "))
        faseeh.Debit(amount)

    elif choice == 3:
        print("Your Current Balance is", faseeh.getBalance())

    elif choice == 4:
        print("Thanks For Using Our Bank")
        break

    else:
        print("Invalid Choice")
