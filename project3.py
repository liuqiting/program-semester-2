import random
random_num = random.randint(10, 20)
while True:
    guess = int(input("Guess a number between 10 and 20: "))
    if guess == random_num:
        print("Congratulations!")
        break
