def get_Element(numbers : list):
	largest = numbers[0]
	for number in numbers:
		if number > largest: largest = number
			return largest	

	
def get_Reversed_List(numbersReversed):
	for index in numbersReversed-1:
		print(numbersReversed[index] end= " ")
		

def get_Element_Occurance(number, specialValue):
	for index in len(number): 
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
	for letter in text; letter++){
		reversed = text.charAt(letter) + reversed;
		}
			if(reversed.equals(text)){
				return true;
			}
			return false;
	}

	public static void printSumOfNumbersOne(int[] numbers){
		int sum = 0;
		for(int number : numbers){
			sum += number;
		}
		System.out.print(sum);
	}

	public static void printSumOfNumbersTwo(int[] numbers){
		int counter = 0;
		int sum = 0;
		while(counter < numbers.length){
			sum += numbers[counter];
		counter++;
		}
		System.out.print(sum);
	}

	public static void printSumOfNumbersThree(int[] numbers){
		int counter = 0;
		int sum = 0;

		do{
			sum += numbers[counter];
		counter++;
		}
		while(counter < numbers.length);
		System.out.print(sum);
	}

	public static int[] printAddedList(int number){
		String newNumber = "";
		newNumber += number;
		int[] numbers = new int[newNumber.length()];

		for (int index = 0; index < newNumber.length(); index++) {
			int remainder = number % 10;
			numbers[(newNumber.length() - 1) - index] = remainder;
			number = number / 10;
		}

		return numbers;



	}
	



}