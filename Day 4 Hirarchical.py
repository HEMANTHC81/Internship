class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("Interest of", interest, "added.")

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(amount, "withdrawn using overdraft facility.")
        else:
            print("Overdraft limit exceeded!")

print("\n Savings Account")
savings = SavingsAccount("ram", 5000, 5)
savings.display_balance()
savings.deposit(1000)
savings.add_interest()
savings.withdraw(2000)
savings.display_balance()

print("\n Current Account")
current = CurrentAccount("Rahul", 3000, 2000)
current.display_balance()
current.deposit(1500)
current.withdraw_with_overdraft(6000)
current.display_balance()
