import random 

sum = 0
first_random = random.randrange(1,101)
second_random = random.randrange(1,101)

sum = first_random + second_random
user_input = int(input("Enter the sum of the number: "))
sum += random
if user_input == sum:
	print("True")
else:
	print("False")