class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def make_call(self, number):
        # f indicates that it is formatted string
        print(f"Calling {number} from {self.brand} {self.model}")

    def send_message(self, number, message):
        print(f"Sending '{message}' to {number} from {self.brand} {self.model}")

# Usage:
phone = Phone("Apple", "iPhone 14")
phone.make_call("123-456-7890")
phone.send_message("987-654-3210", "Hello, world!")