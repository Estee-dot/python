#pseudo code: daysoftheweek
#prompt the user to enter a integer for today's day in the week
#prompt the user to enter number of days after today for the future day
#Calculate the future day by adding "today_day" + number_of_days
#
#display the future day of the week

	week_Day = ["Sunday" ,"Monday" ,"Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	
	today_day = int(input("Enter today's day: "))
	number_of_days = int(input("Enter the number of days elapased since today: "))
	sum_of_days = today_day + number_of_days	
	future_day_of_week = sum_of_days % 6

	if future_day_of_week == 0:
		print("Sunday")
	elif future_day_of_week == 1:
		print("Monday")
	elif future_day_of_week == 2:
		print("Tuesday")
	elif future_day_of_week == 3:
		print("Wednesday")
	elif future_day_of_week == 4:
		print("Thursday")
	elif future_day_of_week == 5:
		print("friday")	
	elif future_day_of_week == 6:
		print("Saturday")
	
print(f"Today is {week_day[today_day]} and the future day is {week_Day[future_day_of_week]}")
