from bank_account import*

Kanna = BankAccount(1000,'Kanna')
PR = BankAccount (2000,'PR')

Kanna.getbalance()
PR.getbalance()

Kanna.deposit(250)
PR.deposit(500)

Kanna.withdraw(4000)
PR.withdraw(300)

PR.transfer(4000, Kanna)
PR.transfer(200, Kanna)

Madu = InterestRewardAcct(1000, "Madu")

Madu.getbalance()
Madu.deposit(500)
Madu.transfer(100, Kanna)

kiruthik = Savings(1000, 'kiruthik')
kiruthik.getbalance()
kiruthik.deposit(500)
kiruthik.transfer(1000, PR)