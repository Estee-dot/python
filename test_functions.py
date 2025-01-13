import unittest
import find_number

class TestFunctions(unittest.TestCase):
	def test_that_find_number_exist(self):
		x = [12, 17, 24, 32, 14]
		y = 24
		find_number.find_number(x, y)

	def test_that_find_number_returns_correct_value(self):
		x = [12, 17, 24, 32, 14]
		y = 24
		actual = find_number.find_number(x , y)
		expected = 2
		self.assertEqual(actual, expected)
		x = [4,3,4,8,9]
		y = 8
		actual = find_number.find_number(x, y)
		expected = 3
		self.assertEqual(actual, expected)

	def test_that_find_number_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, find_number.find_number, "estee")

	

