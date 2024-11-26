from unittest import TestCase 
import functionmultiple

class TestMultipleFunction(TestCase):
	def test_that_multiple_function_exists(self):
		functionmultiple.multiple_of_number(2, 4)

	def test_that_multiple_function_returns_correct_value(self):
		actual = functionmultiple.multiple_of_number(2, 10)
		expected = 20
		actual = functionmultiple.multiple_of_number(7, 9)
		expected = 63

	def test_that_checks_multiple_with_invalid_input(self):
		self.assertRaises(TypeError, functionmultiple.multiple_of_number, "esther")

	def test_function_returns_correct_value_with_float(self):
		actual = functionmultiple.multiple_of_number(2.5 , 4.5)
		expected = 11.25



		                 



                                                                    