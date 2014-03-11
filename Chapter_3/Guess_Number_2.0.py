import random

print("\tWelcome to 'Guess My Number 2.0'!")
print("\nI'm thinking of a number between 1 and 100.")
print("This time you only get 6 tries! Good luck!.\n")

# set the initial values
#range = int(input("Enter range: "))
the_number = random.randint(1, 100)
tries = 1

# guessing loop
while tries != 7:

    guess = int(input("Take a guess: "))
    if guess == the_number:
        print("\nYou guessed it! The number was", the_number)
        print("And it only took you", tries, "tries!")
        input("\nPress the enter key to exit.")
        break
    elif guess < the_number:
        print("Higher...")
    elif guess > the_number:
        print("Lower...")
    else:
        print("Error")
    tries += 1

print("""
 ____        ___       ___  ___   _____
/ ___|      /   |     /   |/   | |  ___|
| |        / /| |    / /|   /| | | |__
| | _     / ___ |   / / |__/ | | | __|
| |_| |  / /  | |  / /       | | | |___
\_____/ /_/   |_| /_/        |_| |_____|
 _____   _     _   _____   _____
/  _  \ | |   / / |  ___| |  _  |
| | | | | |  / /  | |__   | |_| |
| | | | | | / /   |  __|  |  _  /
| |_| | | |/ /    | |___  | | \ |
\_____/ |___/     |_____| |_|  \_|
""")

input("\n\nPress the enter key to exit.")
