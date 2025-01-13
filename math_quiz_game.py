import random

def math_quiz_game():
	sign = ["+", "*", "-"]
	right_answer = []
	count = 0
	passed = 0
	failed = 0
	while count < 5:
		rand1 = random.randrange(1,20)
		rand2 = random.randrange(1,20)
		counter = random.randrange(0,3)
		
		try:
			question = int(input(f"What is {rand1} {sign[counter]} {rand2} ? "))

			print(f"your answer is : {question}")

			if counter == 0:
				answer = rand1 + rand2
			elif counter == 1:
				answer = rand1 * rand2
			elif counter == 2:
				answer = rand1 - rand2

			if answer == question:
				passed += 1
				print("Correct!!")
			else: 
				failed += 1
				print("Wrong")
		
			right_answer.append(f"You missed question {count
+1}: The correct answer for {rand1} {sign[counter]} {rand2} is {answer}")
			count += 1

		except ValueError:
			print("Invalid Input")

	for result in right_answer:
		print(result)

	return (f"Your score is {passed} / 5")
	print("Thank you for playing")			

print(math_quiz_game())
