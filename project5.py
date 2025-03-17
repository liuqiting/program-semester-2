def factorial_while(num):
    fact = 1
    while num > 0:
        fact = fact * num
        num = num - 1
    return fact
number = int(input("Enter a number: "))
print(factorial_while(number))
