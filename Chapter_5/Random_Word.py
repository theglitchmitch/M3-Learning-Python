#imports
import random

#constants
WORD = ["PYTHON", "MITCHELL", "TESTING", "AWESOMENESS", "VACATION", "SANDWICH"]

#variables
printed = []

#start program
print("\tWelcome to the Random Word Program!")
print("\nThis program will print words in a random order and not repeat any!")

input("\nPress the enter key to start.\n")

#keep looping until all words are printed
while len(printed) != len(WORD):
    index_num = random.randrange(len(WORD)) - 1

    if WORD[index_num] in printed:
        continue

    elif WORD[index_num] not in printed:
        print(WORD[index_num])
        printed.append(WORD[index_num])

    else:
        print("error")

input("\n\nPress the enter key to exit.")