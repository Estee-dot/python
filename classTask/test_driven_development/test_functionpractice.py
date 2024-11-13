import unittest
import functionpractice

class TestMultiplicationFunction(unittest.TestCase):
	def test_that_get_product_exist(self):
		functionpractice.get_product(2, 6)

	def test_that_multiple_returns_correct_value(self):
		actual = functionpractice.get_product(5, 10)
		expected = 50
		self.assertEqual(actual, expected)
		actual = functionpractice.get_product(7, 5)
		expected = 35
		self.assertEqual(actual, expected)

	def test_on_product_with_negative_value(self):
		actual = functionpractice.get_product(5, -10)
		expected = -50
		self.assertEqual(actual, expected)
		actual = functionpractice.get_product(-5, -10)
		expected = 50
		self.assertEqual(actual, expected)
		actual = functionpractice.get_product(-5, 10)
		expected = -50
		self.assertEqual(actual, expected)

	def test_that_product_function_detects_string(self):
		self.assertRaises(TypeError, functionpractice.get_product, "estherBigFish", "chicken")










		

		

		