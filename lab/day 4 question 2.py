class BankAccount:

    # 1. Parameterized constructor to initialize account_number and balance
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance
        print(f"Account {self.account_number} created with balance: ${self.balance}")

    # 2. Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Amount must be positive.")
        return self.balance

    # 2. Withdraw method with 4. Invalid withdrawal handling
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount. Amount must be positive.")
            return self.balance
        elif amount > self.balance:
            print(f"Insufficient funds. Withdrawal denied. Available balance: ${self.balance}")
            return self.balance
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
            return self.balance

    # 3. Destructor to display message when object is deleted
    def __del__(self):
        print(f"Account {self.account_number} is being deleted. Final balance: ${self.balance}")


# Demonstration of the class
if __name__ == "__main__":
    # Creating an account (1. Parameterized constructor)
    account1 = BankAccount("ACC001", 1000)

    # 2. Testing deposit method
    account1.deposit(500)

    # 2. & 4. Testing withdraw method with valid and invalid cases
    account1.withdraw(200)  # Valid withdrawal
    account1.withdraw(2000)  # Invalid - insufficient funds
    account1.withdraw(-100)  # Invalid - negative amount

    # 3. Destructor will be called automatically when object is deleted
    del account1