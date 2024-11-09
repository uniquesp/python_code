import sys

def divide(x, y):
    try:
        result = x / y
        print("Result:", result)
    except ZeroDivisionError as e:
        print("Error:", e)
        #We also use sys.exc_info() to get more information about the exception, including its type.
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("Exception type:", exc_type)
    else:
        print("Division successful")
    finally:
        print("This block always executes")

# Example usage:
divide(10, 2)  # Output: Result: 5.0
divide(10, 0)



# Using Raise keyword
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 120:
        raise ValueError("Age cannot be greater than 120")
    else:
        print("Valid   age:", age)

try:
    user_age = int(input("Enter your age: "))
    validate_age(user_age)
except ValueError as e:
    print("Invalid age:", e)