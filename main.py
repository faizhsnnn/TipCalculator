print("Welcome to the tip calculator!")
bill=float(input("What was the total bill?  $"))
tip=int(input("How much tip would you like to give? 10,20,or 15? "))
people=int(input("How many people to split the bill? "))
percent_ammount=(tip/100)*bill
total_bill= percent_ammount+bill
final_price= round(total_bill/people,2)
print(f"Each person should pay: ${final_price}")