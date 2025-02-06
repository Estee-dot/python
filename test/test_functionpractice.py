import unittest
import functionpractice
import functionsum
import functionremove
import functiongrade

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

	def test_that_get_sum_exists(self):
		x = [3,4,5,6]
		functionsum.get_sum(x)

	def test_that_get_sum_returns_correct_value(self):
		actual = functionsum.get_sum([1,5,7,12])
		expected = 25
		self.assertEqual(actual, expected)

	def test_that_get_sum_returns_correct_negative_value(self):
		actual = functionsum.get_sum([-1 ,-9,-3])
		expected = -13
		self.assertEqual(actual, expected)

	def test_that_get_number_removed_exists(self):
		x = [3,4,5,6]
		functionremove.get_number_removed(x)

	def test_that_get_sum_returns_correct_value(self):
		actual = functionremove.get_number_removed([1, 9, 7, 2, 5, 4])
		expected = [1, 9, 2, 5, 4]
		self.assertEqual(actual, expected)

	def test_that_get_student_grade_exists(self):
		x = ["Gloria", "Divine", "Bibi", "Emmanuel", "Christian", "Samuel", "Moses", "Leke", "Tosin"]
		y = [50 , 60, 70, 30, 80, 65, 45, 82, 90, 20]
		functiongrade.get_student_grade(x, y)

	def test_that_get_student_grade_returns_highest_grade_in_py(self):
		actual = functiongrade.get_student_grade(["Gloria", "Divine", "Bibi", "Emmanuel", "Christian", "Samuel", "Moses", "Leke", "Tosin"])
		expected = [50 , 60, 70, 30, 80, 65, 45, 82, 90, 20]
		self.assertEqual(actual, expected)





	







		

		

		