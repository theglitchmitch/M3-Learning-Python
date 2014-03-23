#variables
dad_son = {"mitchell":["Dad", "Grandfather"], "luke":["Darth Vader", "Mister Skywalker"], "stan":["Randy", "Granddad"]}
choice = None

print("""
----Who's Your Daddy?----

    0 - Quit
    1 - Look up a pair
    2 - Add a pair
    3 - Replace a pair
    4 - Delete a pair
    5 - Look up the Grandfather

-------------------------
""")

while choice != 0:
    choice = int(input("Your choice: "))

    if choice == 1:
        son = input("What is the name of the son of the pair: ")
        son = son.lower()
        if son in dad_son:
            dad = dad_son[son][0]
            print("The father of", son, "is", dad)
        else:
            print(son, "is not in the system!\nTry adding it!\n")

    elif choice == 2:
        son = input("What is the name of the son you want to add: ")
        son = son.lower()
        if son not in dad_son:
            dad = input("What is the name of the father you want to add: ")
            dad_son[son] = dad
            print("the son", son, "and the father", dad, "have been added")
        else:
            print(son, "is already in the system! Try something else.")

    elif choice == 3:
        son = input("What is the name of the son whose father you want to replace: ")
        son = son.lower()
        if son in dad_son:
            dad = input("Replace the father by entering the name: ")
            dad_son[son] = dad
            print("the son", son, "and the father", dad, "have been changed")
        else:
            print(son, "is not in the system!\nTry adding it!\n")

    elif choice == 4:
        son = input("Enter the name of the son you want to delete: ")
        if son in dad_son:
            del dad_son[son]
            print(son, "has been deleted!")
        else:
            print(son, "doesn't exist!")

    elif choice == 5:
        son = input("What is the name of the grandchild of the grandfather: ")
        son = son.lower()
        if son in dad_son:
            granddad = dad_son[son][1]
            print("The grandfather of", son, "is", granddad)
        else:
            print(son, "doesn't exist!")

    else:
        print("Invalid choice. Try something else.")

input("\n\nPress the enter key to exit.")
