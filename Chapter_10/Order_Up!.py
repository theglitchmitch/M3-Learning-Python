from tkinter import *

class Application(Frame):
    """ GUI for a Restaurant Menu"""
    def __init__(self, master):
        """ Constructor """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets """
        #Label and buttons for entree
        Label(self, text = "What entree would you like").grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.entree = StringVar()
        self.entree.set(None)

        entree = ["Tomato soup", "A shrimp", "A salad"]
        column = 0
        for entrees in entree:
            Radiobutton(self, text = entrees, variable = self.entree, value = entrees).grid(row = 1, column = column, sticky = W)
            column += 1

        #Label and buttons for main course
        Label(self, text = "What main course would you like").grid(row = 2, column = 0, columnspan = 2, sticky = W)

        self.main_course = StringVar()
        self.main_course.set(None)

        main_course = ["Salmon", "Steak", "Vegetarian"]
        column = 0
        for main in main_course:
            Radiobutton(self, text = main, variable = self.main_course, value = main).grid(row = 3, column = column, sticky = W)
            column += 1

        #Label and buttons for desert
        Label(self, text = "What desert would you like").grid(row = 4, column = 0, columnspan = 2, sticky = W)

        self.desert = StringVar()
        self.desert.set(None)

        desert = ["Ice", "Pudding", "Frozen yogurt"]
        column = 0

        for des in desert:
            Radiobutton(self, text = des, variable = self.desert, value = des).grid(row = 5, column = column, sticky = W)
            column += 1

        #Create side dishes
        Label(self, text = "Would you like any side dishes?").grid(row = 6, column = 0, columnspan = 2, sticky = W)

        self.is_baguette = BooleanVar()
        Checkbutton(self, text = "Baguette", variable = self.is_baguette).grid(row = 7, column = 0, sticky = W)

        self.is_olive = BooleanVar()
        Checkbutton(self, text = "Olives", variable = self.is_olive).grid(row = 7, column = 1, sticky = W)

        self.is_cheese = BooleanVar()
        Checkbutton(self, text = "Cheese", variable = self.is_cheese).grid(row = 7, column = 2, sticky = W)

        #Checkplease button
        Button(self, text = "Check please!", command = self.check_out).grid(row = 8, column = 1, sticky = W)

        #Textbox
        self.check_txt = Text(self, width = 50, height = 12, wrap = WORD)
        self.check_txt.grid(row = 0, column = 3, rowspan = 9)

    def check_out(self):
        """ Creating the bill """
        message = "You have ordered:"
        total = 0

        entree = self.entree.get()
        main_course = self.main_course.get()
        desert = self.desert.get()

        #entree
        if entree == "Tomato soup":
            message += "\nTomato soup\t\t$4.49"
            total += 4.49
        if entree == "A shrimp":
            message += "\nA shrimp\t\t$6.49"
            total += 6.49
        if entree == "A salad":
            message += "\nA salad\t\t$5.95"
            total += 5.95

        #main course
        if main_course == "Salmon":
            message += "\nSalmon\t\t$17.75"
            total += 17.75
        if main_course == "Steak":
            message += "\nSteak\t\t$18.25"
            total += 18.25
        if main_course == "Vegetarian":
            message += "\nVegetarian\t\t$15.95"
            total += 15.95

        #desert
        if desert == "Ice":
            message += "\nIce\t\t$3.95"
            total += 3.95
        if desert == "Pudding":
            message += "\nPudding\t\t$3.49"
            total += 3.49
        if desert == "Frozen yogurt":
            message += "\nFrozen yogurt\t\t$4.25"
            total += 4.25

        #sidedishes
        if self.is_baguette.get():
            message += "\nBaguette\t\t$3.95"
            total += 3.95
        if self.is_olive.get():
            message += "\nOlives\t\t$4.65"
            total += 4.65
        if self.is_cheese.get():
            message += "\nCheese\t\t$89.95"
            total += 89.95

        message += "\n\nYour total: $" + str(total)

        self.check_txt.delete(0.0, END)
        self.check_txt.insert(0.0, message)



#main
root = Tk()
root.title("Order Up!")

app = Application(root)

root.mainloop()

