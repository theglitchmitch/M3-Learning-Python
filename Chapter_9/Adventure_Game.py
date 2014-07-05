class City(object):
    """A city class"""

    def __init__(self, name, discription):
        self.name = name
        self.discription = discription

    def show(self, player):
        print("Welcome to the city of", self.name)
        print(self.discription)
        print("Where do you want to travel now", player, "\n")


class Player(object):
    """A player class"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        rep = self.name
        return rep

    @staticmethod
    def travel(city, player):
        city.show(player)

def main():
    name = input("What is your name: ")

    city1 = City("Asgard", "The beautiful Northern heaven")
    city2 = City("Whiterun", "")
    city3 = City("Majula", "Prepare to die")
    hero = Player(name)

    print("""
    Fast travel menu
    0 - Quit
    1 - Travel to Asgard
    2 - Travel to Whiterun
    3 - Travel to Majula
    """)
    choice = None
    while choice != "0":
        choice = input("Where do you want to travel: ")
        if choice == "1":
            hero.travel(city1, name)
        elif choice == "2":
            hero.travel(city2, name)
        elif choice == "3":
            hero.travel(city3, name)
        else:
            print("This choice isn't available, choose something else.")

main()
input("\n\nPress the enter key to exit.")