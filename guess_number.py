import random
guesses = 0

# start of game
print("Hi, What is your name")
name = input()

# inputs numbers 1 - 20 only
number = random.randint(1, 20)
print("Hello " + name + "! I am thinking of a number between 1 and 20")

# only allows 5 guesses and prevents player from guessing a number
while guesses < 5:
    print("Guess the number? ")
    try:
        guess = input()
        guess = int(guess)
    except ValueError:
        print("you must enter an integer")
        continue

# Guess count increases by 1 each guesses
    guesses = guesses + 1
# lets the player know if their guess is too high or too low
    if guess < number:
        print("Your number is too low.")
    elif guess > number and guess <= 20:
        print("Your number is too high.")
# Prevents player from guessing a number above 20
    elif guess > 20:
        print("Out of guessing range")
    else:
        guess == number
        break

# If the guesses right...
if guess == number:
    guesses = str(guesses)
    print("YAY!! You got it " + name + "!", "It took you " + guesses + " guesses.")

# if the player guesses wrong...
if guess != number:
    number = str(number)
    print("Awe. Unfortunately you did not guess correctly. The number was: " + number + "! Better luck next time.")
