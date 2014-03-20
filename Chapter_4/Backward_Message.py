print("\tWelcome to the Backward Message Program!")

print("This program will let you enter a message which\nwill be printed backwards by the computer!\n")

message = input("Please enter your message here: ")

backward_mess = ""

while message:
    position = len(message) - 1
    backward_mess += message[position]
    message = message[:position]

print("Here is the message printed backwards! ", backward_mess)

print("\n\nPress the enter key to exit.")

