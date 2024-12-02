import unittest
import functionevenOddnumbers
import functionnumbersswitched


class TestEvenOddNumbersFunction(unittest.TestCase): 
	def test_that_get_even_Odd_numbers_exist(self):
		x = [1,2,3,4,5]
		functionevenOddnumbers.get_evenOdd_numbers(x)

	def test_that_get_even_Odd_numbers_returns_correct_value(self):
		actual = functionevenOddnumbers.get_evenOdd_numbers([1,2,3,4,6,9])
		expected = [False, True, False, True, True, False]
		self.assertEqual(actual, expected)
		actual = functionevenOddnumbers.get_evenOdd_numbers([4,3,4,8,9])
		expected = [True, False, True, True, False]
		self.assertEqual(actual, expected)

	def test_that_get_numbers_switched_exist(self):
		x = [1,2,3,4,5]
		y = 3
		functionnumbersswitched.get_numbers_switched(x, y)

	def test_that_get_numbers_switched_returns_correct_value(self):
		x = [1,2,3,4,6,9]
		y = 2
		actual = functionnumbersswitched.get_numbers_switched(x, y)
		expected = [3,4,6,9,1,2]
		self.assertEqual(actual, expected)

	

		
		

