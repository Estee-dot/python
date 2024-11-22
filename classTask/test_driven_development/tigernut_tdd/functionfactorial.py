def get_factorial(number):
    factorial = 1
    for num in range(1, number+1):
        factorial = factorial * num
    return factorial