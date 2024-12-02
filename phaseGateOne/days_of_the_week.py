#pseudo code: daysoftheweek
#prompt the user to enter a integer for today's day in the week
#prompt the user to enter number of days after today for the future day
#Calculate the future day by adding "today_day" + number_of_days
#
#display the future day of the week

sum = 0
while today_day >= 0:

	today_day = int(input("Enter today's day: "))
	number_of_days = int(input("Enter the number of days elapased since today: "))
	sum = today_day + number_of_days	
	
	if today_day == 0:
		print("Sunday")
	elif today_day == 1:
		print("Monday")
	elif today_day == 2:
		print("Tuesday")
	elif today_day == 3:
		print("Wednesday")
	elif today_day == 4:
		print("Thursday")
	elif today_day == 5:
		print("friday")	
	elif today_day == 6:
		print("Saturday")
	
print(f"Today is {} and the future day is {}")
