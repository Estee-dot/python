def get_boolean_value(numbers : list):
	new_List = []
	for num in numbers:
		if num % 2 == 0:
			new_List.append(True)
		else:
			new_List.append(False)

	return new_List	

#def get_evenOdd(my_list):
	#return [True if x % 2 == 0 else False for num in my_list]