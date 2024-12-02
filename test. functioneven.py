import unittest
import functionsumevennumbers


class TestEvenNumbersFunction(unittest.TestCase):
	def test_that_get_sum_of_even_numbers_exist(self):
		x = [1,2,3,4,6,9]
		functionsumevennumbers.get_sum_of_even_numbers(x)