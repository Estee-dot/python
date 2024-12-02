#pseudo code : increasing order
#- prompt the user to enter first number
#- store the number as "first_number"

#- prompt the user to enter second number
#- Store the number as "second_number"

#- prompt the user to enter third number
#- Store the number as "third_number"
#- initialize counter to 0
#- using a while loop, while counter is less than and equal to 3
#- compare if "first_number" > "second_number" and "second_number" > "third_number"
#- display "first_number", "second_number" and "third_number"
#- else if "second_number" > "first_number"  and "first_number" > "third_number"
#- display  "second_number","first_number" and "third_number"
#- else if "third_number" > "first_number" and "first_number" > "second_number" 
#- display  "second_number","first_number" and "third_number"




first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

if first_number > second_number and second_number > third_number:
	print(third_number, second_number, first_number, end = "")

elif second_number > first_number  and first_number > third_number:
	print(third_number, first_number, second_number, end = "")

elif third_number > first_number  and first_number > second_number:
	print(second_number, first_number, third_number, end = "")

elif third_number > second_number  and second_number > first_number:
	print(first_number, second_number, third_number, end = "")

elif second_number > third_number  and third_number > first_number:
	print(first_number, third_number, second_number, end = "")