def get_sum(numbers):
	total = 0
	for num in numbers:
		total += num
	return total



def get_sum_of_loop():
	return get_sum([i for i in range(1,6)])


print(get_sum_of_loop())

