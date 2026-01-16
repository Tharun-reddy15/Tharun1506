class student:
    def display(self):
        print("This is student class")


s1 = student()
s1.display()


class calculator:
    def add(self, a, b):
        print("sum:", a + b)


c = calculator()
c.add(100, 300)


class student:
    def display(self):
        print("This is student class")


s1 = student()
s1.display()


class calculator:
    def add(self, a, b):
        print("sum:", a + b)


c = calculator()
c.add(100, 300)


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(200)