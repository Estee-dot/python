#pseudo code: Generate number:

#- using the random function generate two numbers
#- initialize sum to 0
#- prompt the user to calculate the sum of the two integers 
#- collect the result - store as sum 
#- if answer == generated_answer
#- print True
#- else print false





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