# Write a custom exception class InsufficientFundsError and use it in a banking application.

# implemented in Ques 1

# Create a class BankAccount with methods for deposit, withdrawal, balance check, and transaction history.

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, name, balance):
        self.balance = balance
        self.name = name
        self.trans_history = []
        self.trans_history.append(f"{self.name} - Accounted Created with initial Balance : {balance}")
        
    
    def depoisit(self, amount):
        self.balance += amount
        self.trans_history.append(f"Deposited : {amount}  - Balance : {self.balance}")
    
    def withdrawal(self, amount):
        try:
            if(self.balance == 0 or amount > self.balance):
                raise InsufficientFundsError("Insufficient fund in account")
        except InsufficientFundsError as err:
            print(err)
        else:
            self.balance -= amount
            self.trans_history.append(f"Withdrawal : {amount} - Balance : {self.balance}")
    
    def transaction_history(self):
        return self.trans_history

    def check_balance(self):
        return self.balance
    
ujjawal = BankAccount('Ujjawal', 1000)
anant = BankAccount('Anant', 2000)

ujjawal.withdrawal(2000)


ujjawal.depoisit(100)
anant.depoisit(200)

ujjawal.withdrawal(200)
anant.withdrawal(100)

for i in ujjawal.transaction_history():
    print(i)

for i in anant.transaction_history():
    print(i)


