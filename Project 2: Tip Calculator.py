print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_per = int(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
tip = (tip_per/100)*bill
total_bill = bill + tip
pay = total_bill/number_of_people
pay = round(pay,2)
print(f"Each person should pay: ${pay}")
