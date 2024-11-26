def get_lists_in_list(integers : list):
	index1 = 0
	length = 0
	listOne = []
	listTwo = []

	for number in integers:
		length += 1 
	for count in range(length):
		if count <= length // 2:
			listOne.append(integers[index1])
			index1 += 1
		if count > length // 2:
			listTwo.append(intergers[index1])
			index1 += 1
	result = [listOne, listTwo]
	return result
	