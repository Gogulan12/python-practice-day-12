#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import  logo
import random


print (logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

number = random. randint(1, 100)
print(f"Psst, the correct answer is {number}")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

def hard():
    guessed_number = int(input("Make a guess: "))

    guess = 5

    while guess > 0:
        if number > guessed_number:
            print("To low")
            guess -=1
            if guess == 0:
                print("you lose. Game over ")
            else:
                print(f"you have {guess} attempts left.")
                guessed_number = int(input("Too low. Guess again: "))
        elif number < guessed_number:
            print("To high")
            guess -= 1
            if guess == 0:
                print("you lose. Game over ")
            else:
                print(f"you have {guess} attempts left.")
                guessed_number = int(input("Too high. Guess again: "))
        elif number == guessed_number:
            print(f"Match you win. the anwser is {number}")
            guess = 0


def easy():
    guessed_number = int(input("Make a guess: "))

    guess = 10

    while guess > 0:
        if number > guessed_number:
            print("To low")
            guess -= 1
            if guess == 0:
                print("you lose. Game over ")
            else:
                print (f"you have {guess} attempts left.")
                guessed_number = int(input("Too low. Guess again: "))


        elif number < guessed_number:
            print("To high")
            guess -= 1
            if guess == 0:
                print("you lose. Game over ")
            else:
                print(f"you have {guess} attempts left.")
                guessed_number = int(input("Too high. Guess again: "))
        elif number == guessed_number:
            print(f"Match you win. the anwser is {number}")
            guess = 0

if level == "easy":
    easy()
if level == "hard":
    hard()