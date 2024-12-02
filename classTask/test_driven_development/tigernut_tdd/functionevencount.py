def get_even_count(numbers : list):
	count = 0
	for num in numbers:
		if num % 2 == 0:
			count += 1
	return count
		

def get_even_count(my_list):
	return len([x for x in my_list if x % 2 == 0])