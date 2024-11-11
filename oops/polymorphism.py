# Base class PaymentMethod
class PaymentMethod:
    def process_payment(self, amount):
        pass  # To be implemented by subclasses

# CreditCard class inherits from PaymentMethod
class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

# PayPal class inherits from PaymentMethod
class PayPal(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# BankTransfer class inherits from PaymentMethod
class BankTransfer(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing bank transfer payment of ${amount}")

# Function to process any payment
def make_payment(payment_method: PaymentMethod, amount):
    payment_method.process_payment(amount)

# Create instances of different payment methods
credit_card = CreditCard()
paypal = PayPal()
bank_transfer = BankTransfer()

# Process payment using different payment methods
make_payment(credit_card, 100)     # Output: Processing credit card payment of $100
make_payment(paypal, 200)          # Output: Processing PayPal payment of $200
make_payment(bank_transfer, 300)   # Output: Processing bank transfer payment of $300
