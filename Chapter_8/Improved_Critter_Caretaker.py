# Critter Caretaker
# A virtual pet to care for

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self, value):
        if value < 5:
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
        self.__pass_time(0)

    def eat(self, food):
        print("Brruppp. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time(food)

    def play(self, fun):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time(fun)

def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print \
                ("""
                Critter Caretaker
                0 - Quit
                1 - Listen to your critter
                2 - Feed your critter
                3 - Play with your critter
                """)
        choice = input("Choice: ")
        # exit
        if choice == "0":
            print("Good-bye.")
        # listen to your critter
        elif choice == "1":
            crit.talk()
        # feed your critter
        elif choice == "2":
            food_num = int(input("How many sandwiches do you want to give your Critter: "))
            crit.eat(food_num)
        # play with your critter
        elif choice == "3":
            play_num = int(input("How many hours do you want to play with your Critter: "))
            crit.play(play_num)
        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
input("\n\nPress the enter key to exit.")