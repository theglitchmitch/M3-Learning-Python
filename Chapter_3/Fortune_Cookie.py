import random

print("\tWelcome to the Fortune Cookie Simulator!")
print("\nThis program will tell you your fortune you'd \nnormally get from your local chinese take away!")

input("\nPress the enter key to break the cookie and reveal your fortune!\n")

fortune = random.randint(1, 5)

if fortune == 1:
    print("You will have unexpected great luck.")

elif fortune == 2:
    print("If you are afraid to shake the dice, you will never throw a six.")

elif fortune == 3:
    print("Whenever possible, keep it simple.")

elif fortune == 4:
    print("Elegant surroundings will soon be yours.")

elif fortune == 5:
    print("A single conversation with a wise man is better than ten years of study.")

input("\n\nPress the enter key to exit.")






