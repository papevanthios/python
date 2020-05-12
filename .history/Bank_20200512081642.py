from HeaderFiles import Header1
class Account:
    
    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    def __str__(self):

        print('Account owner: {}'.format(self.owner))
        print('Account balance: {}'.format(self.balance))

    def deposit(self,amount):

        self.balance = self.balance + amount
        print('Deposit Accepted. Total balance: {}'.format(self.balance))

    def withdraw(self, amount):

        if amount > self.balance:
            print('Funds Unavailable!')
        else:
            self.balance = self.balance - amount
            print('Withdraw Accepted. Total balance: {}'.format(self.balance))


acc1 = Account('Man', 500)
print(acc1.owner)
print(acc1.balance)
acc1.deposit(50)
acc1.withdraw(300)
print(acc1.balance)

n = input()