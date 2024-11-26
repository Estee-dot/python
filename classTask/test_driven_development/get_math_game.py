import random
def get_math_game():
	response = 0
	right_answer = [ ]
	positive_counter = 0
	negative_counter = 0
	counter = 0
	sign = ["+","+","+","+","+", "-","-", "*","*","*"]

while counter <= 10:
	for symbol in sign:
		answer1 = random.randrange(1, 1000)
		answer2 = random.randInt(1, 1000 )
		response = input(f"{answer1} + {answer2}")  
	
	response = int(input(f"{counter} what is {answer1} + {answer2}? "))
	if response == (f"{answer1} + {answer2}"):
		positive_counter += 1

	else:
		negative_counter += 1
	right_answer.append(f"{counter}, The right answer is {answer1} + {answer2}")
	count +=1

	print("The right answer is : ")
	for answer in right_answer:
		print(f"{answer}")

		return(f"The number of questions answered correctly is {positive_counter} \n The number of questions answered wrongly are {negative_counter}")

print(get_math_game())



	 

		
		
		
		

	

