import random

print("\tWelcome to Coin Flipper!")
print("\nThis program will flip a coin 100 times and tell you\nthe number of heads and tails you got!")

input("\nPress the enter key to start flipping the coin.\n")

heads = 0
tails = 0
count = 0

while count != 100:
    decide_num = random.randint(1, 2)
    if decide_num == 1:
        heads += 1
        count += 1
    elif decide_num == 2:
        tails += 1
        count += 1

if count == 100:
    print("A 100 coins have been flipped and the number of heads and tails are as follows:\n")
    print("Heads: ", heads)
    print("Tails: ", tails)

    input("\n\nPress the enter key to exit.")