def get_sum(number):
	sum = 0
	newNumbers = str(number)
	for num in newNumbers:
		sum += int(num)
	return sum


#def get_sum(number):
#return(sum(int(num)for num in str(number)))