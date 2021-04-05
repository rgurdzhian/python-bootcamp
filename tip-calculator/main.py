print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

total_bill_with_tips = total_bill + total_bill * percentage / 100

price = round(total_bill_with_tips / number_of_people, 2)

formatted_price = "{:.2f}".format(price)

print(f"Each person should pay: ${formatted_price}")