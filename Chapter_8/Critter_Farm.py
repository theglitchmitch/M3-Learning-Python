# Critter Farm Caretaker
# A whole farm of critters to take care of
import random

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food = 4):
        print("Brruppp. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    critters = []

    crit_num = int(input("How much Critters do you want: "))

    for count in range(crit_num):
        hunger_value = random.randrange(7)
        boredom_value = random.randrange(7)
        crit = Critter(count,hunger_value,boredom_value)
        critters.append(crit)

    choice = None
    while choice != "0":
        print \
                ("""
                Critter Farm Caretaker
                0 - Quit
                1 - Feed your critters
                2 - Play with your critters
                """)
        choice = input("Choice: ")
        print()
        # exit
        if choice == "0":
            print("Good-bye.")
        # feed your critters
        elif choice == "1":
            for i in range(crit_num):
                critters[i].eat()
        # play with your critters
        elif choice == "2":
            for j in range(crit_num):
                critters[j].play()
        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
input("\n\nPress the enter key to exit.")