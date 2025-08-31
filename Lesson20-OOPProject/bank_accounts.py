class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initalAmount, accName):
        self.balance = initalAmount
        self.name = accName
        print(
            f"\nAccount '{self.name}' created.\nBalance = £{self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = £{self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.")
        self.getBalance()

    def viableTrasaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of £{self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viableTrasaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer... 🎇')
            self.viableTrasaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete! 😊\n\n**********')
        except BalanceException as error:
            print(f'\nTransfer interrupted 😢 {error}')


class InterestRewardsAcc(BankAccount):
    # No __init__ needed because we are using the same parameters.
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Complete.")
        self.getBalance()


class SavingsAcc(InterestRewardsAcc):
    def __init__(self, initalAmount, accName):
        super().__init__(initalAmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTrasaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
