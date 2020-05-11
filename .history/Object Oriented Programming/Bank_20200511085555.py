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




a = Account('Man', 500)
print(a)
a.owner
a.balance
