def get_sum_of_even_numbers(numbers : list):
	sum = 0
	for num in numbers:
		if num % 2 == 0:
			sum += num

	return sum
		

def get_even_sum(my_list):
	return[x for x in my_list if x % 2 == 0]