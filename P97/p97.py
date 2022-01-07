import random
a=random.randint(1,9)
print(a)
chances = 5
number = 8

while chances < 5:

    guess = int(input("Guess a number between 1 and 9"))

    if guess == number:
        print("Congratulations You Won!!")
        break
    if not chances < 5:
        print("YOU LOSE, the number is 8")