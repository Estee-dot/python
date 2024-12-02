#pseudo code : math_question:

#- import random
#- import time
#- randomly generate 10 subtraction questions
#- initialize counter to 0
#- initialize passed to 0
#- initialize failed to 0
#- create an empty list called "right_answers"
#- Prompt the user to enter Start time of the test

import random
import time

def get_math_question():
	stop_timer = time.time()
	response = 0
	right_answer = [ ]
	positive_counter = 0
	negative_counter = 0
	counter = 1
	sign = ["-","-","-","-","-", "-","-", "-","-","-"]

	while counter <= 10:
		for symbol in sign:
			answer1 = random.randrange(1, 100)
			answer2 = random.randrange(1, 100) 
 
		response = int(input(f"{counter} what is {answer1} - {answer2}? "))
		if response == (f"{answer1} - {answer2}"):
			positive_counter += 1
		else:
			negative_counter += 1
		right_answer.append(f"{counter}. The right answer is {answer1} - {answer2}")
		counter += 1
		print("The right answer is : ")

		for answer in right_answer:
			print(f"{answer}")
	return(f"The number of questions answered correctly is {positive_counter} \n The number of questions answered wrongly are {negative_counter}")

print(get_math_question())



	 

		
		
		
		

	

