# 1. Import the random module to generate random numbers
import random

# 2. Print a welcome message to the user
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# 3. Generate a random secret number between 1 and 100 and store it in a variable
secret_number = random.randint(1, 100)
guess_count = 0

# 4. Create and infinite loop for the game to run in
while True:
    # 5. ask the user for their guess and convert it to an integer
    guess_str = input("Make a guess: ")
    guess = int(guess_str)
    guess_count += 1 # This is shorthand for guess_count = guess_count + 1

    # 6. Compare the guess to the secret number and give hints
    #    - If the guess is too low, print "Too low."
    #    - If the guess is too high, print "Too high."
    #    - If the guess is correct, print a congrats message, tell them the number of guesses, and then break out of the loop.
    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print(f"You got it! the number was {secret_number}.")
        print(f"It took you {guess_count} guesses.")
        break # Exit the wile loop

print("Thanks for playing!")
