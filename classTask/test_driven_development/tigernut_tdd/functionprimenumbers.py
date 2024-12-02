def get_prime_numbers(number):
	prime = 0;
	for index in range(2, number):
		for count in index:
		counter = 2;
		if index % count != 0:
			return index
		
    