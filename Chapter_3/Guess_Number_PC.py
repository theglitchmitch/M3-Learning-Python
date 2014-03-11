import random

print("\tWelcome to 'Guess My Number'! Switched version!")
print("\nThink of a number between 1 and 100! When the computer gives a number please\ntype 'higher', 'lower' or 'correct' accordingly!")
input("\nPlease press enter to start the game!\n")

high_numb = 100
low_numb = 1
guess_number = random.randint(1, 100)
print("My guess is", guess_number)
player_dir = input("Do I need to go higher, lower or is this correct?\n")
tries = 1

while player_dir != "correct":

    if player_dir == "higher":
        low_numb = guess_number
        guess_number = random.randint(guess_number, high_numb)
        print("My guess is", guess_number)
        player_dir = input("Do I need to go higher, lower or is this correct?\n")
        tries += 1

    elif player_dir == "lower":
        high_numb = guess_number
        guess_number = random.randint(low_numb, guess_number)
        print("My guess is", guess_number)
        player_dir = input("Do I need to go higher, lower or is this correct?\n")
        tries += 1

    else:
        print("ERROR")

print("\nI guessed your number and it only took me", tries,"tries!")

input("\n\nPress the enter key to exit.")