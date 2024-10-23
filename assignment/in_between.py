inBetween = int(input("Enter a number between 0 and 1000"))

digit1 = inBetween / 100
number2 = inBetween / 10
digit2 = number2 % 10
digit3 = inBetween % 10;
	
sum = digit1 + digit2 + digit3;
print(f"Result of sum is"  {sum})
			
