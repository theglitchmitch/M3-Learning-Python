import random

WORDS = ("mitchell", "python", "games", "food", "test")

word = random.choice(WORDS)

word_length = len(word)

print("\tWelcome to the Word Guesser Program!")

print("\nThe program will tell you how long the randomly chosen word is")
print("You have 5 chances to ask if a letter is in the randomly chosen word and\nthe computer will answer accordingly if the letter is in there or not")
print("After that you will have to guess the word!\n")

print("The length of the randomly chosen word is ", word_length, "\n")

chances = 5

while chances != 0:
    letter = input("Please enter a letter: ")
    if letter in word:
        print("yes")
    if letter not in word:
        print("no")
    chances -= 1

print("You've had 5 chances to know more about the word!")
print("It is time to guess the word!\n")

guess = input("Please enter the word: ")
while guess != word:
    print("Sorry, try again")
    guess = input("Please enter the word: ")

print("Congratulations! You have guessed the word!")

print("\n\nPress the enter key to exit.")