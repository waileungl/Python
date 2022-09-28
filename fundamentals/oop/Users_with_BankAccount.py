class User:
    def __init__(self, firstName, lastName, email, age):
        self.first_name = firstName
        self.last_name = lastName
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = []

    def open_new_account(self, accName):
        self.account.append(BankAccount(accName, int_rate_given = None, balance_given=0))

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
        
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("User already a member.")
        return self

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("Sorry! You don't have enough points.")
        else:
            self.gold_card_points = self.gold_card_points - amount
        return self

    def make_deposit(self, accName, amount):
        for account in self.account:
            if account.name == accName:
                account.deposit(amount)
        return self

    def make_withdrawal(self, accName, amount):
        for account in self.account:
            if account.name == accName:
                account.withdraw(amount)
        return self

    def display_user_balance(self,accName):
        for account in self.account:
            if account.name == accName:
                print(f"The current balance in your account '{accName}' is ${account.balance}")
        return self
    
    def transfer_money(self, accName, other_user):
        for account in self.account:
            if account.name == accName:
                recipient = input("Enter the account name you want to transfer to: ")
                amount = int(input(f"Enter the amount you want to transfer to {recipient}: $"))
                account.withdraw(amount)
                for i in other_user.account:
                    if i.name == recipient:
                        i.deposit(amount)
        return self


class BankAccount:
    all_accounts = []
    def __init__(self, name, int_rate_given = None, balance_given=0):
        self.balance = balance_given
        self.interest_rate = int_rate_given
        self.name = name
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

# Creating new user
user1 = User('William', 'Liu', 'liuweiliang@hotmail.com', '26')
user2 = User('Mike', 'kok', 'meiqi0204@hotmail.com', '24')

# Opening new account
user1.open_new_account('waileung')
user2.open_new_account('miki')

# Make deposit and withdrawal to test the method
user1.make_deposit('waileung', 1000)
user1.make_withdrawal('waileung', 500)

# Check current balance
user1.display_user_balance('waileung')
user2.display_user_balance('miki')

user1.transfer_money('waileung', user2)

user1.display_user_balance('waileung')
user2.display_user_balance('miki')