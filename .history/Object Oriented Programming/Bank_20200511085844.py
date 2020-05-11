from os import system, name 
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
clear() 

class Account:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        print('Account owner: {}'.format(self.owner))
        print('Account balance: {}'.format(self.balance))
        return True

    def deposit(amount):
        self.balance = self.balance + amount
        print('Deposit Accepted. Total balance: {}'.format(self.balance))


acc1 = Account('Man', 500)
print(acc1.owner)
print(acc1.balance)
