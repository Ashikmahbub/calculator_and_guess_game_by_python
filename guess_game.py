# Number Guessing Game
# Author: Ashik Mahbub
# Date: 2025-10-05
# Description: A simple guessing game that take inputs as an attempt from user to guess a random .
# Ostad Django React Course Batch 7
# Module 6 - Project 2

import random

print("Welcome to the Number Guessing Game!")
print("Try to guess the number between 1 and 100.\n")

#a random number between 1 and 100
target_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        if guess < target_number:
            print("Too low!\n")
        elif guess > target_number:
            print("Too high!\n")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print("Invalid input. Please enter a numeric value.\n")
