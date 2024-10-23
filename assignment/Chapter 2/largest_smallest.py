firstInteger = int(input("Enter first number: "))
secondInteger = int(input("Enter second number: "))
thirdInteger = int(input("Enter second number: "))

addition = firstInteger + secondInteger + thirdInteger;
average = addition / 3;
product = firstInteger * secondInteger * thirdInteger;
	
int largest = 0;
int smallest = 0;
	
if firstInteger > secondInteger && firstInteger > thirdInteger:
    largest = firstInteger
		
elif secondInteger > firstInteger && secondInteger > thirdInteger:
		largest = secondInteger
		
elif thirdInteger > secondInteger && thirdInteger > firstInteger:
		largest = thirdInteger;
		
else:
	print("They are all equal")

if firstInteger < secondInteger && firstInteger < thirdInteger:
		smallest = firstInteger
		
elif secondInteger < firstInteger && secondInteger < thirdInteger:
		smallest = secondInteger
		
elif thirdInteger < secondInteger && thirdInteger < firstInteger:
		smallest = thirdInteger
		
else:
	print("They are all equal")
	
	print(f"%nThe largest is %d%n" , largest)
	print(f"The smallest is %d" , smallest)