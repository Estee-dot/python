number = int(input("Give me a number: "))

even_number = 0
odd_number = 0

def get_even(number):
    for count in range(1, 11):
        if number % 2 == 0:
	    even_number = even_number + 1
            
        else if number % 2 != 0:
            odd_number = odd_number + 1
print("The even numbers are {even_number) \n the odd number are {odd_number}")
           
get_even(number)
