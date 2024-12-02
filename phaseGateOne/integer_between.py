#pseudo code: integer between 0 and 1000:

#- prompt the user to enter an integer between 0 and 1000
#- convert the number to string
#- create a for loop that loops through the number the user enters
#- using the .isdigits() method to separate the numbers







number = int(input("Enter an integer that is between 0 and 1000: ")
sum = 0
newNumbers = str(number)
for num in newNumbers:
	sum += int(num)
print(sum)


