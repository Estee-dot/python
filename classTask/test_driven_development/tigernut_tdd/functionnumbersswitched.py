def get_numbers_switched(numbers : list, integer):
	newNumber = numbers[:integer:]
	remaining = numbers[integer::] 
	new_List = remaining + newNumber
	return new_List


def get_numbers_switched(numbers : list, integer : int):
	for _ in range(number):
		each = number[0]
		numbers.remove(numbers[0])
		numbers.append(each)
	return numbers