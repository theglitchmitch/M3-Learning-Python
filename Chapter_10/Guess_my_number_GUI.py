from tkinter import *
import random

class Application(Frame):
    """ GUI for Guess My Number """

    def __init__(self, master):
        """ Constructor """
        super(Application, self).__init__(master)
        self.the_number = random.randint(1, 100)
        self.tries = 1
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create the widgets """
        #Labels
        Label(self, text = "I'm thinking of a number between 1 and 100.").grid(row = 0, column = 0, sticky = W)
        Label(self, text = "Try to guess it in as few attempts as possible.").grid(row = 1, column = 0, sticky = W)

        #Text entry
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row = 2, column = 0, sticky = W)

        #Submit button
        Button(self, text = "Submit", command = self.guess_num).grid(row = 2, column = 0, sticky = N)

        #Text
        self.guess_txt = Text(self, width = 40, height = 3, wrap = WORD)
        self.guess_txt.grid(row = 3, column = 0, columnspan = 2)

    def guess_num(self):
        """ The guessing method"""
        guess = int(self.guess_ent.get())
        message = ""

        # guessing loop
        if guess > self.the_number:
            self.guess_txt.delete(0.0, END)
            self.guess_txt.insert(0.0, "Lower...")
            self.tries += 1
        elif guess < self.the_number:
            self.guess_txt.delete(0.0, END)
            self.guess_txt.insert(0.0, "Higher...")
            self.tries += 1
        elif guess == self.the_number:
            message += "You guessed it! The number was "
            message += str(self.the_number)
            message += "\nAnd it only took you "
            message += str(self.tries)
            message += " tries!"

            self.guess_txt.delete(0.0, END)
            self.guess_txt.insert(0.0, message)

#main
root = Tk()
root.title("Guess my Number")

app = Application(root)

root.mainloop()