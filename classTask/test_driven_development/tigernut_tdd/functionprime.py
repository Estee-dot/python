def get_prime_number(number):
    for count in range(2,number):
        if number % count == 0:
            return False
        else:
            return True
