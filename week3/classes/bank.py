class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance +=amount
        print(f"{amount}$ accepted, new balance {self.balance}$")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Denied, you must have more money")
        else:
            self.balance -=amount
            print(f"{amount}$ withdrawed, balance {self.balance}$")
acc = Account('Ilyas', 1500)

acc.deposit(500)
acc.withdraw(400)
acc.withdraw(15000)
acc.withdraw(200)

