class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} rupees. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} rupees. New balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid withdrawal amount")

    def get_balance(self):
        return self.__balance

# Creating a bank account object
account = BankAccount("12345", 1000)

# Accessing and modifying balance through public methods
account.deposit(500)
account.withdraw(200)
print(account.get_balance())