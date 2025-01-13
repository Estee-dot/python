import unittest
import functioneven
import functionvowel
import functionanagram
import functionprime
import functionpalindrome
import functionaverage
import functionreversed
import functionodd
import functionsumofdigits
import functionacronym
import functionmagicnumbers
import functiongetnumbermerged
import functionsumevennumbers
import functionevencount
import functionoddEven
import get_capitalized
import functionmultiple
import functionoddnumbers
import functionsqaure
import functiongreater
import functionstringpalindrome
import functiongetnumbers
import functionaddition
import functionstringcount
import functiongetsum
import functionvowelsremoved
import find_number

class TestSumEvenFunction(unittest.TestCase):
	def test_that_get_even_numbers_exist(self):
		x = [1,2,3,4,5]
		functioneven.get_even_numbers(x)

	def test_that_get_even_numbers_returns_correct_value(self):
		actual = functioneven.get_even_numbers([1,2,3,4,6,9])
		expected = 12
		self.assertEqual(actual, expected)
		actual = functioneven.get_even_numbers([4,3,4,8,9])
		expected = 16
		self.assertEqual(actual, expected)

	def test_that_get_vowel_exist(self):
		char = "python is sweet"
		actual = functionvowel.get_vowel(char)
		expected = 4
		self.assertEqual(actual, expected)

	def test_that_get_vowel_returns_correct_value(self):
		char1 = "python is bitter"
		actual = functionvowel.get_vowel(char1)
		expected = 4
		self.assertEqual(actual, expected)

	def test_that_get_Anagram_exist(self):
		word1 = "silent"
		word2 = "listen"
		actual = functionanagram.get_Anagram(word1, word2)
		expected = True
		self.assertEqual(actual, expected)

	def test_that_get_Anagram_returns_correct_value(self):
		word1 = "evil"
		word2 = "live"
		actual = functionanagram.get_Anagram(word1, word2)
		expected = True
		self.assertEqual(actual, expected)

	def test_that_get_prime_number_exist(self):
		actual = functionprime.get_prime_number(7)
		expected = True
		self.assertEqual(actual, expected)

	def test_that_get_get_palindrome_exist(self):
		actual = functionpalindrome.get_palindrome("madam")
		expected = True

	def test_that_get_palindrome_correct_value(self):
		actual = functionpalindrome.get_palindrome("bacab")
		expected = True
	
	def test_that_get_average_exist(self):
		x = [12, 35 ,9, 4, 8]
		actual = functionaverage.get_average(x)
		expected = 13.6

	def test_that_get_average_correct_value(self):
		actual = functionaverage.get_average([1,2,3,4,6])
		expected = 3.2

	def test_that_get_string_reversed_exist(self):
		actual = functionreversed.get_string_reversed("hello")
		expected = "olleh"

	def test_that_get_string_reversed_correct_value(self):
		actual = functionreversed.get_string_reversed("esther")
		expected = "rehtse"

	def test_that_get_sum_of_odd_digits_exist(self):
		x = [1,2,3,4,5]
		functionodd.get_sum_of_odd_digits(x)

	def test_that_get_sum_of_odd_digits_returns_correct_value(self):
		actual = functionodd.get_sum_of_odd_digits([1,5,8,9,4])
		expected = 15
		self.assertEqual(actual, expected)

	def test_that_get_sum_of_digits_exist(self):
		x = [2, 6, 9, 12, 14, 18]
		functionsumofdigits.get_sum_of_digits(x)

	def test_that_get_sum_of_digits_returns_correct_value(self):
		actual = functionsumofdigits.get_sum_of_digits([1,5,8,9,4])
		expected = 27
		self.assertEqual(actual, expected)

	def test_that_get_acronym_exist(self):
		functionacronym.get_acronym("Portable Network Graphics")

	def test_that_get_magic_numbers_exist(self):
		x = [1,2,3,4]
		functionmagicnumbers.get_magic_numbers(x)

	def test_that_get_magic_numbers_returns_correct_value(self):
		actual = functionmagicnumbers.get_magic_numbers([1,2,3,4,5,6])
		expected = 105
		self.assertEqual(actual, expected)

	def test_that_get_number_merged_exist(self):
		numberOne = [3,4,9,10]
		numberTwo = [1,5,7,8]
		functiongetnumbermerged.get_number_merged(numberOne, numberTwo)

	def test_that_get_number_merged_returns_correct_value(self):
		numberOne = [3,4,9,10,-5]
		numberTwo = [1,5,7,8,32]
		actual = functiongetnumbermerged.get_number_merged(numberOne, numberTwo)
		expected = [-5,1,3,4,5,7,8,9,10,32]
		self.assertEqual(actual, expected)

	def test_that_get_sum_of_even_numbers_exist(self):
		numbers = [3,4,9,10]
		functionsumevennumbers.get_sum_of_even_numbers(numbers)

	def test_that_get_sum_of_even_numbers_correct_value(self):
		numberOne = [2,7,9,17,19,2,8,10]
		actual = functionsumevennumbers.get_sum_of_even_numbers(numberOne)
		expected = 22
		self.assertEqual(actual, expected)

	def test_that_get_even_count_exist(self):
		x = [1,5,7,3,2,9,8,10]
		functionevencount.get_even_count(x)


	def test_that_get_even_count_returns_correct_value(self):
		x = [1,5,7,3,2,9,8,10]
		actual = functionevencount.get_even_count(x)
		expected = 3
		self.assertEqual(actual, expected)
		
	def test_that_get_boolean_value_exist(self):
		x = [1,5,7,3,2,9,8,10]
		functionoddEven.get_boolean_value(x)

	def test_that_get_boolean_value_returns_correct_value(self):
		x = [10,3,7,1,9,4,2,8,5,6]
		actual = functionoddEven.get_boolean_value(x)
		expected = [True, False, False, False, False, True, True, True, False, True]
		self.assertEqual(actual, expected)
	

	def test_that_get_capitalized_exist(self):
		x = ['red', 'orange', 'yellow', 'green', 'blue']
		get_capitalized.get_capitalized(x)

	def test_that_get_capitalized_returns_correct_value(self):
		x = ['red', 'orange', 'yellow', 'green', 'blue']
		actual = get_capitalized.get_capitalized(x)
		expected = ['Red', 'Orange', 'Yellow', 'Green', 'Blue']
		self.assertEqual(actual, expected)

	def test_that_get_multiple_of_3_exist(self):
		x = [3,6,9,12,15,18,21,24,27,30]
		functionmultiple.get_multiple_of_3(x)

	def test_that_get_Odd_numbers_exist(self):
		x = [3,6,9,12,15,18,21,24,27,30]
		functionoddnumbers.get_Odd_numbers(x)

	def test_that_get_Odd_numbers_returns_correct_value(self):
		x = [10,3,7,1,9,4,2,8,5,6]
		actual = functionoddnumbers.get_Odd_numbers(x)
		expected = [9,49,1,81,25]
		self.assertEqual(actual, expected)


	def test_that_get_square_of_number_exist(self):
		x = 4
		functionsqaure.get_square_of_number(x)

	def test_that_get_square_of_number_returns_correct_value(self):
		x = 4
		actual = functionsqaure.get_square_of_number(x)
		expected = [1,4,9,16]
		self.assertEqual(actual, expected)

	def test_that_get_number_greater_exist(self):
		x = [1,5,12,15,8]
		functiongreater.get_number_greater(x)

	def test_that_get_number_greater_returns_correct_value(self):
		x = [1,5,12,15,6]
		actual = functiongreater.get_number_greater(x)
		expected = [12, 15]
		self.assertEqual(actual, expected)

	def test_that_get_string_palindrome_exist(self):
		x = ['madam', 'apple' , 'racecar']
		functionstringpalindrome.get_string_palindrome(x)


	def test_that_get_string_palindrome_returns_correct_value(self):
		x = ['madam', 'apple' , 'racecar']
		actual = functionstringpalindrome.get_string_palindrome(x)
		expected = [True , False , True]
		self.assertEqual(actual, expected)

	def test_that_get_numbers_exist(self):
		x = 'abc123def456'
		functiongetnumbers.get_int(x)

	def test_that_get_numbers_returns_correct_value(self):
		x = 'abc123def456'
		actual = functiongetnumbers.get_int(x)
		expected = [1,2,3,4,5,6]
		self.assertEqual(actual, expected)

	def test_that_get_numbers_doubled_exist(self):
		x = [1,2,3]
		functionaddition.get_numbers_doubled(x)

	def test_that_get_numbers_doubled_returns_correct_value(self):
		x = [1,2,3]
		actual = functionaddition.get_numbers_doubled(x)
		expected = [2,4,6]
		self.assertEqual(actual, expected)

	def test_that_get_string_count_exist(self):
		x = ["Apple", "Fish", "Orange", "Ice", "Lime"]
		functionstringcount.get_string_count(x)

	def test_that_get_sum_exist(self):
		x = 192374
		functiongetsum.get_sum(x)
		
	def test_that_get_sum_returns_correct_value(self):
		x = 192374
		actual = functiongetsum.get_sum(x)
		expected = 26
		self.assertEqual(actual, expected)

	def test_that_get_vowels_removed_exist(self):
		x = ["orange","apple","ice","Beans","Rice"]
		functionvowelsremoved.get_vowels_removed(x)

	def test_that_find_number_exist(self):
		x = [12, 17, 24, 32, 14]
		functionvowelsremoved.get_vowels_removed(x)















	

	

	

