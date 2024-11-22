def get_sum_of_odd_digits(number : list):
    sum = 0
    for num in number:
        if num % 2 != 0:
            sum += num
    return sum
	