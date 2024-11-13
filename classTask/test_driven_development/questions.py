import random
def get_math_game(questions):
	response = 0
	failed = [ ]
	postitive counter = 0
	negative counter = 0
	counter = 0
	sign = ["+","+","+","+","+", "-","-", "*","*","*"]

while counter <= 10:
	answer1 = random.randrange(1, 1000)
	answer2 = random.randInt(1, 1000 )
	for sign in count(0,1):
		response = input(f"{answer1} [0] {answer2}")  
	
	if {answer1} [0] {answer2} == response:
		print("correct answer")
		positive counter += 1

	else:
		negative counter += 1

	 

		
		
		
		

	

