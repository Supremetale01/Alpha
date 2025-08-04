print("Welcome to the Tip Calculator")
meal_price = float(input("What is the total bill? $"))
#tip in percentage
tip = int(input("What's the tip percentage you want to give? "))
People_number = int(input("Total number of people splitting the bill? "))
Tip_amount = (tip / 100) * meal_price
Tiptotalamount = Tip_amount + meal_price
bills_per_person = Tiptotalamount / People_number
print(f"The bill to be shared per person should be: ${bills_per_person} ")