import random
import time

def get_math_questions():
	
	sign = ["-", "-" , "-" , "-" , "-", "-", "-" , "-" , "-" , "-"]
	counter = 0
	passed = 0
	failed = 0
	numbers = []
	right_answer = []

	while counter <= 10:
		first_number = random.randrange(1, 100)
		second_number = random.randrange(1, 100)
	

	question = int(input(f"Calculate {first_number} {sign[counter]} {second_number}: "))
	answer = first_number - second_number
		
	if answer == question:
		passed += 1
	else: 
		failed += 1
	right_answer.append(f"You missed question {counter+1}, The correct answer for {first_number} {sign[counter]} {second_number} is {answer}")
	counter += 1
			
	for result in right_answer:
		print(result)

	return (f"Your score is {passed} / {failed}")

print(get_math_questions())