import random

x = random.randint(1,9)
# print(x)
guess = int(input("Enter a guess: "))
f = True
while f:
    if(guess == x):
        print("Well guessed!")
        f = False 
    else: 
        guess = int(input("Enter a guess: "))
