import math
def get_square_root(number):
	if type(number) in [int, float]:
		if number % 5 == 0:
			square = math.sqrt(number)
			return round(square,2)
    
	elif number % 5 != 0:
		remainder = number % 5
		return round(remainder,2)

	return TypeError
 
	
		