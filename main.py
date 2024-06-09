#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")

total_bill = input("What was the total bill? ")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
no_of_people = input("How many people to split the bill? ")

#total_bill string to just a number (remove $ sign)
total_bill = total_bill[1:]

#convert inputs to int or float
total_bill_as_float = float(total_bill)
tip_as_int = int(tip)
no_of_people_as_int = int(no_of_people)

#individual_bill = (total_bill / no_of_people) * (1 + tip / 100)
individual_bill = (total_bill_as_float / no_of_people_as_int) * (1 + tip_as_int / 100)
