def get_even_numbers(number: list):
    sum = 0
    for num in number:
        if num % 2 == 0:
            sum += num
    return sum
	

