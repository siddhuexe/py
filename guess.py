import random
import os

n = random.randint(0, 9)

while True:
    try:
        guess = int(input("Guess a number between 0 and 9: "))
        if guess < 0 or guess > 9:
            print("Please enter a number between 0 and 9.")
            continue 
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue  

    if guess == n:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        os.system("shutdown /h")


