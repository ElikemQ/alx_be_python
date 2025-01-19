class BankAccount:
    def __init__(self, account_balance, initial_balance = 0):
        self.account_balance = account_balance
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit must be more than zero")

    def withdraw(self, amount):
            if amount > 0 and amount <self.account_balance:
                self.account_balance -= amount
                print(f"Withdrew: ${amount}")
                return True
            elif amount > self.account_balance:
                print("Insufficient funds")
            else:
                 print("Withdrawal amount must be positive")
                 return False
    def current_balance(self, amount):
         amount = self.account_balance + amount
         
    def display_balance(self,):
         print(f"Current balance: ${self.account_balance}")