import random
secret_number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))

while guess != secret_number:
    if guess < 1 or guess > 100:
        print("Your guess is out of bounds. Please guess a number between 1 and 100.")
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    guess = int(input("Guess a number between 1 and 100: "))
print("Congratulations! You've guessed the number.")