price = int(input("Please enter the base price of the car: "))

print("\nThese are the extra fees you'll have to pay:")

tax_price = price * 0.15
tax = print("Tax: This is 15% of the base price of the car, which in your case is:", tax_price)

license_price = price * 0.10
car_license = print("License: This is 10% of the base price of the car, which in your case is:", license_price)

dealer_price = 2000
dealer_prep = print("Dealer Prep: This is a set value for each costumer:", dealer_price)

des_price = 1500
des_charge = print("Destination Charge: This is a set value for each costumer:", des_price)

tot_price = price + tax_price + license_price + dealer_price + des_price
print("\nThe total amount you'll have to pay:", tot_price)

input("\n\nPress the enter key to exit.")