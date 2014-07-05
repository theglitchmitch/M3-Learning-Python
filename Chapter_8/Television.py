# Television
# A television simulator

class Television(object):
    """A Television object"""

    def __init__(self, volume = 0, channel = 0):
        self.volume = volume
        self.channel = channel

    def vol(self, volume):
        self.volume = volume
        if self.volume < 0:
            self.volume = 0
        elif self.volume > 50:
            self.volume = 50
        print("The volume has been changed to", self.volume)

    def chan(self, channel):
        self.channel = channel
        if self.channel < 0:
            self.channel = 0
        elif self.channel > 25:
            self.channel = 25
        print("The channel has been changed to", self.channel)

def main():
    tele = Television()

    choice = None
    while choice != "0":
        print("""
        Television simulator
        0 - Quit
        1 - Change volume
        2 - Change channel
        """)
        print("Volume:", tele.volume,)
        print("Channel:", tele.channel, "\n")
        choice = input("Choice: ")
        # exit
        if choice == "0":
            print("Good-bye.")
        # change the volume
        elif choice == "1":
            volume = int(input("What do you want the volume to be: "))
            tele.vol(volume)
        # change the channel
        elif choice == "2":
            channel = int(input("What do you want the channel to be: "))
            tele.chan(channel)
        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
input("\n\nPress the enter key to exit: ")