#number = int(input("Enter a number: "))

prime = 0
number = 17
def get_even(number):
    for count in range(1, 11):
        if number / 2 == 0:
            print("Even number")
        else:
            print("Odd number")
get_even(number)
