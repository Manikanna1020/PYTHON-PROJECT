class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initalAmount, accName):
        self.balance = initalAmount
        self.name = accName
        print(f"\n Account {accName} created. \n Balance = ${initalAmount: .2f}")
    
    def getbalance(self):
        print(f"\n Account {self.name} Balance: ${self.balance: .2f}")\
    
    def deposit(self, Amount):
        self.balance = self.balance + Amount
        print ("\nDeposit complete.")
        self.getbalance()
    
    def transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f'\nSorry account {self.name} only has a balance of ${self.balance:.2f}')
    
    def withdraw(self, amount):
        try:
            self.transaction(amount)
            self.balance = self.balance - amount
            print('\n Withdraw complete')
            self.getbalance()
        except BalanceException as error:
            print(f'\nwithdraw interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n******\n\nBeginning Transfer....')
            self.transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\n Transfer Complete!!')
        except BalanceException as error:
            print(f'\n Transfer Interrupted: {error}')

class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print('\nDeposit Complete ')
        self.getbalance()

class Savings(InterestRewardAcct):
    def __init__(self, initalAmount, accName):
        super().__init__(initalAmount, accName)

        self.fee = 5
    def withdraw(self, amount):
        try:
            self.transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print('\n Withdraw complete')
            self.getbalance()
        except BalanceException as error:
            print(f'\n Interrupted: {error}')
        