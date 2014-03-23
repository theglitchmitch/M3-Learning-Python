#variables
attributes = {"strength": 0, "health": 0, "wisdom": 0, "dexterity": 0}
pool = 30
inc_dec = ""

#current stats
print("Your current stats are as follows:")
print("Strength:\t",attributes["strength"], "\nHealth:\t\t",attributes["health"], "\nWisdom:\t\t", attributes["wisdom"], "\nDexterity:\t", attributes["dexterity"])
print("You have", pool, "points left to spend.")

#keep looping until user wants to quit
while inc_dec != "quit":
    inc_dec = input("\nDo you want to increase or decrease an attribute or quit: ")
    inc_dec = inc_dec.lower()

    #increase which skill
    if inc_dec == "increase":
        skill = input("\nWhat skill do you want to increase: ")
        skill = skill.lower()

        if skill not in attributes:
            print("\nTry a different attribute!\n")

        #by how much
        else:
            inc = int(input("By how much do you want to increase your attribute: "))

            if inc > pool:
                print("You don't have that many points left!")

            #increase skill
            else:
                attributes[skill] += inc
                pool -= inc
                print("Your current stats are as follows:")
                print("Strength:\t",attributes["strength"], "\nHealth:\t\t",attributes["health"], "\nWisdom:\t\t", attributes["wisdom"], "\nDexterity:\t", attributes["dexterity"])
                print("You have", pool, "points left to spend.")

#decrease which skill
    elif inc_dec == "decrease":
        skill = input("\nWhat skill do you want to decrease: ")
        skill = skill.lower()

        if skill not in attributes:
            print("\nTry a different attribute!\n")

        #by how much
        else:
            dec = int(input("By how much do you want to decrease your attribute: "))

            if dec > attributes[skill]:
                print("You can't do that!")

            #decrease skill
            else:
                attributes[skill] -= dec
                pool += dec
                print("Your current stats are as follows:")
                print("Strength:\t",attributes["strength"], "\nHealth:\t\t",attributes["health"], "\nWisdom:\t\t", attributes["wisdom"], "\nDexterity:\t", attributes["dexterity"])
                print("You have", pool, "points left to spend.")

input("\n\nPress the enter key to exit.")