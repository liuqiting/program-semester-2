def factorial_for(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact
number = int(input("Enter a number: "))
print(factorial_for(number))
