number_inbetween =int(input("Enter a number between 100 and 999: "))
digit1 = number_inbetween // 100 
number1 = number_inbetween // 10
digit2 = number1 % 10 
digit3 = number_inbetween % 10 

print(digit3, digit2, digit1)

odd = even = 0
    
if digit1 % 2 == 0:
        even += 1
else:
        odd += 1
    
if digit2 % 2 == 0:
        even += 1
else:
        odd += 1
        
if digit3 % 2 == 0:
        even += 1
else:
        odd += 1

print("Even number is " , even)
print("Odd number is " , odd)
	
