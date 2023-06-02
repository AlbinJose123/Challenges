class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def getBalance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdrawal(self, amount):
        self.balance -= amount


class SavingsAccount(Account):
    def __init__(self, balance, interestRate):
        super().__init__(balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.balance * self.interestRate) / 100
# Create an instance of SavingsAccount
savings = SavingsAccount(2000, 5)
# Perform the tasks
savings.deposit(500)
print(savings.getBalance()) 

savings.withdrawal(500)
print(savings.getBalance())  

print(savings.interestAmount()) 

savings = SavingsAccount(2000, 5)

# Perform the tasks
savings.deposit(500)
print(savings.getBalance())  

savings.withdrawal(500)
print(savings.getBalance())  

print(savings.interestAmount())  
