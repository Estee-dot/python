def get_evenOdd_numbers(numbers : list):
	new_List = [ ]
	for num in numbers:
		if num % 2 == 0:
			new_List.append(True)
		else:
			new_List.append(False)

	return new_List	