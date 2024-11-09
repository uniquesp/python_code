print("Welcome to Python","sakshi 23+24")
print(23+24)
list = [10,20,20,40]
cities = ["satara","pune","Amravati","Phaltan","Sangli"]

#Length 
def print_len(list):
    print(len(list))

#print elememt on nextLine
def print_list(list):
    for item in list:
        print(item, end=" ")

print(print_list(cities))

# factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print (factorial(5))

#USD to INR
def converter(USD):
    if USD==0:
        return 0
    else:
        inr_val =  USD * 84.38
        print(USD, "USD =", inr_val, "INR")

print(converter(100))

