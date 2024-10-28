count = 0
positive = 0
negative = 0
zero = 0

while count <= 5:
    integer = int(input("Enter a number: " ))
    if integer > 0:
        positive += 1
			
    if integer < 0:
        negative += 1
			
    else:
        zero += 1
        count += 1

		
print("the number of positive is: " , positive)
print("the number of negative is: " , negative)
print("the number of zero is: " , zero)
		
	
	