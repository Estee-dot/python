
number = 6
def get_prime(number):
    for count in range(1, 12):
        if number % count == 0:
            print("True")
        else:
            print("False")
get_prime(number)
