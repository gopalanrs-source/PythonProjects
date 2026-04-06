class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance

    def CheckBalance(self):
        print(f"{self.account_name} has a current balance of ${self.balance:.2f}")

    def Deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} to {self.account_name}'s account.")
        else:
            print("Deposit amount must be positive.")
        self.CheckBalance()

    def Withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f} from {self.account_name}'s account.")
            else:
                print("Insufficient funds for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")
        self.CheckBalance()

    def fundtransfer(self, target_account, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                target_account.balance += amount
                print(f"Transferred ${amount:.2f} from {self.account_name} to {target_account.account_name}.")
            else:
                print(f"{self.account_name} has insufficient funds for transfer.")
        else:
            print("Transfer amount must be positive.")
        self.CheckBalance()
        target_account.CheckBalance()



    
