total_bill = int(input("Please enter your total bill: "))

tip15 = total_bill * 0.15
tot15 = tip15 + total_bill
print("\nThis will be a 15% tip:", tip15, "and in total you will pay", tot15)

tip20 = total_bill * 0.20
tot20 = tip20 + total_bill
print("\nThis will be a 20% tip:", tip20, "and in total you will pay", tot20)

input("\n\nPress the enter key to exit.")
