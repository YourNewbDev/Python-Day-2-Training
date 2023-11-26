## (x/x) * 1.12

print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? ")

tip_percentage = input(
    "What percentage tip would you like to give? 10, 12, or 15? ")

people = input("How many people to split the bill? ")

total_bill = float(total_bill)
tip_percentage = float(tip_percentage)
people = int(people)

tip_percentage = total_bill * (tip_percentage / 100)
total_bill = total_bill + tip_percentage
total_bill_each = round(total_bill / people, 2)

print(f"Each person should pay: {total_bill_each}")
