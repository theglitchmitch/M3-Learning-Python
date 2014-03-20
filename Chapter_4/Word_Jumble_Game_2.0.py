# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word
import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

# pick one word randomly from the sequence
word = random.choice(WORDS)

# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble =""

score = 100

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
Welcome to Word Jumble 2.0!
Now with hints and a scoring system!
Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

print("\nType 'hint' for a hint!")

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    if guess == "hint":
        if correct == "python":
            print("It's an awesome programming language")
        if correct == "jumble":
            print("What did this program do again..?")
        if correct == "easy":
            print("It's not that hard!")
        if correct == "difficult":
            print("This is pretty hard!")
        if correct == "answer":
            print("What could be the solution to this?")
        if correct == "xylophone":
            print("Weird music instrument thingy")
        score -= 50
    print("Try again.")
    guess = input("Your guess: ")

if guess == correct:
    print("That's it! You guessed it!")
    print("This is your score!", score)

print("\nThanks for playing.")
input("\n\nPress the enter key to exit.")
