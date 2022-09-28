class BankAccount:
    all_accounts = []
    def __init__(self, int_rate_given = None, balance_given=0):
        self.balance = balance_given
        self.interest_rate = int_rate_given
        BankAccount.all_accounts.append(self)


    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds:Charging a $5 fee')
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance ${self.balance}, interest rate {self.interest_rate * 100}%")
        return self

    def yield_interest(self):
        self.balance += self.balance*self.interest_rate
        return self

    @classmethod
    def show_bank_accunt_info_all(cls):
        for i in cls.all_accounts:
            i.display_account_info()
        return cls

acc1 = BankAccount(0.2)
acc1.deposit(500).deposit(200).deposit(300).withdraw(500).yield_interest()

acc2 = BankAccount(0.1)
acc2.deposit(500).deposit(500).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest()

BankAccount.show_bank_accunt_info_all()

