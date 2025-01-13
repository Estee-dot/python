def find_number(numbers, number):
	try:
		index = numbers.index(number)
		return index
	except ValueError:
		return not available

