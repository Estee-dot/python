largest = 0
smallest = 0
userValue

while userValue != 0:
    userValue = int(input("Enter a number or 0 to stop the operation: "))

        if userValue > largest:
	    largest = userValue
	else if userValue < smallest:
	    smallest = userValue
	
print("Largest is {largest} smallest is {smallest}") 
