


class BankAccount:
    def __init__(self, balance=0, int_rate=.01):
        self.balance= balance
        self.int_rate = int_rate

    def deposit(self, account):
        self.balance += account
        return self

    def withdrawal(self, amount):
        if self.balance < 0:
            print('insufficient funds: charging a $5 fee')
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f'int_rate: {self.int_rate}')
        print(f'balance: {self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
             self.balance * self.int_rate
             self.balance += self.int_rate
        return self


fanfan_bank_account = BankAccount(350)
murphy_bank_account = BankAccount(200)

fanfan_bank_account.display_account_info().deposit(120).deposit(145).deposit(57).withdrawal(124).yield_interest().display_account_info()
murphy_bank_account.display_account_info().deposit(150).deposit(125).withdrawal(75).withdrawal(27).withdrawal(105).withdrawal(79).yield_interest().display_account_info()

