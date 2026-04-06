from bank_accounts import *

account1 = BankAccount("Gopal", 1000)
account1.CheckBalance()

account2 = BankAccount("Alice",2000)
account2.CheckBalance()

account1.Deposit(750)
account1.Withdraw(500)

account1.fundtransfer(account2, 300)
account2.fundtransfer(account1, 5000)
