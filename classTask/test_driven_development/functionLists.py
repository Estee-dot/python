def get_Element(numbers : list):
	largest = numbers[0]
	for number in numbers:
		if number > largest: largest = number
			return largest	

	
def get_Reversed_List(numbersReversed):
	for index in numbersReversed-1:
		print(numbersReversed[index] end= " ")
		

def get_Element_Occurance(number, specialValue):
	for index in number: 
		if number[index] == specialValue:
			return true
	return false;



def get_OddElement(integers):
	for num in integers:			
		if integers[num[0]] % 2 != 0
			print(integers)

		
def get_Even_Element(integers):
	for num in integers:
		if(integers[num[0]] % 2 == 0){
			print (integers)
			

def get_Total(numbers):
	total = numbers[0];
	for number in numbers:
		total += number
	print(total)
		
	
def get_Palindrome(text):
	reversed = "";
	for letter in text:
		reversed = text + reversed		}
		if reversed.equals(text):
			return true
		return false

def get_SumOfNumbersOne(numbers):
	sum = 0
	for number in numbers:
		sum += number
	print(sum)
	

def get_SumOfNumbersTwo(numbers):
	counter = 0
	sum = 0
	while counter < numbers:
		sum += numbers[counter]
		counter++;
	print(sum)


def get_SumOfNumbersThree(numbers):
	counter = 0
	sum = 0
	do{
		sum += numbers[counter];
	counter++
	while counter < numbers:
		print(sum)
	

def get_AddedList(number):
	newNumber = ""
	newNumber += number
	numbers = new int[len(newNumber)]

	for index in newNumber:
		remainder = number % 10
		numbers[(len(newNumber)- 1) - index] = remainder
			number = number / 10
	return numbers;
