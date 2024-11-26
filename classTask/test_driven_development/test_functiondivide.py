import unittest
import functiondivide
import functioninvest

class TestDivisionOrSquare(unittest.TestCase):
	def test_that_get_square_root_exist(self):
		functiondivide.get_square_root(512)

	def test_that_get_square_root_is_divisible_by_5(self):
		actual = functiondivide.get_square_root(10)
		expected = 3.16
		self.assertEqual(actual, expected)
		actual = functiondivide.get_square_root(25)
		expected = 5
		self.assertEqual(actual, expected)

	def test_that_get_square_root_returns_remainder(self):
		actual = functiondivide.get_square_root(21)
		expected = 1
		self.assertEqual(actual, expected)
		actual = functiondivide.get_square_root(63)
		expected = 6

	def test_that_on_get_square_root_with_negative_value(self):
		 self.assertRaises(TypeError, functiondivide.get_square_root, (-1))

	def test_that_get_square_root_returns_correct_value_with_float(self):
		actual = functiondivide.get_square_root(20.12)
		expected = 0.12
		self.assertEqual(actual, expected)

	def test_that_get_square_root_function_detects_string(self):
		self.assertRaises(TypeError, functiondivide.get_square_root, "estherBigFish", "chicken")

	def test_that_get_investment_exist(self):
		functioninvest.get_investment(1000, 5, 12)

	def test_that_get_investment_returns_correct_Value(self):
		actual = functioninvest.get_investment(1000, 1, 12)
		expected = 1126.83
		self.assertEqual(actual, expected)

	def test_that_get_investment_function_detects_string(self):
		self.assertRaises(TypeError, functioninvest.get_investment, "DivineBigchicken", "chicken", "cowhead")

	


	





		






		