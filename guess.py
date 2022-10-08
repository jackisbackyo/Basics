import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number: "))
        if guess < random_number:
            print("Guess is too low!")
        elif guess > random_number:
            print("Guess is too high!")
        else:
            print("Congrats! You guessed correct!")
guess(100)