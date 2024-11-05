fiveDigit = int(input("Enter five digits"))

firstOne = fiveDigit / 10000
secondNumber = fiveDigit / 1000
secondDigit = secondNumber % 10
thirdNumber = fiveDigit / 100
thirdDigit = thirdNumber % 10
fourthNumber = fiveDigit / 10
fourthDigit = fourthNumber % 10
fifthDigit = fiveDigit % 10

print(firstOne ,"   ",secondDigit,"   ", thirdDigit ,"   ",fourthDigit ,"   ",fifthDigit)
	 

