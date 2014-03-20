print("\tWelcome to the Counter Program!")

print("This program will let you enter a begin number, an end number\nand the step size, then the computer will count for you!")

begin = int(input("\nWhat is the beginning number? "))
end = int(input("\nWhat is the end number? ")) + 1
step_size = int(input("\nFinally, what is the step size? "))

for number in range(begin, end, step_size):
    print(number)

input("\n\nPress the enter key to exit.")